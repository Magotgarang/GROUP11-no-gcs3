m = int(input("Enter a number: "))

if m % 2 == 0:
    print("Weird")
else:
    if m >= 2 and m <= 5:
        print("Not weird")
    elif m >= 6 and m <= 20:
        print("Weird")
    elif m >= 20:
        print("Not weird")
