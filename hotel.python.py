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
  print("\t\t\t\t\t 4 Amenities Information")
  print("\t\t\t\t\t\t 5 Exit")
  
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
elif agent == 4:
  print(" ")
  Amenities()
else:
  exit()
  
Home()
