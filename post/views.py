from django.shortcuts import render, get_object_or_404
from .models import Post
# from card.models import Card
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import PostSerializers
# from taggit.models import Tag

# Create your views here.

class PostList(ListAPIView):
    queryset = Post.objects.filter(status='published').all()
    serializer_class = PostSerializers

class PostList_home(ListAPIView):
    queryset = Post.objects.filter(status='published').all()[:3]
    serializer_class = PostSerializers

def PostDetail(RetrieveAPIView, id):
    queryset = get_object_or_404(Post, id=id)
    # queryset = Post.objects.filter(status='published').all()
    serializer_class = PostSerializers





# def Homepage(request):
#     posts = Post.objects.filter(status='published').all()[:3]
#     cards = Card.objects.filter(status='published').all()[:3]
#     return render(request, 'index.html', locals())

# def Aboutpage(request):
#     return render(request, 'about.html', locals())

# def Contactpage(request):
#     return render(request, 'contact.html', locals())

# def post_list(request):
#     posts = Post.objects.filter(status='published').all()
#     return render(request, "news.html", locals())

# def post_detail(request, year, month, day, pk,):
#     post = get_object_or_404(Post, pk=pk)
#     last_posts = Post.objects.filter(status='published').all()[:3]
#     return render(request, "blog-single.html", locals())

# def card_detail(request):
#     cards = Card.objects.filter(status='published').all()
#     return render(request, 'galery.html', locals())


    