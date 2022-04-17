num = float(input("enter your number: "))
def is_numeric(num):
  
  if isinstance(num, int):
    return True
  elif isinstance(num, float):
    return True
  else:
    print(False)

print(is_numeric(num))