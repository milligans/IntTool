from flask import render_template, url_for, request, redirect, flash, send_file
from application.videoselector import videoSelector
from application import app

@app.route("/", methods=['GET', 'POST'])
def homepage():
    vid_url="static/videos/openers/1.mp4"
    if request.method=="POST":
        category=request.form.get('videos')
        # print(request.form.get('videos'))
        vid_url=videoSelector(category)
    return render_template('index.html', vid_url=vid_url)