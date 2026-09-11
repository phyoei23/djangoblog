from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {'title': 'Djangoblog Homepage.'})

def about(request):
    return render(request, 'blog/about.html', {'about': 'Djangoblog team.'})

def content(request):
    return render(request, 'blog/content.html', {'content': 'Djangoblog team.'})