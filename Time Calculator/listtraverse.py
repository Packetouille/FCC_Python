entry = input("Enter a day: ")
days_later = int(input("Days to advance: "))
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

entry = entry.lower()
entry = entry.capitalize()

index = days.index(entry)
start_day = days[index]

count = 0
while count < days_later :
    count += 1; index += 1
    if index >= len(days) :
        index = 0

print(f"Final = {days[index]}")
