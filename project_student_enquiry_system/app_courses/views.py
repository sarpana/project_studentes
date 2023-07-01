from django.shortcuts import render

# Create your views here.
def course_index(request):
    context={"title":"SES|courses","body_title":"here are the details"}
    return render(request,'courses/index.html',context)
    
def course_create(request):
    return render(request,'courses/create.html')
def course_show(request):
    return render(request,'courses/show.html')
def course_edit(request):
    return render(request,'courses/edit.html')