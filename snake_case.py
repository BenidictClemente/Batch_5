def snake_case(name):
  return name.lower().replace(" ","_")
name = input("Enter your name :")
print(snake_case(name))
