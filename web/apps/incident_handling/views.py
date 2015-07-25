from django.shortcuts import render_to_response
from django.template import RequestContext

def view_incident_handling(request):
    return render_to_response('incident_handling.html',
                                context_instance=RequestContext(request),
                                )
