from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest



def get_ajax_wrapper(request, url='', context={}, return_type='html'):
    """
    Return path of page with ajax or json data with ajax.

    url = path to html file. (defauld='')

    context = data for django template engine

    return_type - can be 'html' or 'json'. (default = 'html')
    """
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            if return_type == 'html':
                return render(request, url, context)
            
            elif return_type == 'json':
                return JsonResponse({'context': context})
        else:
            return JsonResponse({'req_error': 'invalid request'}, status=400)
        
    else:
        return HttpResponseBadRequest('Invalid request')