from django.shortcuts import render

def chat(request):
    return render(request, 'chat/create_post.html')
    # return render(request, 'chat/index.html')