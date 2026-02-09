name = input("Enter the name:")
goal = input("Enter the daily goal:")
# file = open("journal.txt","a")
# file.write("\nThis is JP Nagar")
# file.write("\nBengaluru - 560078")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Daily_goal: {goal}\n")

print("Entry saved to journal")