import os
import tensorflow
import numpy as np
from flask import Flask, render_template, request
import prediction
result =	{
  0: "Explosion",
  1: "Fighting",
  2:  "Burgulary",
}
app = Flask(__name__)

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
	 img=np.asarray(imges)	
	 ret=prediction.check(img)	
	 val=result[ret]
	 print(val)
	 try:
		 os.remove(vid_path)
	 except:
		 pass
	 return render_template("index.html")
if __name__=='__main__':
    app.run(debug=True)
