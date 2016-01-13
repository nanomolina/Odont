from django.shortcuts import render_to_response
from django.template import RequestContext

def ejemplo(request):
    return render_to_response(
        'dental_office/ejemplo.html',
        context_instance=RequestContext(request)
    )

def patients(request):
    return render_to_response(
        'dental_office/patients.html',
        context_instance=RequestContext(request)
    )
