import os
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

from django_lab.models import Simulation
import datetime
import time
import random

ts = time.time()

for i in xrange(10):
	Simulation(
		name="test" + str(i + 1),
		description="desc1",
		particle_number=random.randint(1, 10) * 1000,
		detuning=random.randint(-10, 10),
		enqueued_time=datetime.datetime.fromtimestamp(ts - random.randint(0, 10 ** 5))).save()
