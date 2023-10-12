# Author - Mayank Bajaj

'''
https://commentpicker.com/youtube-channel-id.php
pip install pafy
pip install youtube-dl==2020.12.2
pip install pillow
pip install numerize
pip install matplotlib
pip install mysql-connector-python
pip install google-api-python-client
'''

import csv
import pafy
import pickle
import shutil
from tkinter import *
from datetime import date
import tkinter.filedialog
from numerize import numerize
import mysql.connector as sql
from PIL import ImageTk, Image
from tkinter import messagebox
import matplotlib.pyplot as plt
from urllib.request import urlopen
from googleapiclient.discovery import build

mysqlpass = '2006'


def graphvalue(a):
    with open('graphratio.dat', 'rb') as f:
        g = pickle.load(f)
    return g[len(str(max(a.values())))]


def start():
    def login2():
        def check():
            mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
            d = {}
            mycursor = mydb.cursor()
            mycursor.execute('select * from accounts')
            myrecord = mycursor.fetchall()
            for x in myrecord:
                d[x[0]] = x[1]
            mycursor.close()
            mydb.close()
            if username.get() == '':
                messagebox.showerror('Error', 'Please Enter Username')
            elif username.get() not in d.keys():
                messagebox.showerror('Error', 'Username not found, Please Register First')
            else:
                if password.get() != d[username.get()]:
                    messagebox.showerror('Error', 'Wrong Password')
                else:
                    login2s.destroy()
                    user = username.get()
                    mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                    mycursor = mydb.cursor()
                    mycursor.execute('select username from accounts')
                    myrecord = mycursor.fetchall()
                    for i in myrecord:
                        mycursor.execute('update accounts set rememberme = 0 where username = "' + i[0] + '"')
                        mydb.commit()
                    mycursor.execute('update accounts set rememberme = "' + str(remme.get()) + '" where username = "' + user + '"')
                    mydb.commit()
                    mycursor.close()
                    mydb.close()
                    b1(user)

        def fp():
            def checkdob():
                mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                mycursor = mydb.cursor()
                mycursor.execute("select * from accounts where username='" + username.get() + "'")
                myrecord = mycursor.fetchall()
                e = myrecord[0][3]
                z = str(e)
                if str(dobyear.get()) == '' or str(dobmonth.get()) == '' or str(dobdate.get()) == '' or str(
                        newpassword.get()) == '':
                    messagebox.showerror('Error', 'Please fill all your credentials.')
                elif str(dobyear.get()) != z[:4] or str(dobmonth.get()) != z[5:7] or str(dobdate.get()) != z[8:]:
                    messagebox.showerror('Error', 'Invalid DOB, Please try again.')
                else:
                    mycursor.execute("update accounts set password='" + newpassword.get() + "' where username='" + username.get() + "'")
                    mydb.commit()
                    mycursor.close()
                    mydb.close()
                    messagebox.showinfo('YDA', 'Password Changed!, Please Login Now.')
                    fps.destroy()
                    login2()

            mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
            d = {}
            mycursor = mydb.cursor()
            mycursor.execute('select * from accounts')
            myrecord = mycursor.fetchall()
            for x in myrecord:
                d[x[0]] = x[1]
            mycursor.close()
            mydb.close()
            if username.get() not in d.keys():
                messagebox.showerror('Error', 'Please Enter Username.')
            elif username.get() not in d.keys():
                messagebox.showerror('Error', 'Username not found, Please Register First.')
            else:
                login2s.destroy()
                fps = Tk()
                fps.title('YouTube Data Analyser')
                fps.geometry('510x400')
                fps.resizable(False, False)
                fps.attributes()

                img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
                Label(fps, image=img2).place(x=236, y=349)

                img3 = ImageTk.PhotoImage(Image.open('yda.png'))
                Label(fps, image=img3).place(x=10, y=-30)

                Label(fps, text='DATE OF BIRTH', font=('arial', 15, 'bold')).place(x=180, y=90)
                Label(fps, text='DD  MM  YYYY', font=('arial', 15, 'bold')).place(x=185, y=150)
                Label(fps, text='NEW PASSWORD', font=('arial', 15, 'bold')).place(x=170, y=180)

                dobyear = StringVar()
                dobmonth = StringVar()
                dobdate = StringVar()
                Entry(fps, textvariable=dobyear, font=('arial', 17, 'bold'), width=4).place(x=270, y=120)
                Entry(fps, textvariable=dobmonth, font=('arial', 17, 'bold'), width=2).place(x=230, y=120)
                Entry(fps, textvariable=dobdate, font=('arial', 17, 'bold'), width=2).place(x=190, y=120)

                newpassword = StringVar()
                Entry(fps, textvariable=newpassword, font=('arial', 17, 'bold'), width=27).place(x=75, y=210)

                Button(fps, text='Next =>', font=('Arial', 15, 'bold'), width=29, bd=7, command=checkdob).place(x=70,
                                                                                                                y=290)
                fps.mainloop()

        try:
            login.destroy()
        except:
            pass
        login2s = Tk()
        login2s.title('YouTube Data Analyser')
        login2s.geometry('510x400')
        login2s.resizable(False, False)
        login2s.attributes()

        img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
        Label(login2s, image=img2).place(x=236, y=349)

        img3 = ImageTk.PhotoImage(Image.open('yda.png'))
        Label(login2s, image=img3).place(x=10, y=-30)

        Label(login2s, text='USERNAME', font=('arial', 15, 'bold')).place(x=200, y=90)
        Label(login2s, text='PASSWORD', font=('arial', 15, 'bold')).place(x=200, y=180)

        username = StringVar()
        Entry(login2s, textvariable=username, font=('arial', 17, 'bold'), width=27).place(x=75, y=120)

        password = StringVar()
        Entry(login2s, textvariable=password, font=('arial', 17, 'bold'), width=27).place(x=75, y=210)

        Button(login2s, text='LOGIN =>', font=('Arial', 15, 'bold'), width=29, bd=7, command=check).place(x=70, y=290)
        Button(login2s, text='FORGOT PASSWORD', font=('Arial', 7, 'bold'), width=20, bd=4, command=fp).place(x=298, y=245)
        remme = IntVar()
        Checkbutton(login2s, text = 'Remember Me', variable = remme).place(x=75, y=245)
        login2s.mainloop()

    def ra():
        def na():
            mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
            l = []
            mycursor = mydb.cursor()
            mycursor.execute('select username from accounts')
            myrecord = mycursor.fetchall()
            for x in myrecord:
                l.append(x[0])
            if username.get() in l:
                messagebox.showerror('Error', 'Username already taken')
            elif username.get() == '' or fullname.get() == '' or password.get() == '' or dobyear == '' or dobdate.get() == '' or dobmonth.get() == '' or len(dobyear.get()) != 4 or len(dobdate.get()) != 2 or len(dobmonth.get()) != 2:
                messagebox.showerror('Error', 'Please Enter valid Credentials')
            else:
                mycursor.execute("insert into accounts values('" + username.get() + "','" + password.get() + "','" + fullname.get() + "','" + dobyear.get() + "-" + dobmonth.get() + "-" + dobdate.get() + "', default)")
                mycursor.execute('create table ' + username.get() + '_yda(channelname varchar(500), channelid varchar(500) primary key)')
                mydb.commit()
                mycursor.close()
                mydb.close()
                messagebox.showinfo('YDA', 'USER REGISTERED!, Please Login Now.')
                registeracc.destroy()
                login2()

        login.destroy()
        registeracc = Tk()
        registeracc.title('YouTube Data Analyser')
        registeracc.geometry('510x500')
        registeracc.resizable(False, False)
        registeracc.attributes()

        img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
        Label(registeracc, image=img2).place(x=236, y=449)

        img3 = ImageTk.PhotoImage(Image.open('yda.png'))
        Label(registeracc, image=img3).place(x=10, y=-30)

        Label(registeracc, text='FULL NAME', font=('arial', 15, 'bold')).place(x=200, y=140)
        Label(registeracc, text='DATE OF BIRTH', font=('arial', 15, 'bold')).place(x=180, y=30)
        Label(registeracc, text='DD  MM  YYYY', font=('arial', 15, 'bold')).place(x=185, y=90)
        Label(registeracc, text='USERNAME', font=('arial', 15, 'bold')).place(x=200, y=230)
        Label(registeracc, text='PASSWORD', font=('arial', 15, 'bold')).place(x=200, y=320)

        fullname = StringVar()
        Entry(registeracc, textvariable=fullname, font=('arial', 17, 'bold'), width=27).place(x=75, y=170)
        dobyear = StringVar()
        dobmonth = StringVar()
        dobdate = StringVar()
        Entry(registeracc, textvariable=dobyear, font=('arial', 17, 'bold'), width=4).place(x=270, y=60)
        Entry(registeracc, textvariable=dobmonth, font=('arial', 17, 'bold'), width=2).place(x=230, y=60)
        Entry(registeracc, textvariable=dobdate, font=('arial', 17, 'bold'), width=2).place(x=190, y=60)

        username = StringVar()
        Entry(registeracc, textvariable=username, font=('arial', 17, 'bold'), width=27).place(x=75, y=260)

        password = StringVar()
        Entry(registeracc, textvariable=password, font=('arial', 17, 'bold'), width=27).place(x=75, y=350)

        Button(registeracc, text='LOGIN =>', font=('Arial', 15, 'bold'), width=29, bd=7, command=na).place(x=70, y=400)

        registeracc.mainloop()

    mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
    mycursor = mydb.cursor()
    mycursor.execute('select count(*) from accounts where rememberme = 1')
    myrecord = mycursor.fetchall()
    if int(myrecord[0][0]) == 0:
        mycursor.close()
        mydb.close()
        login = Tk()
        login.title('YouTube Data Analyser')
        login.geometry('510x400')
        login.resizable(False, False)
        login.attributes()

        img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
        Label(login, image=img2).place(x=236, y=349)

        img3 = ImageTk.PhotoImage(Image.open('yda.png'))
        Label(login, image=img3).place(x=10, y=-30)

        Button(login, text='REGISTER ACCOUNT', font=('Arial', 15, 'bold'), width=30, bd=7, command=ra).place(x=70, y=210)
        Button(login, text='LOGIN', font=('Arial', 15, 'bold'), width=30, bd=7, command=login2).place(x=70, y=150)

        login.mainloop()
    else:
        mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
        mycursor = mydb.cursor()
        mycursor.execute('select username from accounts where rememberme = 1')
        myrecord = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        b1(myrecord[0][0])


