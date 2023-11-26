from rest_framework import serializers
from artist.models import artist,album

class artistSerializer(serializers.ModelSerializer):
    class Meta:
        model = artist
        fields = '__all__'

class albumSerializer(serializers.ModelSerializer):
    class Meta:
        model = album
        fields = '__all__'

