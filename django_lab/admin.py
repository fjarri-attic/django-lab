from django_lab.models import Simulation, XYData
from django.contrib import admin

class DataInline(admin.StackedInline):
	model = XYData

class SimulationAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['name', 'description']}),
		('Timings',
			{'fields': ['enqueued_time', 'start_time', 'finish_time'],
			'classes': ['collapse']}),
		('Parameters', {'fields': ['particle_number', 'detuning'], 'classes': ['collapse']}),
	]

	readonly_fields = ('enqueued_time', 'start_time', 'finish_time',
		'particle_number', 'detuning')
	list_display = ('name', 'particle_number', 'detuning')
	list_filter = ('start_time', 'finish_time', 'enqueued_time')
	search_fields = ('name',)
	date_hierarchy = 'start_time'


admin.site.register(Simulation, SimulationAdmin)
