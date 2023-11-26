# Create your views here.
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from artist.models import artist, album
from .serializers import artistSerializer, albumSerializer
# Create your views here.

@api_view(['GET'])
def artistListing(request):
    print("artist.api")
    singers=artist.objects.all()
    art=artistSerializer(singers, many=True)
    return Response(art.data)

@api_view(['GET'])
def artistDetail(request):
    print('artist.api')
    singer=artist.objects.get(id=2)
    art=artistSerializer(singer, many=False)
    return Response (art.data )

@api_view(['GET'])
def artistId(request,id):
    print('artist.api')
    singer= artist.objects.get(id=id)
    art=artistSerializer(singer, many=False)
    return Response (art.data )

@api_view(['POST'])
def addApiView(request):
    serializer = artistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])  # You can also use 'PATCH' if you want to handle partial updates
def editApiView(request, id):
    try:
        art = artist.objects.get(id=id)
    except art.DoesNotExist:
        return Response({'error': 'artist does not exist'}, status=404)
    serializer = artistSerializer(art, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def artistSongs(request):
    songs=artist.objects.all()
    songs=artistSerializer(songs,many=True)
    return Response(songs.data) 
    
@api_view(['GET'])
def songApiView(request):
    print('artist.api')
    songs= album.objects.all()
    song=albumSerializer(songs, many=True)
    return Response (song.data )

@api_view(['GET'])
def songDetail(request,id):
    print('artist.api')
    try:
        songs = album.objects.get(id=id)
    except songs.DoesNotExist:
        return Response({'error': 'artist does not exist'}, status=404)
    song=albumSerializer(songs, many=False)
    return Response (song.data )



