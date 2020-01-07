from picamera import PiCamera;
from time import sleep

camera = PiCamera()

#camera upside down so flip
camera.rotation = 180
#camera.exposure_mode = 'nightpreview'

camera.start_preview()
for i in range(20):
    sleep(3)
    camera.capture('/home/pi/Desktop/raspi-cam/dad-test/cat-spy_%s.jpg' % i)
camera.stop_preview()
