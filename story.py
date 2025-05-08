# Arianna Hicks
# 10/11/24
# This program will walk the user through a chose your own adventure story. 

print("The day started off great, clear skies and a warm breeze. A perfect day for a walk. \n\n As you were on your walk the wind started to pick up and the skies turned grey. \n\n")

choice1 = input("The weather's starting to make you nervous. Do you want to continue walking, or find somewhere to wait out the storm? Enter your Choice (continue/wait):").strip().lower()
choice2 = ""

if choice1 == "wait":
  choice2 = input("\n\n You run over to a nearby shack. When you get there you're hesitant to go inside. Do you want to go in, or should you wait it out under a nearby tree instead? Enter your Choice (shack/tree):").strip().lower()
  if choice2 == "tree":
    print("\n\n Good idea! You waited out the storm and can now return home safe. The end!")
    input("Press Enter to Exit:")
  elif choice2 == "shack":
    print("\n\n Bad choice. You opened the door to the shack and were immediatley trapped by an evil witch. You never made it back home. The end!")
    input("Press Enter to Exit:")
  else:
   print ("That wasn't an option. Your story ends here. Pay attention next time.")

elif choice1 == "continue":
  print("\n\n Bad choice. You got struck by lightning and never made it back home. The end!")
  input("Press Enter to Exit:")
else:
  print ("That wasn't an option. Your story ends here. Pay attention next time.")
