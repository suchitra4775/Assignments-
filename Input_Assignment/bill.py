total_amount = float(input("total amount: ")) 
tip_percentage = float(input("Tip percentage: "))
number_of_people = int(input("Number of people: "))
tip_amount = total_amount * tip_percentage / 100
bill_contribution = total_amount / number_of_people
tip_contribution = tip_amount / number_of_people
total_contribution = bill_contribution + tip_contribution
print("Bill contribution per person: ", bill_contribution)
print("Tip contribution per person: ", tip_contribution)
print("Total contribution per person: ", total_contribution)