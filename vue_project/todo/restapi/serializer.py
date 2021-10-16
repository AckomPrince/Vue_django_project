from rest_framework import serializers
from .models import Blogger
class BloggerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogger
        fields = ['pk', 'url', 'first_name', 'last_name', 'age' , 'region', 'city', 'description']
        