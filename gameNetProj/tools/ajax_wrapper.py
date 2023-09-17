from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest

def get_ajax_wrapper(request, url, context):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            return render(request, url, context)
        else:
            return JsonResponse({'req_error': 'invalid request'}, status=400)
        
    else:
        return HttpResponseBadRequest('Invalid request')