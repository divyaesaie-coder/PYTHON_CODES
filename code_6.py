#Question:Program to calculate total fare between multiple stops using given routes,with validation.
routes = {
    ("StopA", "StopB"): 15,
    ("StopB", "StopC"): 10,
    ("StopC", "StopD"): 12
}
print(routes)
stops=input("Enter stops:").split(",")
total=0
error=False

for i in range(len(stops)-1):
    leg=(stops[i].strip(),stops[i+1].strip())
    if leg in routes:
        total+=routes[leg]
    else:
        print("NO ROUTE")
        error=True
        break
if not error:
    print("Total_fare:",total)
