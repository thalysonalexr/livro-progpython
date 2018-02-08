days = int(input("Days: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

total = days * 24 * 60 * 60
total = total + hours * 60 * 60
total = total + minutes * 60 + seconds

print("Quantidade de segundos: %d" %(total))
