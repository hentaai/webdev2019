import json
from api.models import TaskList
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from api.serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer, TaskSerializer2
# Create your views here.

@csrf_exempt
def task_lists(request):
	if request.method == 'GET':
		task_lists = TaskList.objects.all()
		serializer = TaskListSerializer2(task_lists, many=True)
		return JsonResponse(serializer.data, safe=False)
	
	elif request.method == 'POST':
		body = json.loads(request.body)
		serializer = TaskListSerializer2(data=body)
		
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		
		return JsonResponse(serializer.errors)

	return JsonResponse({'error': 'bad request'})


@csrf_exempt
def task_list_detail(request, pk):
	try:
		tasklist = TaskList.objects.get(id = pk)
	except TaskList.DoesNotExist as e:
		return JsonResponse({'error': str(e)})

	if request.method == 'GET':
		serializer = TaskListSerializer2(tasklist)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		body = json.loads(request.body)
		serializer = TaskListSerializer2(instance=tasklist, data=body)
		
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		
		return JsonResponse(serializer.errors)
	
	elif request.method == 'DELETE':
		tasklist.delete()
		return JsonResponse({'delete': True})

	return JsonResponse(tasklist.to_json())

@csrf_exempt
def tasks(request, pk):
	try: 
		task_list = TaskList.objects.get(id = pk)
	except TaskList.DoesNotExist as e:
		return JsonResponse({'error': str(e)})


	if request.method == 'GET':
		tasks = task_list.task_set.all()
		serializer = TaskSerializer2(tasks, many=True)
		return JsonResponse(serializer.data, safe = False)

	elif request.method == 'POST':
		body = json.loads(request.body)
		serializer = TaskSerializer2(data=body)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors)