def start2():
    ydaintro.destroy()
    start()
def ysc(cid):
    def b12():
        a = str(response['items'][0]['snippet']['title']) + '.csv'
        with open(a, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['CHANNEL NAME', str(response['items'][0]['snippet']['title'])])
            writer.writerow(['CHANNEL DATE', str(response['items'][0]['snippet']['publishedAt'])[8:10] + '-' + str(response['items'][0]['snippet']['publishedAt'])[5:7] + '-' + str(response['items'][0]['snippet']['publishedAt'])[0:4]])
            writer.writerow(['COUNTRY OF ORIGIN', list(countrycodes.keys())[list(countrycodes.values()).index(response['items'][0]['snippet']['country'])]])
            writer.writerow(['SUBSCRIBER COUNT', response['items'][0]['statistics']['subscriberCount'], numerize.numerize(int(response['items'][0]['statistics']['subscriberCount']))])
            writer.writerow(['TOTAL VIEWS', response['items'][0]['statistics']['viewCount'], numerize.numerize(int(response['items'][0]['statistics']['viewCount']))])
            writer.writerow(['TOTAL LIKES', str(s), numerize.numerize(s)])
            writer.writerow(['VIDEO COUNT', response['items'][0]['statistics']['videoCount']])
        fdr = tkinter.filedialog.askdirectory()
        q = ''
        for x in fdr:
            if x == '/':
                q += '/'
                q += x
            else:
                q += x
        q += '/' + a
        shutil.move(a, q)

    def b8():
        def b13():
            a = str(response['items'][0]['snippet']['title']) + "'s likes per year.csv"
            with open(a, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['CHANNEL NAME', response['items'][0]['snippet']['title']])
                writer.writerow(['YEAR', 'NUMBER OF LIKES'])
                for key in lpy:
                    writer.writerow([key, lpy[key]])
            fdr = tkinter.filedialog.askdirectory()
            q = ''
            for x in fdr:
                if x == '/':
                    q += '/'
                    q += x
                else:
                    q += x
            q += '/' + a
            shutil.move(a, q)

        def b14():
            a = str(response['items'][0]['snippet']['title']) + "'s views per year.csv"
            with open(a, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['CHANNEL NAME', response['items'][0]['snippet']['title']])
                writer.writerow(['YEAR', 'NUMBER OF VIEWS'])
                for key in viewspy:
                    writer.writerow([key, viewspy[key]])
            fdr = tkinter.filedialog.askdirectory()
            q = ''
            for x in fdr:
                if x == '/':
                    q += '/'
                    q += x
                else:
                    q += x
            q += '/' + a
            shutil.move(a, q)

        def b15():
            a = str(response['items'][0]['snippet']['title']) + "'s videos per year.csv"
            with open(a, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['CHANNEL NAME', response['items'][0]['snippet']['title']])
                writer.writerow(['YEAR', 'NUMBER OF VIDEOS'])
                for key in vpy:
                    writer.writerow([key, vpy[key]])
            fdr = tkinter.filedialog.askdirectory()
            q = ''
            for x in fdr:
                if x == '/':
                    q += '/'
                    q += x
                else:
                    q += x
            q += '/' + a
            shutil.move(a, q)

        def b16():
            graph.destroy()

        def b9():
            x = lpy.keys()
            y = lpy.values()
            plt.bar(x, y, label=lpy.keys(),
                    color=['red', 'pink', 'blue', 'yellow', 'violet', 'black', 'orange', 'purple', 'green', 'brown', 'gray'])
            plt.xlabel('Years')
            plt.ylabel('Number of Likes ' + graphvalue(lpy))
            plt.legend()
            plt.show()

        def b10():
            x = viewspy.keys()
            y = viewspy.values()
            plt.bar(x, y, label=viewspy.keys(),
                    color=['red', 'pink', 'blue', 'yellow', 'violet', 'black', 'orange', 'purple', 'green', 'brown', 'gray'])
            plt.xlabel('Years')
            plt.ylabel('Number of Views ' + graphvalue(viewspy))
            plt.legend()
            plt.show()

        def b11():
            x = vpy.keys()
            y = vpy.values()
            plt.bar(x, y, label=vpy.keys(),
                    color=['red', 'pink', 'blue', 'yellow', 'violet', 'black', 'orange', 'purple', 'green', 'brown', 'gray'])
            plt.xlabel('Years')
            plt.ylabel('Number of Videos')
            plt.legend()
            plt.show()

        global response
        yscs.destroy()
        graph = Tk()
        graph.title('YouTube Data Analyser')
        graph.geometry('510x400')
        graph.resizable(False, False)
        graph.attributes()

        img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
        Label(graph, image=img2).place(x=236, y=349)

        img3 = ImageTk.PhotoImage(Image.open('yda.png'))
        Label(graph, image=img3).place(x=10, y=-30)

        img4 = ImageTk.PhotoImage(Image.open('frame.png'))
        Label(graph, image=img4).place(x=214, y=14)

        img5 = ImageTk.PhotoImage(data=rawdata)
        Label(graph, image=img5).place(x=220, y=20)

        img6 = ImageTk.PhotoImage(Image.open('arrow.png'))
        Label(graph, image=img6).place(x=180, y=147)
        Label(graph, image=img6).place(x=180, y=227)
        Label(graph, image=img6).place(x=180, y=307)

        Button(graph, text='LIKES / YEAR', font=('Arial', 10, 'bold'), width=12, bd=4, command=b9).place(x=90, y=150)
        Button(graph, text='VIEWS / YEAR', font=('Arial', 10, 'bold'), width=12, bd=4, command=b10).place(x=90, y=230)
        Button(graph, text='VIDEOS / YEAR', font=('Arial', 10, 'bold'), width=12, bd=4, command=b11).place(x=90, y=310)
        Button(graph, text='EXPORT TO CSV', font=('Arial', 10, 'bold'), width=15, bd=4, command=b13).place(x=280, y=150)
        Button(graph, text='EXPORT TO CSV', font=('Arial', 10, 'bold'), width=15, bd=4, command=b14).place(x=280, y=230)
        Button(graph, text='EXPORT TO CSV', font=('Arial', 10, 'bold'), width=15, bd=4, command=b15).place(x=280, y=310)
        Button(graph, text='QUIT', font=('Arial', 10, 'bold'), width=15, bd=4, command=b16).place(x=20, y=360)

        graph.mainloop()

    yscs = Tk()
    yscs.title('YouTube Data Analyser')
    yscs.geometry('510x400')
    yscs.resizable(False, False)
    yscs.attributes()

    img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
    Label(yscs, image=img2).place(x=236, y=349)

    img3 = ImageTk.PhotoImage(Image.open('yda.png'))
    Label(yscs, image=img3).place(x=10, y=-30)

    img4 = ImageTk.PhotoImage(Image.open('frame.png'))
    Label(yscs, image=img4).place(x=214, y=14)
    youtube = build('youtube', 'v3', developerKey='AIzaSyBghHd_FTCdfCf51FJxXf8d1kaQCDUKr4U')
    request = youtube.channels().list(part='snippet, contentDetails, statistics', id=cid)
    response = request.execute()

    u = urlopen(response['items'][0]['snippet']['thumbnails']['default']['url'])
    rawdata = u.read()
    u.close()

    img5 = ImageTk.PhotoImage(data=rawdata)
    Label(yscs, image=img5).place(x=220, y=20)

    with open('countrycodes.dat', 'rb') as f:
        countrycodes = pickle.load(f)

    syear = int(str(response['items'][0]['snippet']['publishedAt'])[0:4])
    pyear = int(str(date.today().year))
    vpy = {}
    viewspy = {}
    lpy = {}
    for i in range(syear, pyear + 1):
        vpy[i] = 0
        viewspy[i] = 0
        lpy[i] = 0
    uid = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    youtube = build('youtube', 'v3', developerKey='AIzaSyBghHd_FTCdfCf51FJxXf8d1kaQCDUKr4U')
    vrequest = youtube.playlistItems().list(part='contentDetails', playlistId=uid, maxResults=50)
    vresponse = vrequest.execute()
    vids = []
    for i in range(len(vresponse['items'])):
        vids.append(vresponse['items'][i]['contentDetails']['videoId'])
    npt = vresponse.get('nextPageToken')
    mp = True
    while mp:
        if npt is None:
            mp = False
        else:
            vrequest = youtube.playlistItems().list(part='contentDetails', playlistId=uid, maxResults=50, pageToken=npt)
            vresponse = vrequest.execute()
            for i in range(len(vresponse['items'])):
                vids.append(vresponse['items'][i]['contentDetails']['videoId'])
            npt = vresponse.get('nextPageToken')
    for i in range(0, len(vids), 50):
        vrequest = youtube.videos().list(part='snippet, statistics', id=','.join(vids[i:i + 50]))
        vresponse = vrequest.execute()
        for video in vresponse['items']:
            vpy[int(str(video['snippet']['publishedAt'])[0:4])] += 1
            viewspy[int(str(video['snippet']['publishedAt'])[0:4])] += int(video['statistics']['viewCount'])
            try:
                lpy[int(str(video['snippet']['publishedAt'])[0:4])] += int(video['statistics']['likeCount'])
            except:
                pass
    global s
    try:
        s = 0
        for i in lpy:
            s += int(lpy[i])
    except:
        pass
    Label(yscs, text='Channel Name : ' + response['items'][0]['snippet']['title'], font=('arial', 13, 'bold')).place(x=20, y=130)
    Label(yscs, text='Channel Date : ' + str(response['items'][0]['snippet']['publishedAt'])[8:10] + '-' + str(response['items'][0]['snippet']['publishedAt'])[5:7] + '-' + str(response['items'][0]['snippet']['publishedAt'])[0:4], font=('arial', 13, 'bold')).place(x=20, y=170)
    Label(yscs, text='Country of origin : ' + list(countrycodes.keys())[list(countrycodes.values()).index(response['items'][0]['snippet']['country'])],font=('arial', 13, 'bold')).place(x=20, y=210)
    Label(yscs, text='Subscriber Count : ' + response['items'][0]['statistics']['subscriberCount'] + ' ≅ ' + numerize.numerize(int(response['items'][0]['statistics']['subscriberCount'])),font=('arial', 13, 'bold')).place(x=20, y=250)
    Label(yscs, text='Total Views : ' + response['items'][0]['statistics']['viewCount'] + ' ≅ ' + numerize.numerize(int(response['items'][0]['statistics']['viewCount'])), font=('arial', 13, 'bold')).place(x=20, y=290)
    try:
        Label(yscs, text='Total Likes : ' + str(s) + ' ≅ ' + numerize.numerize(s), font=('arial', 13, 'bold')).place(
            x=20, y=330)
    except:
        pass
    Label(yscs, text='Video Count : ' + response['items'][0]['statistics']['videoCount'],font=('arial', 13, 'bold')).place(x=20, y=370)
    Button(yscs, text='SEE GRAPHICALLY', font=('Arial', 10, 'bold'), width=20, bd=7, command=b8).place(x=325, y=200)
    Button(yscs, text='EXPORT THIS DATA TO CSV', font=('Arial', 10, 'bold'), width=25, bd=7, command=b12).place(x=280, y=158)
    yscs.mainloop()


