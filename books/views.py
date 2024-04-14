from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet






class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'statud': f"Returned {len(books)}",
            'books': serializer_data
        }
        return Response(data)

class BookCreatedApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status': 'Kitob saqlandi',
                'books': data
            }
            return Response(data)
        else:
            return Response(
            {
                'status': False,
                'message': 'Serializer is not valid'
            }, status=status.HTTP_400_BAD_REQUEST
            )


class BookDetailApiView(APIView):

    def get(self, request, pk, *args, **kwargs):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data

            data = {
                'status': 'Succesfull',
                'book': serializer_data
            },
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {'status': 'Does not exists',
                 'message': 'Book is not fount'
                 }, status=status.HTTP_404_NOT_FOUND
            )


class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                'status': True,
                'message': 'Succesfull delete'
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': False,
                'message': 'Book is not fount'
            }, status=status.HTTP_404_NOT_FOUND)


class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
            return Response({
                'status': True,
                'message': f"Book {book_saved} updated successfully"
            })
        

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
