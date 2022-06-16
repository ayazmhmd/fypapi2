import os
import tensorflow
import numpy as np
from flask import Flask, render_template, request
import prediction
import gc
result =	{
  0: "Explosion",
  1: "Fighting",
  2:  "Burgulary",
}
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST': 
	 Vid = request.files['my_video']

	 vid_path = Vid.filename	
	 Vid.save(vid_path)
	 imges=prediction.video_capture(vid_path)
	 try:
		 os.remove(vid_path)
	 except:
		 pass
	 img=np.asarray(imges)	
	 del(imges)
	 gc.collect()
	 ret=prediction.check(img)	
	 val=result[ret]
	 print(val)
	 return render_template("index.html", Pred = ret,cat=val, vid_name=Vid.filename)
if __name__=='__main__':
    app.run(debug=True,use_reloader=False)
