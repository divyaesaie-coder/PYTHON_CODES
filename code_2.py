#QUESTION:Calculate library fines with differnt late days for each book.
books=[]
borrowed =input("ENTER THE BOOK:").split(",")
total_fine=0
for book in borrowed:
    days_late=int(input(f"ENTER DAYS LATE FOR {book}:"))
    if days_late<=5:
        fine=days_late*2
    else:
        fine=(5*2)+((days_late-5)*5)
    total_fine+=fine
print("Total_fine:$",total_fine)
