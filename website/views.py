from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Diary
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
# Create your views here.


def home(request):
	return render(request,'website/home.html')

@login_required(login_url='login/')
def diary(request):
	current_user = request.user
	context ={
		'diaries':Diary.objects.filter(author=current_user.id)
	}
	return render(request,'website/diary.html', context)



@login_required(login_url='login/')
def ReadDiary(request,diary_id):
	diary=Diary.objects.filter(id=diary_id).first()
	return render(request,'website/read_diary.html',{'diary':diary})


@login_required(login_url='login/')
class WriteDiary(CreateView):
	model=Diary
	fields = ['title','content']
	






