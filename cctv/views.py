from django.shortcuts import render

def post_list(request):
    return render(request, 'cctv/post_list.html', {})
