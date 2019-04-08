from django.shortcuts import render
from api.models import TaskList
from django.http import JsonResponse
# Create your views here.


def task_lists(request):
	task_lists = TaskList.objects.all()
	json_tasks = [l.to_json() for l in task_lists]
	return JsonResponse(json_tasks, safe=False)

def task_list_detail(request, pk):
	try:
		task_list = TaskList.objects.get(id = pk)
	except TaskList.DoesNotExist as e:
		return JsonResponse({'error': str(e)})

	return JsonResponse(task_list.to_json())

def tasks(request, pk):
	try: 
		task_list = TaskList.objects.get(id = pk)
	except TaskList.DoesNotExist as e:
		return JsonResponse({'error': str(e)})

	tasks = task_list.task_set.all()
	json_tasks = [t.to_json() for t in tasks]
	return JsonResponse(json_tasks, safe = False)
