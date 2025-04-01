from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def main():
    if(request.method == "GET"):
        return render_template("ScheduleInfo.html")
    else:
        CreateCheckFile();
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

    data = (
        (1,course1, teacher1, room1),
        (2,course2, teacher2, room2),
        (3,course3, teacher3, room3),
        (4,course4, teacher4, room4),
        (5,course5, teacher5, room5),
        (6,course6, teacher6, room6),
        (7,course7, teacher7, room7),
        (8,course8, teacher8, room8)
        )
    
    return DisplayInfo()

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

    logacctfile.write(str(username) + "," + str(userpasswd));


if __name__=="__main__":
    app.run();
