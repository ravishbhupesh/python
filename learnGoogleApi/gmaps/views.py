from django.shortcuts import render
from googleapiclient.discovery import build
import pprint, sys


api_key = 'AIzaSyCZj5q3y3t5JSG3HvZrfyMGLa7X0_Pihqk'

booksService = build('books', 'v1', developerKey=api_key)


# Create your views here.
def index(request):
    androidBookRequest = booksService.volumes().list(source='public', q='android')
    response = androidBookRequest.execute()
    pprint.pprint(len(response['items']))
    #pprint.pprint(response)
    books = []
    for book in response['items']:
        bookTitle = book['volumeInfo']['title']
        books.append(bookTitle)
    for b in books:
        print(b)
    return render(request, 'gmaps/index.html', {'books':books})
