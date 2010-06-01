from django.shortcuts import render_to_response, get_object_or_404

from django_lab.models import Simulation

def index(request):
	simulation_list = Simulation.objects.all().order_by('-enqueued_time')
	return render_to_response('django_lab/index.html',
		{'simulation_list': simulation_list})

def detail(request, simulation_id):
	s = get_object_or_404(Simulation, pk=simulation_id)
	return render_to_response('django_lab/detail.html', {'simulation': s})
