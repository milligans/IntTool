from random import randint
import os, os.path

def videoSelector(chosen):
    if not chosen:
        video_choice = "static/videos/openers/1.mp4"
        return video_choice

    list=os.listdir("application/static/videos/" + chosen + "/")
    number_files=len(list)
    if number_files == 0:
        video_choice = "static/videos/openers/1.mp4"
        return video_choice
    file_num=randint(1, number_files)
    # print(number_files, " is the directory length")
    video_choice = "static/videos/" + chosen +"/" +str(file_num) +".mp4"
    # print(video_choice)
    return video_choice

