print("Welcome to Hotel Python!")
print("\t\t 1 Booking")
print("\t\t 2 Payment")
print("\t\t 3 Guest Requests")
print("\t\t 4 Exit")

reservation=" "
payment=" "
payment_method=" "
requests=" "

def guest_info(reservation="A"):
    print("Please collect guest information such as name, phone number, and dates of stay")
    reservation=" "

guest_info("A")

agent=input("Enter guest name: ")
print(agent)

agent_a=input("Enter guest phone number: ")
print(agent_a)

agent_b=input("Enter the desired check in date and check out date in MM/DD/YY = MM/DD/YY: ")
print(agent_b)

agent_c=input("Enter cash or card: ")
print(agent_c)


def guest_requests(requests="R"):
    print("Ask guest if they have any special requests for the room: ")
    requests="R"

guest_requests("R")

agent_d=input("Enter special requests: ")
print(agent_d)

while True:
    breakfast = input("Would you like to add breakfast to your stay (yes or no): ")
    print()
    
    if breakfast.lower() == "yes":
        print("Breakfast will be added to your final bill. This includes breakfast for two. Each additional meal will be $10.")
        break
    else:
        print("Breakfast will not be added to your final bill. Please let me know if you would like to change that.")

room_rate=int(input("Enter weekend room rate: "))
hotel_stayfee=5
breakfast_charge=10

final_total=room_rate + hotel_stayfee + breakfast_charge

print()

print("Repeat the following information back to guest: ")
print()
print("Thank you for choosing to stay at Hotel Python. We have", agent, "staying with us", agent_b, "using", agent_c, "to pay for the room. We also made sure to include", agent_d, "in the room notes as well.")

print()
print("Final Bill as follows...")
print(agent, ",thank you for choosing to stay with us.")
print(agent_a)
print()
print("Method of Payment: ", agent_c)
print("Breakfast Charge: ", breakfast)
print("The total amount charged for your stay is $", final_total)
