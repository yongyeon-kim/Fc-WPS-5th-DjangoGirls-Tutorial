from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_list(request):
    #return HttpResponse('<html><body>Post list</body></html>')
    return render(request, 'blog/post_list.html')
