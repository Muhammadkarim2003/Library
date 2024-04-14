from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (BookListApiView, BookCreatedApiView, BookDetailApiView,
                    BookDeleteApiView, BookUpdateApiView, BookUpdateApiView, BookViewSet)


router = SimpleRouter()
router.register('books', BookViewSet, basename='books')


urlpatterns = [
    #ApiView
    # path('bookss/', BookListApiView.as_view()),
    # path('books-created/', BookCreatedApiView.as_view()),
    # path('detail/<int:pk>/', BookDetailApiView.as_view()),
    # path('delete/<int:pk>/', BookDeleteApiView.as_view()),
    # path('update/<int:pk>/', BookUpdateApiView.as_view()),
]

urlpatterns = urlpatterns + router.urls
