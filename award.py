swimming = 0
cycling = 0
running = 0

total_triathlon = sum([swimming, cycling, running])
print(f"Thank you for participating in the triathlon!\nYour total time to complete the triathlon was: {total_triathlon}")

if total_triathlon <= 100:
    print("You have qualified and earned the award of Provincial colours.")
elif 101 <= total_triathlon <= 105:
    print("You have earned the award of Provincial half colours.")
elif 106 <= total_triathlon <= 110:
    print("You have earned the award of Provincial scroll.")
else:
    print("No award given")
