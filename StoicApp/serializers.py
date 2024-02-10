from .models import Phrases,Filosofo,Picture;
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer;

class FilosofoSerializer(ModelSerializer):
    class Meta:
        model = Filosofo
        fields = "__all__"

class PhrasesSerializer(ModelSerializer):
    class Meta:
        model = Phrases
        fields = "__all__"


class PictureSerializer(ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"