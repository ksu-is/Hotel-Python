name = []
phone_number = []
room_number = []
reservation = []
price = []
customer_id = []

def Home():
  print("\t Welcome to Hotely Python")
  print("\t\t 1 Booking")
  print("\t\t\t 2 Payment")
  print("\t\t\t\t 3 Guest Requests")
  print("\t\t\t\t\t 4 Exit")
  
agent == input("Enter an option to start: ")
if agent == 1:
  print(" ")
  Booking()
elif agent == 2:
  print(" ")
  Payment()
elif agent == 3:
  print(" ")
  Guest_Requests()
else:
  exit()
  
Home()
