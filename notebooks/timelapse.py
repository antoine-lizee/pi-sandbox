from picamera import PiCamera
from IPython.display import Image
import os
from fractions import Fraction
from time import sleep
from datetime import datetime



camera = PiCamera(sensor_mode=4, resolution=(1640, 1232))
# camera = PiCamera()


# camera.start_preview()
# camera.stop_preview()


def get_settings_from_cam(camera, settings=None):
    if settings == None:
        settings = dir(camera)
    for attr in settings:
        if attr[0] != '_' and attr not in ('frame', 'led'):
            print('%s: %s' % (attr, getattr(camera, attr)))
            
#get_settings_from_cam(camera)



get_settings_from_cam(camera, ('analog_gain', 'digital_gain', 'exposure_speed', 'iso', 'shutter_speed', 'resolution'))


total_time = 10 * 60  # in minutes
frame_rate = 24  # in fps
speed = 10  # in minutes per seconds

sleep_time = speed * 60 / frame_rate
n_pics = int(total_time * 60 / sleep_time)

os.makedirs('timelapse', exist_ok=True)
for i in range(n_pics):
    sleep(sleep_time)
    print('taking picture %d/%d, at %s' % (i+1, n_pics, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    camera.capture('timelapse/%d.jpg' % i)

os.system('avconv -r %d -i timelapse/%%d.jpg -vcodec libx264 -y timelapse.mp4' % frame_rate)
