from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .models import Phrases,Filosofo,Picture
from .serializers import PhrasesSerializer, FilosofoSerializer,PictureSerializer, UserSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.
def test(request):
    return HttpResponse("hello world")


## FILOSOFO ##

## Apenas Listagem ##
class FilosofoView(ListAPIView):
    queryset = Filosofo.objects.all()
    serializer_class = FilosofoSerializer

## Listar filtrando apenas um ##
class SingleFilosofoView(RetrieveAPIView):
    queryset = Filosofo.objects.all()
    serializer_class = FilosofoSerializer

## Listar e permitir postagem ##
class FilosofoListAdmin(ListCreateAPIView):
    queryset = Filosofo.objects.all()
    serializer_class = FilosofoSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

## Listar apenas um e permitir que delete ##

class SingleFilosofoAdmin(RetrieveUpdateDestroyAPIView):
    queryset = Filosofo.objects.all()
    serializer_class = FilosofoSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


## PHRASES ##

#Todas as frases
class PhrasesView(ListAPIView):
    queryset = Phrases.objects.all()
    serializer_class = PhrasesSerializer


# Frase por filosofo
class FilosofoPhrasesView(ListAPIView):
    serializer_class = PhrasesSerializer

    def get_queryset(self):
        filosofo_id = self.kwargs['filosofo_id']
        return Phrases.objects.filter(philosopher_id=filosofo_id)

#Frase Individual
class SinglePhraseView(RetrieveAPIView):
    queryset = Phrases.objects.all()
    serializer_class = PhrasesSerializer

# Lista de frases post + get
class PhrasesListAdmin(ListCreateAPIView):
    queryset = Phrases.objects.all()
    serializer_class = PhrasesSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

# Frase individual todos os CRUD options
class SinglePhraseAdminView(RetrieveUpdateDestroyAPIView):
    queryset = Phrases.objects.all()
    serializer_class = PhrasesSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


## PICTURES

#Lista todas as pictures
class PicturesView(ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

#Lista apenas uma picture
class SinglePictureView(RetrieveAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

#Lista picture por filosofo
class FilosofoPicturesView(ListAPIView):
    serializer_class = PictureSerializer
    def get_queryset(self):
        filosofo_id = self.kwargs['filosofo_id']
        return Picture.objects.filter(philosopher_id=filosofo_id)

#Lista todas as pictures post + get
class PicturesAdmin(ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

#Retorna uma picture com todos os crud
class SinglePicturesAdmin(RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

# USER
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]