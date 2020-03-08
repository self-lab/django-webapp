from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'whatever',
        'title': 'Blog Post I',
        'content': 'First posted content',
        'date_posted' : 'August 27, 2020'
    },
    {
        'author': 'ksenya',
        'title': 'Blog Post II',
        'content': '2nd posted content',
        'date_posted' : 'August 27, 2016'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
