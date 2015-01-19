import pygame.camera as pycam

# initialize module
pycam.init()

# Get all available cameras
cameras = pycam.list_cameras()
print("Available cameras:")
for c in cameras:
    print(c)

# Use the first one on the list
print("Using camera", cameras[0])
cam = pygame.camera.Camera(cameras[0])
cam.start()

while True:
    img = cam.get_image() # get an image 
    raw = cam.get_raw()   # get raw data