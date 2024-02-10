from django.urls import path
from .views import test, FilosofoView, PhrasesView, PicturesView, SingleFilosofoView, FilosofoPhrasesView, SinglePhraseView, FilosofoPicturesView, SinglePictureView, UserList
from .views import FilosofoListAdmin, SingleFilosofoAdmin, PicturesAdmin, PhrasesListAdmin, SinglePhraseAdminView, SinglePicturesAdmin

urlpatterns = [
    path('', test, name='apiTest'),
    path("filosofo/", FilosofoView.as_view(), name="filosofoList"),
    path("filosofo/<int:pk>", SingleFilosofoView.as_view(), name="filosofoList"),
    path("phrases/", PhrasesView.as_view(), name="phrasesList"),
    path("filosofo/<int:filosofo_id>/phrases/", FilosofoPhrasesView.as_view(), name='filosofo-phrases-list'),
    path("filosofo/<int:filosofo_id>/phrases/<int:pk>", SinglePhraseView.as_view(), name='single-phrases'),
    path("pictures/", PicturesView.as_view(), name="picturesList"),
    path("filosofo/<int:filosofo_id>/pictures/", FilosofoPicturesView.as_view(), name="filosofo-pictures-list"),
    path("filosofo/<int:filosofo_id>/pictures/<int:pk>", SinglePictureView.as_view(), name="single-picture"),
    path('users/', UserList.as_view(), name='user-list'),

    ## Admin Endpoints
    path("adm/filosofos", FilosofoListAdmin.as_view(), name="filosofoAdmin"),
    path("adm/filosofos/<int:pk>", SingleFilosofoAdmin.as_view(), name="filosofoRetrieveAdmin"),

    #Phrases
    path("adm/phrases/", PhrasesListAdmin.as_view(), name="phrasesAdmin"),
    path("adm/pictures/", SinglePhraseAdminView.as_view(), name="singlePhraseAdmin"),

    #Pictures
    path("adm/pictures", PicturesAdmin.as_view(), name="picturesAdmin"),
    path("adm/pictures/<int:pk>/", SinglePicturesAdmin.as_view(), name="singlePicturesAdmin")
]