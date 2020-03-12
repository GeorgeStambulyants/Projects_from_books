from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm, SearchForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
        search_query = SearchQuery(query)
        results = Post.objects.annotate(similarity=TrigramSimilarity('title', query)).\
                                        filter(similarity__gte=0.3).order_by('-similarity')
    return render(request, 'blog/post/search.html', {'form': form,
                                                         'query': query,
                                                         'results': results})


def post_share(request, post_id):
    # Получение статьи по идентификатору
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        # Форма была отправлена на сохранение
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Все поля формы прошли валидацию
            cd = form.cleaned_data
            # ... Отправка электронной почты
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd["name"]} ({cd["email"]}) recommends you reading "{post.title}"'
            message = f'Read "{post.title}" at {post_url}\n\n{cd["name"]} comments: {cd["comments"]}'
            send_mail(subject, message, 'admin@blog.com', [cd['to']])
            sent = True
        else:
            form = EmailPostForm()
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html',
                            {'post': post, 'form': form, 'sent': sent})


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request, tag_slug=None):
    object_list = Post.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_lists = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, return first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page number is greater than all the pages, return the last page
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts, 'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',  #  all posts are draft, so there are no matches
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)

    # Список активных комментариев для этой статьи
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # User send comment
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid:
            #  Создаем комментарий, но пока не сохраняем в базе данных
            new_comment = comment_form.save(commit=False)
            # Привязываем комментарий к текущей статье.
            new_comment.post = post
            # Сохраняем комментарий в базе данных
            new_comment.save()
    else:
        comment_form = CommentForm()
    post_tags_id = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_id).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    return render(request, 'blog/post/detail.html',
                            {'post': post,
                             'comments': comments,
                             'new_comment': new_comment,
                             'comment_form': comment_form,
                             'similar_posts': similar_posts})
