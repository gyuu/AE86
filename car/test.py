from rotate import *
from distance import *
try:
	while True:
		print "Distance:%0.2f m" % checkdist()
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
