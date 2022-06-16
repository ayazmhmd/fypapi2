import numpy as np
import tensorflow as tf
import cv2
from tensorflow.keras.models import load_model
print(cv2.__version__)
def video_capture(vid_path):
    # video_name=os.path.splitext(video_file)[0]
    # vid_path=os.path.join(path1,video_file)
    vid_capture = cv2.VideoCapture(vid_path) 
    if (vid_capture.isOpened() == False):
      print("Error opening the video file")
      return None
    else:
      d=0
      counter=0
      cat_images=[]
    while(vid_capture.isOpened()):
      ret, frame = vid_capture.read()
      if ret == True:
          d=d+1
          if d <16:
            continue
          else:
            counter=counter+1
            d=0
            frame_grey=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            datu=np.array(frame_grey)
            normu_dat=datu/255
            cat_images.append(normu_dat)
            if counter==60:
              break
      else:
        if counter<60:
          while counter<60:
            cat_images.append(normu_dat)
            counter=counter+1
        break
    vid_capture.release()
    return cat_images


def check(images):
    new_model = tf.keras.models.load_model('3dcnn_weight.h5',compile = True)
    test_img=images.reshape((-1, 60, 240, 320, 1))
    x=new_model.predict(test_img)
    b=np.argmax(x)
    print(b)
    return b

