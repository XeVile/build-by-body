from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
    # Create a list to itterate over HTML
    latest_post_list = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'index.html', context)

def expand(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, '_layouts/expand.html')

