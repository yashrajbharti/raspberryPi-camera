import picamera
import time

camera = picamera.PiCamera()
camera.vflip = True
# for vertically flipping the image
camera.capture('example.jpg')
# saves captured image as example.jpg
