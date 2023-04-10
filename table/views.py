from django.shortcuts import render

from table.models import *

def add_Teacher(request):
    if request.method == 'POST':
        T_id=request.POST.get('T_id') 
        T_name = request.POST.get('T_name')


        Teacher_obj = Teacher(T_id=T_id, T_name=T_name, )
        Teacher_obj.save()
        return render(request, 'success.html')
    else:
        return render(request, 'add_Teacher.html')
def add_Course(request):
    if request.method == 'POST':
        c_id= request.POST.get('c_id') 
        c_name = request.POST.get('c_name')

        T_id= request.POST.get('T_id')
        teacher_instance = Teacher.objects.get(pk=T_id)


        Course_obj= Course(c_id=c_id, c_name=c_name,T_id=teacher_instance )
        Course_obj.save()
        
        return render(request, 'success.html')
    else:
        
        return render(request, 'add_Course.html',)

# Create your views here.
