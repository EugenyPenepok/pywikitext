from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_categories$', views.get_categories, name='get_categories'),
    url(r'^post_tree_categories', views.post_tree_categories, name='post_tree_categories'),
    url(r'^get_headers', views.get_headers, name='get_headers')
]