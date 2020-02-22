from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic,Entry
from .forms import TopicForm,EntryForm

# Create your views here.
def index(request):
	"""学习笔记的主页"""
	return render(request,'learning_logs/index.html')

def topics(request):
	"""显示所有主题"""	
	topics=Topic.objects.order_by('date_added')
	context={'topics':topics}
	return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
	"""显示单个主题及其下所有条目"""
	topic=Topic.objects.get(id=topic_id)
	entries=topic.entry_set.order_by('-date_added')
	context={'entries':entries,'topic':topic}
	return render(request,'learning_logs/topic.html',context)
	
def new_topic(request):
	"""添加新主题"""	
	if request.method!='POST':
		# 未提交数据的创建一个新表单
		form=TopicForm()
		print("method!='Post'")
	else:
		# Post提交的数据，对数据做处理
		form=TopicForm(request.POST)
		print("form=",form)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
			
	context={'form':form}
	return render(request,'learning_logs/new_topic.html',context)

def new_entry(request,topic_id):
	"""在特定主题中添加新条目"""
	topic=Topic.objects.get(id=topic_id)
	
	if request.method!='POST':
		# 未提交数据时创建一个空表单
		form=EntryForm()
	else:
		# POST提交过来的数据进行处理
		form=EntryForm(data=request.POST)
		if form.is_valid():
			new_enty=form.save(commit=False)
			new_enty.topic=topic
			new_enty.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
	
	context={'topic':topic,'form':form}
	return render(request,'learning_logs/new_entry.html',context)		

def edit_entry(request,entry_id):
	"""修改某个条目"""
	entry=Entry.objects.get(id=entry_id)
	topic=entry.topic
	
	if request.method!='POST':
		# 未提交请求
		form=EntryForm(instance=entry)
	else:
		# POST提交过来数据
		form=EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
			
	context={"topic":topic,"form":form,"entry":entry}
	return render(request,'learning_logs/edit_entry.html',context)
	
	
	
	
	

