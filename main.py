'''1/Room Rent
2/Roommates no
3/Monthly food expense
4/Electricity bill
5/E-bill per unit charge
6/Wifi bill
'''

room_rent=int(input("Enter the Amt. of Monthly Room Rent :- ₹"))
total_roommates=int(input("Enter total no. of Room-Mates :- "))
food_expense=int(input("Enter the Amt. of Total Food-Expenses :- ₹"))
e_bill=int(input("Enter the total Units of Electricity used :- "))
unit_charge=int(input("Enter the Amt. of Per Unit Electric Charge :- ₹"))
wifi_bill=int(input("Enter the Amt. of Wifi-bill :- ₹"))
ebill_total= e_bill*unit_charge

total= room_rent+food_expense+ebill_total+wifi_bill
total2= (room_rent+food_expense+ebill_total+wifi_bill)//(total_roommates)

print(f"Total Expense For This Month :- {total}")
print(f"Each Room-mates will pay :- ₹{(total2)}")

