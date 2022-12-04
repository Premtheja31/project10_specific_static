from django.shortcuts import render

# Create your views here.
def specific_html(request):
    return render(request,'specific_html.html')