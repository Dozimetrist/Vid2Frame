import cv2
import os

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print(current_working_directory)
  
# Read the video from specified path. Considering py. file is in the same directory as the video.
cam = cv2.VideoCapture("Sample.mp4")
  
try:
      
    # creating a folder named data
    if not os.path.exists('D:\Downloads\Projects\Python\Frames extraction\extracted'):
        os.makedirs('D:\Downloads\Projects\Python\Frames extraction\extracted')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  
# frame
currentframe = 0
  
while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        # if video is still left continue creating images
        # save frame
        name = 'D:\Downloads\Projects\Python\Frames extraction\extracted\pic_' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 60 #at 30 fps, this advances one second. at 60 it advances 2 seconds.
        cam.set(1, currentframe) #each
    else:
        break
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()