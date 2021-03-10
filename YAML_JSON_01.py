import re
import time


class Timetable:
    def __init__(self, subjects):
        self.subjects = subjects


class TimetableParser:
    def parser(self, line, subject):
        line = str(line).replace(" ", "", 1)
        x = line.split(":")
        key = x[0]
        word = x[1].replace("\n", "")
        if key == "day":
            subject.day = word
        elif key == "time":
            subject.time = x[1] + ":" + x[2] + ":" + x[3]
        elif key == "room":
            subject.room = eval(word)
        elif key == "lesson":
            subject.lesson = word
        elif key == "teacher":
            subject.teacher = word
        elif key == "location":
            subject.location = word
        elif key == "week":
            subject.week = word
        return subject

    def run(self, fileIn):
        lines = fileIn.readlines()
        subjects = [Lection(), Lection(), Lection(), Lection()]
        k = -1
        for line in lines:
            line = line.replace("\n", "")
            line = line.replace("  ", "")
            if re.fullmatch(r"\s*subject\d:", line):
                k += 1
            elif line.count("timetable") != 1:
                subjects[k] = self.parser(line, subjects[k])
        schedule = Timetable(subjects)
        return schedule


class Lection:
    def __init__(self):
        self.day = None
        self.time = None
        self.room = None
        self.lesson = None
        self.teacher = None
        self.location = None
        self.week = None


start_time = time.time()
fileIn = open("Wednesday.yaml", 'r')
parser = TimetableParser()
schedule = parser.run(fileIn)
json = "{\n\t\"timetable\": {\n"
for i in range(len(schedule.subjects)):
    j = 0
    el = schedule.subjects[i]
    json += "\t\t\"subject{}\": {}\n".format(i + 1, "{")
    sub_dict = schedule.subjects[i].__dict__
    for p in sub_dict:
        if type(sub_dict[p]) is int:
            json += "\t\t\t\"{}\": {},\n".format(p, sub_dict[p])
            j = j + 1
            continue
        if j == len(sub_dict) - 1:
            json += "\t\t\t\"{}\": \"{}\"\n".format(p, sub_dict[p])
        else:
            json += "\t\t\t\"{}\": \"{}\",\n".format(p, sub_dict[p])
            j = j + 1
    if i == len(schedule.subjects) - 1:
        json += "\t\t{}\n".format("}")
    else:
        json += "\t\t{}\n".format("},")
json += "\t}\n}"
fileIn.close()

fileOut = "Wednesday_01.json"
openFile = open(fileOut, 'w')
openFile.write(json)
openFile.close()
print("Successfully converted!\nSaved to file:", fileOut)

print("Executed time: %s seconds." % (time.time() - start_time))
