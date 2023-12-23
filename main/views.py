from django.shortcuts import render

def create_expert_view(request):
    return render(request, template_name='create_expert.html')

# Create your views here.
