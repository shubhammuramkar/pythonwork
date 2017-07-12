import json
def greet_user():
  """Greet the user by name."""
  filename = "usernames.json"
  try:
    with open(filename) as f:
      username = json.load(f)
  except FileNotFoundError :
    username = input("Enter your name ")
    with open(filename,'w') as f:
      json.dump(usernames,f)
      print("I will remnember you when you will come back " + username  + "!")
  else:
    print("Welcome back, " + username + "!")
greet_user()