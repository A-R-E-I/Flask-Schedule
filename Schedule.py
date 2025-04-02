from flask import Flask, render_template, request
import os.path
from os import path

app = Flask(__name__)

global whichfilename, period1, period2, period3, period4, period5, period6, period7, period8;
whichfilename = "LoginAccounts.doc";
period1 = []
period2 = []
period3 = []
period4 = []
period5 = []
period6 = []
period7 = []
period8 = []

@app.route("/", methods=["GET","POST"])
def main():
    if(request.method == "GET"):
        return render_template("ScheduleInfo.html")
    else:
        return GetInfo()
    
def GetInfo():
    global headings, data
    headings = ("Period","Course name","Teacher name","Room Number")
    
    course1 = request.form.get("txtcoursename1")
    teacher1 = request.form.get("txtteacher1")
    room1 = request.form.get("txtroom1")
        
    course2 = request.form.get("txtcoursename2")
    teacher2 = request.form.get("txtteacher2")
    room2 = request.form.get("txtroom2")
    
    course3 = request.form.get("txtcoursename3")
    teacher3 = request.form.get("txtteacher3")
    room3 = request.form.get("txtroom3")

    course4 = request.form.get("txtcoursename4")
    teacher4 = request.form.get("txtteacher4")
    room4 = request.form.get("txtroom4")

    course5 = request.form.get("txtcoursename5")
    teacher5 = request.form.get("txtteacher5")
    room5 = request.form.get("txtroom5")

    course6 = request.form.get("txtcoursename6")
    teacher6 = request.form.get("txtteacher6")
    room6 = request.form.get("txtroom6")

    course7 = request.form.get("txtcoursename7")
    teacher7 = request.form.get("txtteacher7")
    room7 = request.form.get("txtroom7")

    course8 = request.form.get("txtcoursename8")
    teacher8 = request.form.get("txtteacher8")
    room8 = request.form.get("txtroom8")

    firstPd = period1.append("|" + str(course1) + "|" + str(teacher1) + "|" + str(room1) + "|")
    secondPd = period2.append("|" + str(course2) + "|" + str(teacher2) + "|" + str(room2) + "|")
    thirdPd = period3.append("|" + str(course3) + "|" + str(teacher3) + "|" + str(room3) + "|")
    fourthPd = period4.append("|" + str(course4) + "|" + str(teacher4) + "|" + str(room4) + "|")
    fifthPd = period5.append("|" + str(course5) + "|" + str(teacher5) + "|" + str(room5) + "|")
    sixthPd = period6.append("|" + str(course6) + "|" + str(teacher6) + "|" + str(room6) + "|")
    seventhPd = period7.append("|" + str(course7) + "|" + str(teacher7) + "|" + str(room7) + "|")
    eighthPd = period8.append("|" + str(course8) + "|" + str(teacher8) + "|" + str(room8) + "|")
    CreateCheckFile();
    TakefileInfo();

    data = (
        (1,Pd1course, Pd1teacher, Pd1room),
        (2,Pd2course, Pd2teacher, Pd2room),
        (3,Pd3course, Pd3teacher, Pd3room),
        (4,Pd4course, Pd4teacher, Pd4room),
        (5,Pd5course, Pd5teacher, Pd5room),
        (6,Pd6course, Pd6teacher, Pd6room),
        (7,Pd7course, Pd7teacher, Pd7room),
        (8,Pd8course, Pd8teacher, Pd8room)
        )

    return DisplayInfo()

def TakefileInfo():
    global Pd1course, Pd1teacher, Pd1room, Pd2course, Pd2teacher, Pd2room;
    global Pd3course, Pd3teacher, Pd3room, Pd4course, Pd4teacher, Pd4room;
    global Pd5course, Pd5teacher, Pd5room, Pd6course, Pd6teacher, Pd6room;
    global Pd7course, Pd7teacher, Pd7room, Pd8course, Pd8teacher, Pd8room;
    Infofilename = open(whichfilename,"r");
    UserValue = Infofilename.read().split("|");
    Infofilename.close();
    
    Pd1course = UserValue[1].strip();
    Pd1teacher = UserValue[2].strip();
    Pd1room = UserValue[3].strip();
    
    Pd2course = UserValue[5].strip();
    Pd2teacher = UserValue[6].strip();
    Pd2room = UserValue[7].strip();

    Pd3course = UserValue[9].strip();
    Pd3teacher = UserValue[10].strip();
    Pd3room = UserValue[11].strip();

    Pd4course = UserValue[13].strip();
    Pd4teacher = UserValue[14].strip();
    Pd4room = UserValue[15].strip();

    Pd5course = UserValue[17].strip();
    Pd5teacher = UserValue[18].strip();
    Pd5room = UserValue[19].strip();

    Pd6course = UserValue[21].strip();
    Pd6teacher = UserValue[22].strip();
    Pd6room = UserValue[23].strip();

    Pd7course = UserValue[25].strip();
    Pd7teacher = UserValue[26].strip();
    Pd7room = UserValue[27].strip();

    Pd8course = UserValue[29].strip();
    Pd8teacher = UserValue[30].strip();
    Pd8room = UserValue[31].strip();
  

def DisplayInfo():
    return render_template("ScheduleOutput.html",headings=headings,data=data)

def CreateCheckFile():
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    fileexist = bool(path.exists(whichfilename));
    if(fileexist == False):
        status = "new";
    else:
        status = "edit"

    WriteToFile(status);

def WriteToFile(whichstatus):
    if(whichstatus == "new"):
        logacctfile = open(whichfilename,"x")
        logacctfile.close();
        logacctfile = open(whichfilename,"w")
    else:
        logacctfile = open(whichfilename,"a")
        logacctfile = open(whichfilename,"w")

    filevalOne = period1
    filevalTwo = period2
    filevalThree = period3
    filevalfour = period4
    filevalfive = period5
    filevalsix = period6
    filevalseven = period7
    filevaleight = period8
    
    logacctfile.write(str(filevalOne) + str(filevalTwo) + str(filevalThree) + str(filevalfour) + str(filevalfive) + str(filevalsix) + str(filevalseven) + str(filevaleight));

if __name__=="__main__":
    app.run();
