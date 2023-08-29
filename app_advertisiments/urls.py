from django.urls import path

from .views import index, top_sellers
from .views import advertisiment_post


urlpatterns = [
    path("", index, name="main-page"),
    path("top-sellers/", top_sellers, name="top-sellers"),
    path("advertisiment-post/", advertisiment_post, name="adv-post")
]
