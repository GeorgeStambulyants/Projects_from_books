from django.test import TestCase
from django.test.client import RequestFactory
from django.urls.base import reverse

from . models import Movie
from . views import MovieList


class MovieListPaginationTestCase(TestCase):

    ACTIVE_PAGINATION_HTML = '''
        <li class="page-item">
            <a href="{}?page={}" class="page-link">
            {}
            </a>
        </li>
    '''

    def setUp(self):
        for n in range(15):
            Movie.objects.create(title=f'Title {n}',
                                 year=1990 + n,
                                 runtime=100)

    def test_first_page(self):
        movie_list_path = reverse('core:MovieList')
        request = RequestFactory().get(path=movie_list_path)
        response = MovieList.as_view()(request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(movie_list_path, 1, 'First'),
            response.rendered_content
        )
