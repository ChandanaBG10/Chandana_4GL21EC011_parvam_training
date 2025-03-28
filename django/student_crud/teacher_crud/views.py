
from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm
from django.contrib import messages

# Create your views here.
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_crud/teacher_list.html', {'teachers': teachers})

def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher details added successfully!')
            return redirect('teacher-list')
    else:
        form = TeacherForm()
    return render(request, 'teacher_crud/create_teacher.html', {'form': form})

def view_teacher(request, pk):
    
    teacher  = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teacher_crud/view_teacher.html', {'teacher': teacher})


def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher updated successfully!')
            return redirect('teacher-list')
        else:
            messages.error(request, 'Error updating teacher. Please check the form.')
    else:
        form = teacherForm(instance=teacher)
    
    return render(request, 'teacher_crud/create_teacher', {'form': form, 'update': True, 'teacher': teacher})  

def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        messages.success(request, 'teacher deleted successfully!')
        return redirect('teacher-list')
    return render(request, 'teacher_crud/delete_teacher.html', {'teacher': teacher})



