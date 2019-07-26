# ！/usr/bin/env python
# -*-coding:utf-8-*-
"""
@Author  : JianweiZheng
@Time    : 2019/07/26 
@Desc : get the CC_Web_video dataset
@Project : python_appliction
@FileName: get-CCWebVideo.py
@Software: python
"""
import sys
import you_get
import pandas as pd
import csv
import os
import subprocess
def download(url, path):
	sub = "you-get -o" + path +" "+ url
	subprocess.run(args=sub, shell=True)
    # sys.argv = ['you-get', '-o', path, url]
    # you_get.main()
 
 
if __name__ == '__main__':

	info_file = "Video_Complete.csv"
	with open(info_file, 'r', encoding="utf-8") as csvfile:
		reader = csv.reader(csvfile)
		TopicIDList = [row[1] for row in reader]
		print(TopicIDList[0])

	with open(info_file, 'r', encoding="utf-8") as csvfile:
		reader = csv.reader(csvfile)
		VideoNameList = [row[3] for row in reader]
		print(VideoNameList[0])

	TopicIDList.remove(TopicIDList[0])
	VideoNameList.remove(VideoNameList[0])

	for i in range(len(TopicIDList)):
		if(i >= 90 ):
			print(i)
			TopicID = TopicIDList[i]
			VideoName = VideoNameList[i]
			url = "http://vireo.cs.cityu.edu.hk/webvideo/videos/"+TopicID+"/"+VideoName
			path = "./Videos"
			download(url, path)

