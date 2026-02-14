#QUESTION:Given marks  of multiple students,calculate each student's total marks and idenify the topper with highest score.
students = {
    "Asha": {"math": 80, "science": 75, "english": 90},
    "Rahul": {"math": 65, "science": 70, "english": 60}
}
students["Divya"]={"math":90,"science":89,"english":99}#added new student
students["Asha"]["math"]=70#updated marks
#finding out the topper
#step1:find the total of three students
asha=0
for mark in students["Asha"].values():
    asha=asha+mark
print("Asha_total",asha)
rahul=0
for mark in students["Rahul"].values():
    rahul=rahul+mark
print("rahul_total",rahul)
divya=0
for mark in students["Divya"].values():
    divya=divya+mark
print("Divya_total",divya)
#step2:put all the total value of three students together in one dict
total={"Asha":asha,"Rahul":rahul,"Divya":divya}
print(total)
#step3:using the max key word to find highest marks
highest_marks=max(total.values())
for name in total:
    if total[name]==highest_marks:
        topper=name
print("The topper is",topper,"with",highest_marks,"marks")
