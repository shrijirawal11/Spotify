from django.urls import path, include
from artist.views import artistListing, artistDetail,artistId,addApiView,editApiView,songApiView,songDetail

urlpatterns = [
    path('',artistListing , name="listing"),
    path('art/',artistDetail, name="art"),
    path('artist/<int:id>/',artistId, name="Dynamic_art"),
    path('addartist/',addApiView, name="add_artist"),
    path('editartist/<int:id>/',editApiView, name="edit_artist"),
    path('songlist/',songApiView, name="song_list"),
    path('songlistid/<int:id>/',songDetail, name="songlist_detail"),

]
