# order_videos
Sort videos by schedule

If you record your classes you can use this python script to sort each video separately into different folders.

This script was made in python 3.7.

1. You have to modify Orar.txt according to the following model:
  **DAY(WEEK_StartHour:EndHour_ClassName-WEEK_StartHour:EndHour_ClassName(**
  You have to change: 
    "DAY" with the day of the week in which the class is held 
    "WEEK" with M/I/P(M-if the class is always held/ I-if the class is held in odd week/ P-if the class is held in even week)
    "StartHour" with the hour the class starts
    "EndHour" with the hour the class ends
    "ClassName" with the name of the file you want to move the class to
2. You have to create directories for each class in the main directory
3. The video files have to be named by the next model:  YYYY-MM-DD hh:mm:ss.mp4 (if you use obs that's the default name)

After you have all the video files and the script in the same directory you have to open the terminal in the directory file. Type in terminal : ```py order_videos.py``` and that's all.

This is an exemple: 
  ![Example Image1](https://i.imgur.com/xzUqhP3.png)
  ![Example Image2](https://i.imgur.com/uRUagEy.png)
