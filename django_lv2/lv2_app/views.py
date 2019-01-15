from django.shortcuts import render
from lv2_app.models import User
from lv2_app.forms import UserForm

# Create your views here.
def index(request):
    my_dir = {'access_user': User.objects.order_by('last_name')}
    return render(request, 'lv2_app/index.html', context=my_dir)

def formpage(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'lv2_app/formpage.html',{'form':form})


