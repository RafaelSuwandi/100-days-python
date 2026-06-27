# NOTE Section 2 : Day 2 (Beginner)
print("DAY 2")
# Learning about Basic Data type, Arithmatic and f-string function

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip will you give? 10, 12, or 15? "))
people = int(input("How many people will split the bill? "))

# Math on tip percentage
percen_tip = tip / 100 # First make the tip into decimal
total_tip = bill * percen_tip # Then do bill time percen_tip to get the total_tip
total_bill = total_tip + bill # Then do bill plus total_tip to get the total_bill (bill + tip)
pay = round(total_bill / people, 2) # At last divide the total_bill and the number of people (don't forget to use round function to get the last two decimal)

print(f"Each person should pay: {pay}")  # Print the total amount of money, each person has to pay using f string 