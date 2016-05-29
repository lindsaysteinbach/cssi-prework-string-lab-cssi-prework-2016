
### Challenge 1 - Percy Replacement:
def percy_replacer(string_about_percy):
  return string_about_percy.replace('Percy','Ron')

### Challenge 2 - String Interpolation:
def weasley_invitation(name,day,date,month):
  return "The family of {name} Weasley proudly invite you to celebrate their graduation from Hogwarts on {day} the {month} of {date}. Festivities will be held at The Burrow. See you then!".format(name="Ron",day="Sunday",date="18th",month="May")

### Challenge 3 - Seating Location
def seating_location(last_name):
  rear="ABCDEFG"
  front="W"
  
  if (last_name[0] in rear) == True:
      row = "the rear section"
  elif (last_name[0] in front) == True:
      row = "the front row"
  else:
      row = "the middle section"

  return "You have a reserved seat in {seating_area}.".format(seating_area=row)

###Challenge 4 - All Together
def create_invitation(first_name, last_name, message):
  cap_first = first_name.upper()
  ps_message=seating_location(last_name)

  return "DEAR {first},\n{msg}\nP.S. {ps_msg}".format(first=cap_first, last=last_name, msg=message, ps_msg=ps_message)