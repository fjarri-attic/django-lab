from django.conf.urls.defaults import *

urlpatterns = patterns('django_lab.views',
	(r'^$', 'index'),
	(r'^simulation/(?P<simulation_id>\d+)/$', 'detail')
)