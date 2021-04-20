from django.urls import path, include
from . import views
from book.router import router


urlpatterns = [
    path('books/', include(router.urls)),
    path('post/q=<category>/', views.post_books, name="post_books"),
]
