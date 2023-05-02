value=input("Calculator\n")
if "*" in value:
    first=float(value.split("*")[0])
    second=float(value.split("*")[1])
    total=first*second
    print(total)
elif "/" in value:
    first=float(value.split("/")[0])
    second=float(value.split("/")[1])
    total=first/second
    print(total)
elif "+" in value:
    first=float(value.split("+")[0])
    second=float(value.split("+")[1])
    total=first+second
    print(total)
elif "-" in value:
    first=float(value.split("-")[0])
    second=float(value.split("-")[1])
    total=first-second
    print(total)
else:
    print("ERROR TRY AGAIN")
