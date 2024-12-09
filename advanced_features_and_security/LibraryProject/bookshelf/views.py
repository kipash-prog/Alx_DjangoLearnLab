from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from .models import MyModel
# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import CustomUser

@permission_required('your_app_name.can_view', raise_exception=True)
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'edit_user.html', {'user': user})



@permission_required('app_name.can_edit', raise_exception=True)
def edit_view(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        instance.name = request.POST['name']
        instance.save()
        return redirect('success_url')
    return render(request, 'edit_template.html', {'instance': instance})
@permission_required('app_name.can_delete', raise_exception=True)
def delete_view(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)
    instance.delete()
    return redirect('success_url')
