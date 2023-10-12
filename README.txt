# Author - Mayank Bajaj
# YouTube-Data-Analyser

A Python Based GUI To Analyze and compare Youtube Channel Using MySQL

INTRODUCTION


The Project is designed to access data of almost all channels live on
YouTube in real time, which are presented to you in an interactive
way. Some features of this project are:

1. Credentials of YouTube channels are automatically saved, this
will lead you in saving time when you use it next time.
2. It helps us to calculate and display likes, views, and video count
data in an interactive way of presentation and export all the
data to CSV files easily.
3. Compare any 5 YouTube channels of your choice in terms of
likes, views, and video count, which can be exported to csv
easily.
4. Download any Audio or Video from YouTube easily. 


MODULES USED IN THE PROJECT

1. CSV – To export all the data extracted from YouTube to CSV.
2. Pafy – To Download Videos and Audios from YouTube.
3. Pickle – To read Binary file to access data like graph ratios and
Country codes stored in binary files.
4. Shutil – To move extracted CSV files or downloaded audio/video to
any desired location.
5. Tkinter – To create a Graphical User Interface and Present the project
more interactively.
6. Datetime – To access real-time date for some calculations in the
project.
7. File Dialog – To ask the user for the directory of the desired location of
CSV files or downloaded audio/video.
8. Numerize – To very large values of numbers to a more readable form.
9. Mysql.connector – To connect the project to MySQL and add, remove,
or modify records.
10. PIL – To display images in the GUI and make is look premium branded.
11. Messagebox – To pop up messages in front of user.
12. Matplotlib – To display graphs based on the criteria chosen by user.
13. Urllib -To download temporary data like logo of YouTube channels
from the internet.
14. Google API Client – To fetch data from YouTube.


I have made this project which analyse the data of your favourite
YouTube content creators and present it in an interactive way, also
you can compare the data of multiple creators and helps you to
begin your YouTube content creation journey more efficiently.
Lastly, we can also download any video or audio from youtube by
using this app. This project uses MySQL as its Database
Management System. And all its data is stored in a data base named
‘yda’. The database ‘yda’ initially have only one table named
‘accounts’ which is used to store account information of registered
users and the program further creates a separate table for every
user to give him/her a personalised experience. However the
program has ability to create the database and all the tables on its
own.

When we run the project:

1) It searches MySQL for the database ‘yda’. If found, it proceeds.
If not found it creates one.
2) Secondly, It Searches for a table named ‘accounts’ in the
database ‘yda’. If found, it proceeds. If not found, it creates one.
3) Now a GUI intro Window comes in front saying ‘Welcome to
YouTube Data Analyser’ and a button ‘Get Started =>’ .
4) When you press the button it requires registration and login
(only for the first time or if you haven’t checked the ‘remember
me’ check box)
5) Now the main window opens having 4 Options:
 Single Channel States: to analyse a single channel
 Compare channels: to compare upto 5 channels
 Download Video/Audio: to download an Audio/ Video
from YouTube.
 Sign Out: to sign out of the account. 
