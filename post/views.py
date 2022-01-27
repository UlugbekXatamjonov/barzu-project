from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import PostSerializer
from .models import Post
# Create your views here.

class ListPost(ListAPIView):
    queryset = Post.objects.order_by('-created').all()
    serializer_class = PostSerializer
    

class DetailPost(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(DetailPost, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Post.objects.order_by('-hit_count_generic__hits'),
        })
        return context
