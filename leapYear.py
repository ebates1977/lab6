def leap_year():
  year = int(input("please enter the year: "))

  if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
      print(str(year) + " is a leap year")
      return True

   

  else:
    print(str(year) + " is not a leap year")
    return False
    
leap_year()