def happy_birthday(day, month):
  # Let's sanitatize the inputs
  if day is not int:
    raise TypeError('Invalid day value ({day}). Must be a number.')
  if month is not int:
    raise TypeError('Invalid month value ({month}).  Must be a number.')
  if day < 1 or day > 31:
    raise ValueError(f'Invalid day value ({day}).  Must be between 1 and 31.')
  if month < 1 or month > 12:
    raise ValueError(f'Invalid month value ({month}).  Must be between 1 and 12.'

  # Let's generate some happy birthday messages
  if month == 2 and day == 22:
    return "Happy Birthday George Washington!"
  elif month == 7 and day == 4:
    return "Happy Birthday America!"
  # Add in other options below

  # This will catch all other cases
  else:
    return "Happy Birthday!"
        