def b1(user):
    def start1():
        mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
        mycursor = mydb.cursor()
        mycursor.execute('select username from accounts')
        myrecord = mycursor.fetchall()
        for i in myrecord:
            mycursor.execute('update accounts set rememberme = 0 where username = "' + i[0] + '"')
            mydb.commit()
        mycursor.close()
        mydb.close()
        option.destroy()
        start()
    def b4():
        option.destroy()
        def b28():
            if urltext.get() == '':
                messagebox.showerror('Error', 'Please Enter a URL')
            else:
                Label(ytcd, text='Downloading..', font=('arial', 13, 'bold')).place(x=20, y=320)
                url = urltext.get()
                vdo = pafy.new(url)
                if av.get() == 0:
                    vbest = vdo.getbest(preftype='mp4')
                    vbest.download(filepath=fgr.get())
                elif av.get() == 1:
                    abest = vdo.getbestaudio(preftype='m4a')
                    abest.download(filepath=fgr.get())
                Label(ytcd, image=img4).place(x=130, y=320)
                Label(ytcd, text='Downloaded', font=('arial', 15, 'bold')).place(x=21, y=320)
                fdr = tkinter.filedialog.askdirectory()
                q = ''
                for x in fdr:
                    if x == '/':
                        q += '/'
                        q += x
                    else:
                        q += x
                q += '/' + vdo.title
                try:
                    shutil.move(vdo.title + '.mp4', q + '.mp4')
                except:
                    pass
                try:
                    shutil.move(vdo.title + '.mp4', q + '.mp4')
                except:
                    pass
        def b27():
            if urltext.get() == '':
                messagebox.showerror('Error', 'Please Enter a URL')
            else:
                url = urltext.get()
                vdo = pafy.new(url)
                streams = vdo.allstreams
                title = vdo.title
                Label(ytcd, text=title, font=('arial', 13, 'bold')).place(x=120, y=250)
                Label(ytcd, text=vdo.duration, font=('arial', 13, 'bold')).place(x=180, y=281)
                if av.get() == 0:
                    vbest = vdo.getbest(preftype='mp4')
                    v = round(vbest.get_filesize() * 0.000001, 2)
                    Label(ytcd, text=str(v) + ' MB', font=('arial', 13, 'bold')).place(x=115, y=220)
                elif av.get() == 1:
                    abest = vdo.getbestaudio(preftype='m4a')
                    a = round(abest.get_filesize() * 0.000001)
                    Label(ytcd, text=str(a) + ' MB', font=('arial', 13, 'bold')).place(x=115, y=220)

            Label(ytcd, text='Total Size : ', font=('arial', 13, 'bold')).place(x=20, y=220)
            Label(ytcd, text='Video Title : ', font=('arial', 13, 'bold')).place(x=20, y=250)
            Label(ytcd, text='Content Duration : ', font=('arial', 13, 'bold')).place(x=20, y=280)

        ytcd = Tk()
        ytcd.title('YouTube Content Downloader')
        ytcd.geometry('510x400')
        ytcd.resizable(False, False)
        ytcd.attributes()

        img = ImageTk.PhotoImage(Image.open(r'YCD IMG.png'))
        Label(ytcd, image=img).place(width=200, height=100)

        img3 = ImageTk.PhotoImage(Image.open(r'Made by Mayank Bajaj.png'))
        Label(ytcd, image=img3).place(x=236, y=349)

        img4 = ImageTk.PhotoImage(Image.open(r'Tick Logo.png'))

        fgr = StringVar()
        urltext = StringVar()
        Label(ytcd, text='Enter the URL of the Video here:', font=('arial', 17, 'bold')).place(x=20, y=100)
        Entry(ytcd, textvariable=urltext, font=('arial', 17, 'bold'), width=27).place(x=20, y=150)

        Button(ytcd, text='Get Data', font=('Arial', 10, 'bold'), width=12, bd=4, command=b27).place(x=380, y=148)
        Button(ytcd, text='Start Downloading', font=('Arial', 10, 'bold'), width=15, bd=4, command=b28).place(x=360, y=300)

        av = IntVar()
        Radiobutton(ytcd, text='Video', value=0, variable=av).place(x=20, y=190)
        Radiobutton(ytcd, text='Audio', value=1, variable=av).place(x=100, y=190)

        ytcd.mainloop()

    def b3():
        def remove():
            register.destroy()

            def b30():
                mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                mycursor = mydb.cursor()
                mycursor.execute('DELETE FROM ' + user + '_yda WHERE channelname="' + menu.get() + '"')
                mydb.commit()
                mycursor.close()
                mydb.close()

            def b31():
                mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                mycursor = mydb.cursor()
                mycursor.execute('truncate ' + user + '_yda')
                mydb.commit()
                mycursor.close()
                mydb.close()

            def b32():
                remove.destroy()

            mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
            mycursor = mydb.cursor()
            mycursor.execute('select count(*) from ' + user + '_yda')
            myrecord = mycursor.fetchall()
            mycursor.close()
            mydb.close()
            if int(myrecord[0][0]) == 0:
                messagebox.showerror('Error', "You don't have any saved channels yet.")
            else:
                remove = Tk()
                remove.title('YouTube Data Analyser')
                remove.geometry('510x400')
                remove.resizable(False, False)
                remove.attributes()
    
                img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
                Label(remove, image=img2).place(x=236, y=349)

                img3 = ImageTk.PhotoImage(Image.open('yda.png'))
                Label(remove, image=img3).place(x=10, y=-30)

                menu = StringVar()
                menu.set('Select channel to be removed')
                mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                mycursor = mydb.cursor()
                a = []
                mycursor.execute('select channelname from ' + user + '_yda')
                myrecord = mycursor.fetchall()
                for x in myrecord:
                    a.append(str(x)[2:-3])
                mydb.commit()
                mycursor.close()
                mydb.close()
                e = 'drop = OptionMenu(remove, menu'
                for b in a:
                    e += ', "' + b + '"'
                e += ').place(x=20, y=100)'
                exec(e)
                Button(remove, text='REMOVE', font=('Arial', 10, 'bold'), width=12, bd=4, command=b30).place(x=380, y=98)
                Button(remove, text='REMOVE ALL CHANNELS', font=('Arial', 10, 'bold'), width=20, bd=4, command=b31).place(x=320, y=158)
                Button(remove, text='QUIT', font=('Arial', 10, 'bold'), width=12, bd=4, command=b32).place(x=380, y=298)
                remove.mainloop()

        def b17():
            global response
            if registeredcreds.get() == '':
                messagebox.showerror('Error', 'Please Enter your channel creds')
            else:
                youtube = build('youtube', 'v3', developerKey='AIzaSyBghHd_FTCdfCf51FJxXf8d1kaQCDUKr4U')
                try:
                    request = youtube.channels().list(part='snippet, contentDetails, statistics',id=registeredcreds.get())
                    response = request.execute()
                except Exception:
                    messagebox.showerror('Error', 'Please connect to the internet')
                if len(response) < 4:
                    messagebox.showerror('Error', 'Please enter valid channel creds')
                else:
                    mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                    mycursor = mydb.cursor()
                    a = []
                    mycursor.execute('select channelid from ' + user + '_yda')
                    myrecord = mycursor.fetchall()
                    for x in myrecord:
                        a.append(str(x)[2:-3])
                    if registeredcreds.get() not in a:
                        mycursor.execute('insert into ' + user + '_yda values("' + response['items'][0]['snippet']['title'] + '","' + registeredcreds.get() + '")')
                        mydb.commit()
                        mycursor.close()
                        mydb.close()

        def b18():
            def b19():
                def b20():
                    subs = {}
                    for a in all_data:
                        subs[a['Channel_name']] = int(a['Subscribers'])
                    x = subs.keys()
                    y = subs.values()
                    plt.bar(x, y, label=subs.keys(), color=['red', 'pink', 'blue', 'yellow', 'violet', 'black', 'orange', 'purple', 'green', 'brown', 'gray'])
                    plt.xlabel('Channels')
                    plt.ylabel('Subscribers ' + graphvalue(subs))
                    plt.legend()
                    plt.show()

                def b21():
                    views = {}
                    for a in all_data:
                        views[a['Channel_name']] = int(a['Views'])
                    x = views.keys()
                    y = views.values()
                    plt.bar(x, y, label=views.keys(), color=['red', 'pink', 'blue', 'yellow', 'violet', 'black', 'orange', 'purple', 'green', 'brown', 'gray'])
                    plt.xlabel('Channels')
                    plt.ylabel('Total Views ' + graphvalue(views))
                    plt.legend()
                    plt.show()

                def b22():
                    videos = {}
                    for a in all_data:
                        videos[a['Channel_name']] = int(a['Total_videos'])
                    x = videos.keys()
                    y = videos.values()
                    plt.bar(x, y, label=videos.keys(), color=['red', 'pink', 'blue', 'yellow', 'violet', 'black', 'orange', 'purple', 'green', 'brown', 'gray'])
                    plt.xlabel('Channels')
                    plt.ylabel('Total Videos ' + graphvalue(videos))
                    plt.legend()
                    plt.show()

                def b23():
                    subs = {}
                    for b in all_data:
                        subs[b['Channel_name']] = int(b['Subscribers'])
                    a = ' vs '.join(subs.keys()) + 'Subscribers.csv'
                    with open(a, 'w') as f:
                        writer = csv.writer(f)
                        writer.writerow(['Channel Name', 'Subscribers'])
                        for c in subs:
                            writer.writerow([c, subs[c]])
                    fdr = tkinter.filedialog.askdirectory()
                    q = ''
                    for x in fdr:
                        if x == '/':
                            q += '/'
                            q += x
                        else:
                            q += x
                    q += '/' + a
                    shutil.move(a, q)

                def b24():
                    views = {}
                    for b in all_data:
                        views[b['Channel_name']] = int(b['Views'])
                    a = ' vs '.join(views.keys()) + 'Views.csv'
                    with open(a, 'w') as f:
                        writer = csv.writer(f)
                        writer.writerow(['Channel Name', 'Total Views'])
                        for c in views:
                            writer.writerow([c, views[c]])
                    fdr = tkinter.filedialog.askdirectory()
                    q = ''
                    for x in fdr:
                        if x == '/':
                            q += '/'
                            q += x
                        else:
                            q += x
                    q += '/' + a
                    shutil.move(a, q)

                def b25():
                    videos = {}
                    for b in all_data:
                        videos[b['Channel_name']] = int(b['Total_videos'])
                    a = ' vs '.join(videos.keys()) + 'Total Videos.csv'
                    with open(a, 'w') as f:
                        writer = csv.writer(f)
                        writer.writerow(['Channel Name', 'Total Videos'])
                        for c in videos:
                            writer.writerow([c, videos[c]])
                    fdr = tkinter.filedialog.askdirectory()
                    q = ''
                    for x in fdr:
                        if x == '/':
                            q += '/'
                            q += x
                        else:
                            q += x
                    q += '/' + a
                    shutil.move(a, q)

                def b26():
                    comparisiontable.destroy()

                ctbc = [menu1.get(), menu2.get(), menu3.get(), menu4.get(), menu5.get()]
                if 'Select Third Channel or leave empty' in ctbc:
                    ctbc.remove('Select Third Channel or leave empty')
                if 'Select Forth Channel or leave empty' in ctbc:
                    ctbc.remove('Select Forth Channel or leave empty')
                if 'Select fifth channel or leave empty' in ctbc:
                    ctbc.remove('Select fifth channel or leave empty')
                if ctbc[0] == 'Select First Channel' or ctbc[1] == 'Select Second Channel':
                    messagebox.showerror('Error', 'Please select at least 2 channels')
                else:
                    comparecreds.destroy()
                    comparisiontable = Tk()
                    comparisiontable.title('YouTube Data Analyser')
                    comparisiontable.geometry('510x400')
                    comparisiontable.resizable(False, False)
                    comparisiontable.attributes()

                    img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
                    Label(comparisiontable, image=img2).place(x=236, y=349)

                    img3 = ImageTk.PhotoImage(Image.open('yda.png'))
                    Label(comparisiontable, image=img3).place(x=10, y=-30)

                    mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                    mycursor = mydb.cursor()
                    ids = []
                    for i in ctbc:
                        mycursor.execute('select channelid from ' + user + '_yda where channelname="' + i + '"')
                        myrecord = mycursor.fetchall()
                        for x in myrecord:
                            ids.append(str(x)[2:-3])
                    mydb.commit()
                    mycursor.close()
                    mydb.close()

                    all_data = []
                    youtube = build('youtube', 'v3', developerKey='AIzaSyBghHd_FTCdfCf51FJxXf8d1kaQCDUKr4U')
                    request = youtube.channels().list(part='snippet, contentDetails, statistics', id=','.join(ids))
                    response = request.execute()

                    for i in range(len(response['items'])):
                        data = dict(Channel_name=response['items'][i]['snippet']['title'],
                                    Subscribers=response['items'][i]['statistics']['subscriberCount'],
                                    Views=response['items'][i]['statistics']['viewCount'],
                                    Total_videos=response['items'][i]['statistics']['videoCount'])
                        all_data.append(data)

                    img6 = ImageTk.PhotoImage(Image.open('arrow.png'))
                    Label(comparisiontable, image=img6).place(x=200, y=127)
                    Label(comparisiontable, image=img6).place(x=200, y=207)
                    Label(comparisiontable, image=img6).place(x=200, y=287)

                    Button(comparisiontable, text='Subscribers', font=('Arial', 10, 'bold'), width=12, bd=4, command=b20).place(x=110, y=130)
                    Button(comparisiontable, text='Total Views', font=('Arial', 10, 'bold'), width=12, bd=4, command=b21).place(x=110, y=210)
                    Button(comparisiontable, text='Total Videos', font=('Arial', 10, 'bold'), width=12, bd=4, command=b22).place(x=110, y=290)
                    Button(comparisiontable, text='EXPORT TO CSV', font=('Arial', 10, 'bold'), width=15, bd=4, command=b23).place(x=300, y=130)
                    Button(comparisiontable, text='EXPORT TO CSV', font=('Arial', 10, 'bold'), width=15, bd=4, command=b24).place(x=300, y=210)
                    Button(comparisiontable, text='EXPORT TO CSV', font=('Arial', 10, 'bold'), width=15, bd=4, command=b25).place(x=300, y=290)
                    Button(comparisiontable, text='QUIT', font=('Arial', 10, 'bold'), width=15, bd=4, command=b26).place(x=20, y=360)
                    comparisiontable.mainloop()

            mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
            mycursor = mydb.cursor()
            mycursor.execute('select count(*) from ' + user + '_yda')
            myrecord = mycursor.fetchall()
            mycursor.close()
            mydb.close()
            if int(myrecord[0][0]) == 0:
                messagebox.showerror('Error', "You don't have any saved channels yet.")
            if int(myrecord[0][0]) == 0:
                messagebox.showerror('Error', "You need atleast 2 channels to proceed.")
            else:
                register.destroy()
                comparecreds = Tk()
                comparecreds.title('YouTube Data Analyser')
                comparecreds.geometry('510x400')
                comparecreds.resizable(False, False)
                comparecreds.attributes()

                img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
                Label(comparecreds, image=img2).place(x=236, y=349)

                img3 = ImageTk.PhotoImage(Image.open('yda.png'))
                Label(comparecreds, image=img3).place(x=10, y=-30)

                menu1 = StringVar()
                menu1.set('Select First Channel')

                menu2 = StringVar()
                menu2.set('Select Second Channel')

                menu3 = StringVar()
                menu3.set('Select Third Channel or leave empty')

                menu4 = StringVar()
                menu4.set('Select Forth Channel or leave empty')

                menu5 = StringVar()
                menu5.set('Select fifth channel or leave empty')

                mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                mycursor = mydb.cursor()
                a = []
                mycursor.execute('select channelname from ' + user + '_yda')
                myrecord = mycursor.fetchall()
                for x in myrecord:
                    a.append(str(x)[2:-3])
                mydb.commit()
                mycursor.close()
                mydb.close()
                e = 'drop1 = OptionMenu(comparecreds, menu1'
                for b in a:
                    e += ', "' + b + '"'
                e += ').place(x=20, y=100)'
                h = 'drop2 = OptionMenu(comparecreds, menu2'
                for b in a:
                    h += ', "' + b + '"'
                h += ').place(x=20, y=150)'
                g = 'drop3 = OptionMenu(comparecreds, menu3'
                for b in a:
                    g += ', "' + b + '"'
                g += ').place(x=20, y=200)'
                i = 'drop4 = OptionMenu(comparecreds, menu4'
                for b in a:
                    i += ', "' + b + '"'
                i += ').place(x=20, y=250)'
                j = 'drop5 = OptionMenu(comparecreds, menu5'
                for b in a:
                    j += ', "' + b + '"'
                j += ').place(x=20, y=300)'
                exec(e)
                exec(g)
                exec(h)
                exec(i)
                exec(j)
                Button(comparecreds, text='NEXT =>', font=('Arial', 10, 'bold'), width=20, bd=7, command=b19).place(x=20, y=360)

                comparecreds.mainloop()

        option.destroy()
        register = Tk()
        register.title('YouTube Data Analyser')
        register.geometry('510x400')
        register.resizable(False, False)
        register.attributes()

        img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
        Label(register, image=img2).place(x=236, y=349)

        img3 = ImageTk.PhotoImage(Image.open('yda.png'))
        Label(register, image=img3).place(x=10, y=-30)

        registeredcreds = StringVar()
        Label(register, text='Enter Channel ID here:', font=('Arial', 17, 'bold')).place(x=20, y=100)
        Entry(register, textvariable=registeredcreds, font=('arial', 17, 'bold'), width=27).place(x=20, y=150)
        Button(register, text='REGISTER', font=('Arial', 10, 'bold'), width=12, bd=4, command=b17).place(x=380, y=148)
        Button(register, text='NEXT =>', font=('Arial', 10, 'bold'), width=30, bd=7, command=b18).place(x=120, y=200)
        Button(register, text='REMOVE SAVED CHANNELS', font=('Arial', 10, 'bold'), width=30, bd=7, command=remove).place(x=120, y=250)
        register.mainloop()

    def b2():
        def remove():
            def b30():
                mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                mycursor = mydb.cursor()
                mycursor.execute('DELETE FROM ' + user + '_yda WHERE channelname="' + menu.get() + '"')
                mydb.commit()
                mycursor.close()
                mydb.close()

            def b31():
                mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                mycursor = mydb.cursor()
                mycursor.execute('DELETE FROM ' + user + '_yda')
                mydb.commit()
                mycursor.close()
                mydb.close()

            def b32():
                remove.destroy()

            mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
            mycursor = mydb.cursor()
            mycursor.execute('select count(*) from ' + user + '_yda')
            myrecord = mycursor.fetchall()
            mycursor.close()
            mydb.close()
            if int(myrecord[0][0]) == 0:
                messagebox.showerror('Error', "You don't have any saved channels yet.")
            else:
                creds.destroy()
                remove = Tk()
                remove.title('YouTube Data Analyser')
                remove.geometry('510x400')
                remove.resizable(False, False)
                remove.attributes()

                img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
                Label(remove, image=img2).place(x=236, y=349)

                img3 = ImageTk.PhotoImage(Image.open('yda.png'))
                Label(remove, image=img3).place(x=10, y=-30)
    
                menu = StringVar()
                menu.set('Select channel to be removed')
                mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                mycursor = mydb.cursor()
                a = []
                mycursor.execute('select channelname from ' + user + '_yda')
                myrecord = mycursor.fetchall()
                for x in myrecord:
                    a.append(str(x)[2:-3])
                mydb.commit()
                mycursor.close()
                mydb.close()
                e = 'drop = OptionMenu(remove, menu'
                for b in a:
                    e += ', "' + b + '"'
                e += ').place(x=20, y=100)'
                exec(e)
                Button(remove, text='REMOVE', font=('Arial', 10, 'bold'), width=12, bd=4, command=b30).place(x=380, y=98)
                Button(remove, text='REMOVE ALL CHANNELS', font=('Arial', 10, 'bold'), width=12, bd=4, command=b31).place(x=380, y=158)
                Button(remove, text='QUIT', font=('Arial', 10, 'bold'), width=12, bd=4, command=b32).place(x=380, y=298)
                remove.mainloop()

        def b5():
            global response
            if channelcreds.get() == '':
                messagebox.showerror('Error', 'Please Enter your channel creds')
            else:
                youtube = build('youtube', 'v3', developerKey='AIzaSyBghHd_FTCdfCf51FJxXf8d1kaQCDUKr4U')
                try:
                    request = youtube.channels().list(part='snippet, contentDetails, statistics', id=channelcreds.get())
                    response = request.execute()
                except Exception:
                    messagebox.showerror('Error', 'Please connect to the internet')

                if len(response) < 4:
                    messagebox.showerror('Error', 'Please enter valid channel creds')
                else:
                    mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                    mycursor = mydb.cursor()
                    a = []
                    mycursor.execute('select channelid from ' + user + '_yda')
                    myrecord = mycursor.fetchall()
                    for x in myrecord:
                        a.append(str(x)[2:-3])
                    if channelcreds.get() not in a:
                        mycursor.execute('insert into ' + user + '_yda values("' + response['items'][0]['snippet'][
                            'title'] + '","' + channelcreds.get() + '")')
                        mydb.commit()
                        mycursor.close()
                        mydb.close()
                    creds.destroy()
                    ysc(channelcreds.get())

        def b6():
            def b7():
                global response
                mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                mycursor = mydb.cursor()
                mycursor.execute('select channelid from ' + user + '_yda where channelname = "' + menu.get() + '"')
                myrecord = mycursor.fetchall()
                cn = str(myrecord)[3:-4]
                mydb.commit()
                mycursor.close()
                mydb.close()
                youtube = build('youtube', 'v3', developerKey='AIzaSyBghHd_FTCdfCf51FJxXf8d1kaQCDUKr4U')
                try:
                    request = youtube.channels().list(part='snippet, contentDetails, statistics', id=cn)
                    response = request.execute()
                except Exception:
                    messagebox.showerror('Error', 'Please connect to the internet')

                if len(response) < 4:
                    messagebox.showerror('Error', 'Please enter valid channel creds')
                else:
                    print(response)
                    vsc.destroy()
                    ysc(cn)
            
            mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
            mycursor = mydb.cursor()
            mycursor.execute('select count(*) from ' + user + '_yda')
            myrecord = mycursor.fetchall()
            mycursor.close()
            mydb.close()
            if int(myrecord[0][0]) == 0:
                messagebox.showerror('Error', "You don't have any saved channels yet.")
            else:
                creds.destroy()
                vsc = Tk()
                vsc.title('YouTube Data Analyser')
                vsc.geometry('510x400')
                vsc.resizable(False, False)
                vsc.attributes()

                img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
                Label(vsc, image=img2).place(x=236, y=349)

                img3 = ImageTk.PhotoImage(Image.open('yda.png'))
                Label(vsc, image=img3).place(x=10, y=-30)

                menu = StringVar()
                menu.set('Select your channel')
                mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
                mycursor = mydb.cursor()
                a = []
                mycursor.execute('select channelname from ' + user + '_yda')
                myrecord = mycursor.fetchall()
                for x in myrecord:
                    a.append(str(x)[2:-3])
                mydb.commit()
                mycursor.close()
                mydb.close()
                e = 'drop = OptionMenu(vsc, menu'
                for b in a:
                    e += ', "' + b + '"'
                e += ').place(x=20, y=100)'
                exec(e)
                Button(vsc, text='NEXT =>', font=('Arial', 10, 'bold'), width=12, bd=4, command=b7).place(x=380, y=98)
                vsc.mainloop()

        option.destroy()
        creds = Tk()
        creds.title('YouTube Data Analyser')
        creds.geometry('510x400')
        creds.resizable(False, False)
        creds.attributes()

        img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
        Label(creds, image=img2).place(x=236, y=349)

        img3 = ImageTk.PhotoImage(Image.open('yda.png'))
        Label(creds, image=img3).place(x=10, y=-30)

        channelcreds = StringVar()
        Label(creds, text='Enter Channel ID here:', font=('Arial', 17, 'bold')).place(x=20, y=100)
        Entry(creds, textvariable=channelcreds, font=('arial', 17, 'bold'), width=27).place(x=20, y=150)

        Button(creds, text='NEXT =>', font=('Arial', 10, 'bold'), width=12, bd=4, command=b5).place(x=380, y=148)
        Button(creds, text='VIEW SAVED CHANNELS', font=('Arial', 10, 'bold'), width=30, bd=7, command=b6).place(x=120, y=200)
        Button(creds, text='REMOVE SAVED CHANNELS', font=('Arial', 10, 'bold'), width=30, bd=7, command=remove).place(x=120, y=250)

        creds.mainloop()

    option = Tk()
    option.title('YouTube Data Analyser')
    option.geometry('510x400')
    option.resizable(False, False)
    option.attributes()

    img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
    Label(option, image=img2).place(x=236, y=349)

    img3 = ImageTk.PhotoImage(Image.open('yda.png'))
    Label(option, image=img3).place(x=10, y=-30)

    mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
    mycursor = mydb.cursor()
    mycursor.execute('select fullname from accounts where username = "' + user + '"')
    myrecord = mycursor.fetchall()
    name = myrecord[0][0]
    mycursor.close()
    mydb.close()

    welcometext = 'Welcome, ' + name
    Label(option, text=welcometext, font=('arial', 18, 'bold')).place(x=30, y=100)
    Button(option, text='SINGLE CHANNEL STATS', font=('Arial', 15, 'bold'), width=25, bd=7, command=b2).place(x=105, y=150)
    Button(option, text='COMPARE CHANNELS', font=('Arial', 15, 'bold'), width=25, bd=7, command=b3).place(x=105, y=210)
    Button(option, text='DOWNLOAD A VIDEO / AUDIO', font=('Arial', 15, 'bold'), width=25, bd=7, command=b4).place(x=105, y=270)
    Button(option, text='SIGN OUT', font=('Arial', 10, 'bold'), width=10, bd=5, command=start1).place(x=7, y=360)
    option.mainloop()


