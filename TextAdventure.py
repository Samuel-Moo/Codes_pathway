start = print("""You're the hero, 
but you have already finished 
everything a hero a has
to do and you're bored, 
you decide to do something with your life, 
you settle on 3 options, 
find FRIENDS and maybe a partner, 
or live a RELAXED life in 
your house in the forest.""") 
first_decision = input("What do you decide to do FRIENDS/RELAXED? ")

if first_decision.lower() == "friends":
    print("""You decide to go find some friends, 
but it isn't as simple as you would think,
because everyone in the country knows you, 
either they get with you because of your fame 
or they simply are afraid of you. 
You can decide to go to ANOTHER place 
where you aren't know or GIVE UP and go 
to your home. """)
    friends1 = input("What will you do? ANOTHER/GIVE UP")
    
    if friends1.lower ()== "another":
        print("""You decide to go to another place,
a far far away place where you name is only
gossip, there you meet some companions that 
invite you to form a party with them, 
you realize that having friends is nice,
and there is even a girl who looks like
    she likes you... 
    THE END""")
    elif friends1.lower() == "give up":
        print("""Life alone isn't so bad, 
maybe you can get used to it, 
but a part of you will always 
be a little regretful that you 
had chose to go to another place... 
THE END""")
    else: 
        print("""Why? Why can't I make friends? What's 
the point in saving the world if you 
have no one to enjoy it with? Is there 
even a point in living anymore? 
Wait a second, what if I was reborn
again? What would happen in that case?
It is very risky, do I do it?""")
    friends2 = input("YES/NO? ")    
    
    if friends2.lower() == "yes":
        print("""The decision has been made,
I will do it! As you said,
it was done, but when you did
it you couldn't remember anything
of your past life so everything repeated..
START AGAIN PLEASE """)        
    elif friends2.lower() == "no":
        print("""I don't thing it's worth it...
THE END""")
    
elif first_decision.lower() == "relaxed":
        print("""A relaxed life is nice, 
I think I will do this until
my time comes...
THE END""")

else:
    print("""You couldn't decide on any of the 
other options, so you decide to 
go start away in a faraway place, 
there you lived amazing things, 
but that is a story for another time. THE END """)

