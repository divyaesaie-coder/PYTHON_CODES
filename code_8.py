#Question:Program to read,add and save tasks using file handling.
tasks=[]																	
try:
        f=open("tasks.txt","r")
        for line in f:
        	tasks.append(line.strip())
        	f.close()
except:
	pass
date=input("enter date:")
print(date)
while True:
    task = input("Enter task including time(or type exit): ")
    if task == "exit":
        break
    tasks.append(task)
f=open("tasks.txt","w")
for t in tasks:
	f.write(t+"/n")
f.close()
print("tasks saved!")
print(tasks)