while True:
    mydb = sql.connect(host='localhost', user='root', password=mysqlpass)
    d = []
    mycursor = mydb.cursor()
    mycursor.execute('show databases')
    myrecord = mycursor.fetchall()
    for x in myrecord:
        d.append(str(x)[2:-3])
    if 'yda' not in d:
        mycursor.execute('create database yda')
        mydb.commit()
        mycursor.close()
        mydb.close()
    else:
        mycursor.close()
        mydb.close()
        break

while True:
    mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
    d = []
    mycursor = mydb.cursor()
    mycursor.execute('show tables')
    myrecord = mycursor.fetchall()
    for x in myrecord:
        d.append(str(x)[2:-3])
    if 'accounts' not in d:
        mycursor.execute("create table accounts(username varchar(100) primary key, password varchar(200), fullname varchar(50), dob date, rememberme tinyint default 0)")
        mydb.commit()
        mycursor.close()
        mydb.close()
    else:
        mycursor.close()
        mydb.close()
        break

while True:
    mydb = sql.connect(host='localhost', user='root', password=mysqlpass, database='yda')
    mycursor = mydb.cursor()
    mycursor.execute('desc accounts')
    myrecord = mycursor.fetchall()
    i = [('username', b'varchar(100)', 'NO', 'PRI', None, ''), ('password', b'varchar(200)', 'YES', '', None, ''), ('fullname', b'varchar(50)', 'YES', '', None, ''), ('dob', b'date', 'YES', '', None, ''), ('rememberme', b'tinyint', 'YES', '', b'0', '')]
    if myrecord != i:
        mycursor.execute('alter table accounts add column rememberme tinyint default 0')
        mydb.commit()
        mycursor.close()
        mydb.close()
        break
    else:
        mycursor.close()
        mydb.close()
        break



ydaintro = Tk()
ydaintro.title('YouTube Data Analyser')
ydaintro.geometry('510x400')
ydaintro.resizable(False, False)
ydaintro.attributes()

img2 = ImageTk.PhotoImage(Image.open('Made by Mayank Bajaj.png'))
Label(ydaintro, image=img2).place(x=236, y=349)

img3 = ImageTk.PhotoImage(Image.open('welcome.png'))
Label(ydaintro, image=img3).place(x=100, y=20)

Button(ydaintro, text='GET STARTED =>', font=('Arial', 10, 'bold'), width=15, bd=4, command=start2).place(x=187, y=300)

ydaintro.mainloop()
