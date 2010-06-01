from django.db import models


class Simulation(models.Model):
	name = models.CharField(max_length=256)
	description = models.TextField(blank=True)
	particle_number = models.IntegerField(editable=False)
	detuning = models.FloatField(editable=False)
	start_time = models.DateTimeField(null=True, editable=False)
	finish_time = models.DateTimeField(null=True, editable=False)
	enqueued_time = models.DateTimeField(editable=False)

	def __unicode__(self):
		return self.name


class XYData(models.Model):
	simulation = models.ForeignKey(Simulation)
	name = models.CharField(max_length=256)
	xname = models.CharField(max_length=32)
	yname = models.CharField(max_length=32)


class XYValue(models.Model):
	xydata = models.ForeignKey(XYData)
	x = models.FloatField()
	y = models.FloatField()
