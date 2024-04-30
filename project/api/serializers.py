from api.models import Movie 
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    # add new field without add in model field
    len_of_name = serializers.SerializerMethodField() 
    def get_len_of_name(self,object):
        length = len(object.name)
        return length
    class Meta:
        model = Movie
        fields = '__all__'
    