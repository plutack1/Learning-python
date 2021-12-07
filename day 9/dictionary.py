travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
new_country = input("what is the name of the country?")
no_of_visits = input("How many times did you visit?")
cities_visited = []
run_again = True
while run_again is True:
  city = input("What is the name of the city?")
  cities_visited.append(city)
  answer = input("Did yo visit another city?\nYes or No").lower()
  if answer == "yes":
    run_again = True
  else:
    run_again = False
new_entry = {}
new_entry["country"] = new_country
new_entry["visits"] = no_of_visits
new_entry["cities"] = cities_visited
travel_log.append(new_entry)











#🚨 Do not change the code below
#add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
