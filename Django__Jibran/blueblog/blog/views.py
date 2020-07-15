from django.urls import reverse, reverse_lazy
from django.http.response import (
    HttpResponseRedirect, HttpResponseForbidden,
)
from django.utils.text import slugify
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import BlogForm
from .models import Blog


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            if Blog.objects.filter(owner=self.request.user).exists():
                ctx['has_blog'] = True
                ctx['blog'] = Blog.objects.get(owner=self.request.user)

        return ctx


class NewBlogView(CreateView):
    form_class = BlogForm
    template_name = 'blog_settings.html'

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.owner = self.request.user
        blog_obj.slug = slugify(blog_obj.title)
        blog_obj.save()

        return HttpResponseRedirect(reverse('home'))

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if Blog.objects.filter(owner=user).exists():
            return HttpResponseForbidden(
                'You can not create more than one blog per account'
            )
        return super(NewBlogView, self).dispatch(request, *args, **kwargs)


class UpdateBlogView(UpdateView):
    form_class = BlogForm
    template_name = 'blog_settings.html'
    success_url = reverse_lazy('home')
    model = Blog

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateBlogView, self).dispatch(request, *args, **kwargs)
