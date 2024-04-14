from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'isbn', 'price')


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.isalpha():
            raise ValidationError({
                'ststus': False,
                'message': 'Kitobni sarlavhasini harf bilan kiriting'
                }
            )
        
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({
                'status': False,
                'message': 'Kitob sarlavha va muallifi birxillarini kirita olmaysiz'
            })

        return data
    
    def validate_price(self, price):
        if price < 0 or price > 9999999:
            raise ValidationError({
                'status': False,
                'message': 'Narx notug\'ri kiritilgan'
            })


