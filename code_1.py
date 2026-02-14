#QUESTION:Create a Python program to record daily exercise,study and sleep data, and identify days with low sleep(<7hrs)
entries = []
while True:
    print("ADD TODAY'S DATE:")
    d = input("Date: ")
    ex = int(input("Exercise mins: "))
    st = int(input("Study mins: "))
    sl = float(input("Sleep hours: "))
    entries.append({"date": d, "ex": ex, "st": st, "sl": sl})
    print("Saved!")

    print("\n1) View all  2) Low sleep")
    ch = input("Choose: ")

    if ch == "1":
        for e in entries:
            print(e)
    if ch == "2":
        for e in entries:
            if e["sl"] < 7:
                print("Low sleep:", e)
            else:
                print("Good sleep:", e)
    if input("CONTINUE?(yes/no): ") != "yes":
        print("THANK YOU!!")
        break
