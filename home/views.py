from django.shortcuts import render
from django.shortcuts import redirect
from .models import post
from django.core.paginator import Paginator
from django.http import Http404


def post_view(rq):
    new_post = post.objects.order_by('-publish_date')
    ara = rq.GET.get('Ara')
    if ara:
        new_post = new_post.filter(title__icontains=ara)
    paginator = Paginator(new_post, 4) # Show 25 contacts per page.
    page_number = rq.GET.get('sayfa')
    page_obj = paginator.get_page(page_number)
    return render(rq, 'home.html', {'posts': page_obj})


def detail_view(rq, pk):
    dpost = post.objects.get(pk=pk)
    return render(rq, 'detail.html', {'post': dpost})

