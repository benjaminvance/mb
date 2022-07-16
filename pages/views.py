from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = 'pages/views.html'


class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", 'body']
