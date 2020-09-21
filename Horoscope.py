#To show today'shoroscope

print('''
       1)Aries
       2)Taurus
       3)Gemini
       4)Cancer
       5)Leo
       6)Virgo
       
       ''')

s= int(input("Chhose your Horscope acoording to your name and press enter"))
print(s)


if s==1:
print("There could be trouble brewing in the workplace, Aries."
            "Some of your colleagues neither like nor trust each other and find it impossible to work together."
           " Adjustments are needed if everyone is going to work to the best of their abilities."
           " If you are in a position to handle this, do it now. If you are not distance yourself from the situation."
            "It is the only way to stay sane!")
elif s==2:
print("Squabbles may come up between you and a sibling or neighbor, Taurus."
      "Your ability to compromise is definitely called for here."
     " If you aren't careful, this could turn into a battle of wills."
                 " The minute the disagreement comes up, try to talk it out and turn it into a win/win situation."
      "Otherwise, things may be said that shouldn't be, and feelings could remain hurt for a long time.")
elif s==3:
print("Squabbles may come up between you and a sibling or neighbor, Taurus."
           " Your ability to compromise is definitely called for here."
            "If you aren't careful, this could turn into a battle of wills."
           " The minute the disagreement comes up, try to talk it out and turn it into a win/win situation."
           " Otherwise, things may be said that shouldn't be, and feelings could remain hurt for a long time."
 elif s==4:
 print("Too much rigorous exercise over the past few days might have you feeling a little sore and tired, Cancer."
                  "Your nerves may be on edge, and you could be more likely than usual to snap at those around you."
                 " Try to ease both nerves and muscle aches by soaking in a hot bath."
                  "Herbal tea might also help."
                  "Accept that you should take it easy today and then do it!")
 elif s==5:
 print("Ganesha foresees that today, you will be gripped by the desire to shop till you drop, even if"
                  "it means having to spend a small fortune from your hard-earned savings!"
                  "You have no problem with that,"
                  "especially if all the money-spending is being undertaken to please your sweetheart."
                  "Those who try to warn you against carrying out your plans will be doing so in vain."
                  "It's not for nothing they say, “Love is blind.”)
elif s==6:
print("A virtual conference of some kind could touch upon some pretty volatile issues, Virgo."
                  "People could disagree to the point that the meeting turns into a shouting match."
                  "You probably have strong opinions on this as well, but don't get involved."
                 " You won't be able to stop the argument, and it can only cause you stress."
                 " If you can, avoid joining this meeting altogether."
                 " Think about it!")
else:
print("Invalid input")



                  
