# Ask the user if they have played open
show_instruotion = input("have you played this game"
"before? ") .lower()

# If they say yes, output 'program continues'
if show_instruotion == "yes":
    print("program continues")

elif show_instruotion == "no":
  print("display instructions")

# If they say no, output 'display instruotion'
else:
   print("please answer yes / no")
