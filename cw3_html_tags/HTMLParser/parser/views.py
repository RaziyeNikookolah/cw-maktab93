from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def result(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    html_tags = request.POST['html_input']
    return HttpResponse(html_tags)
