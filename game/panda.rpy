## Panda DATE 1

label pandadate1:
    p "Alright. I could…"
    p "*yawn*"
    p "…spare some time for you, I guess."

    scene bg cafe day
    with fade
    show panda normal
    with dissolve
    
    p "I love the café. So many wonderful smells!"
    p "I could just sit here and eat and eat and eat."
    p "What do you like most about the café?"
menu:
    "Smells":
        jump pandadate1_choice1_smells
    
    "Food":
        jump pandadate1_choice1_food
    
    "Firmness of the seats":
        jump pandadate1_choice1_seats
    
label pandadate1_choice1_smells:
    p "I absolutely agree. It's truly a…"
    p "*yawn*"
    p "…treat for the nose. The nose knows, after all. *chuckle*"
    jump pandadate1_choice2

label pandadate1_choice1_food:
    p "Yes, the food here is quite scrumptious!"
    p "Fresh cuisine is very important to a bear of my standards."
    jump pandadate1_choice2

label pandadate1_choice1_seats:
    p "Oh, is that so? Chairs usually bruise my baby bear bottom."
    p "I prefer the comfort of the bare ground. Each to their own, I suppose…"
    jump pandadate1_choice2
    
label pandadate1_choice2:
    p "You see, a proper dining atmosphere is very important to me."
    p "I may seem like your typical lazy panda, but even I have dreams and ambitions."
    p "My calling in life is food, and one day I hope to open up my own restaurant!"
    p "I'd recruit famous chefs the world over, and…"
    p "*yawn*"
    p "...serve the greatest food known to earthkind!"
    p "Alas, now that we're stuck in here I fear my dream may never come true…"
menu:
    "Don't give up hope!":
        jump pandadate1_choice2_hope
    
    "Pandas can't open resturants, silly.":
        jump pandadate1_choice2_silly
    
    "Have you ever heard of \"Panda Express\"?":
        jump pandadate1_choice2_express
    
label pandadate1_choice2_hope:
    p "You're too kind, really."
    p "But I fear it's just…"
    p "*yawn*"
    p "…wishful thinking at this point."
    p "Thank you for believing in me."
    jump pandadate1_success

label pandadate1_choice2_silly:
    p "Thanks for the \"encouraging\" words."
    p "I may be slow, but I'm not dull."
    p "At least humor me in my…"
    p "*yawn*"
    p "…lofty ambitions."
    jump pandadate1_failure

label pandadate1_choice2_express:
    p "Don't even mention that foul place!"
    p "A culinary auteur such as myself has no patience for \"take-out\" establishments."
    p "Do you think me a panda of…"
    p "*yawn*"
    p "…poor taste?"
    jump pandadate1_failure

label pandadate1_success:
    p "You've given me new resolve, Cutie."
    p "Perhaps my dream isn't so far-fetched after all."
    p "Cutie, you seem to be quite the foodie yourself!"
    p "Ever thought about…"
    p "*yawn*"
    p "…being a maitre d?"
    p "Hahahahaha."
    jump whatever

label pandadate1_failure:
    p "Hmm, maybe you weren't the culinary appreciator I thought you were."
    p "Thank you for humoring me in my…"
    p "*yawn*"
    p "…idle chatter. Perhaps I'll see you around, or perhaps not."
    p "Farewell."
    jump whatever
    
## Panda DATE 2

label pandadate2:
    p "Why don't we dine in…"
    p "*yawn*"
    p "…a more secluded spot?"

    scene bg pools day
    with fade
    show panda normal
    with dissolve
    
    p "This is a favorite spot of mine."
    p "The clear water, reflecting everything off its surface…"
    p "I could get lost in…"
    p "*yawn*"
    p "…the crystal blue."
    p "So, Cutie, have you given it any thought?"
menu:
    "Yes, I have.":
        jump pandadate2_choice1_yes
    
    "What are you talking about?":
        jump pandadate2_choice1_what

label pandadate2_choice1_yes:
    p "I knew you were a human of taste!"
    jump pandadate2_choice2
    
label pandadate2_choice1_what:
    p "Oh…you don't remember?"
    p "I thought you wanted to be my maitre d…"
    jump pandadate2_choice2
    
label pandadate2_choice2:
    p "I've been thinking about our time together."
    p "We've only known each other for a short time, and yet…"
    p "*yawn*"
    p "…you seem to understand my passion."
    p "Perhaps…you could be more than just the waitstaff?"
    p "You and I could be head chefs of our very own restaurant."
    p "What would you want as the special of the day?"
    
menu:
    "...Love.":
        jump pandadate2_success
    
    "Fish Sticks":
        jump pandadate2_failure

label pandadate2_success:
    p "I was hoping you'd say that."
    p "Bears can be quite adept at cuddling, too."
    p "Would you like to take an after-dinner nap with me?"
    "You spend hours cuddling with Panda."
    jump whatever
    
label pandadate2_failure:
    p "You're testing me, NAME."
    p "Could you at least act like you care about this bear?"
    "You and Panda spend your time in silence."
    jump whatever
        
## Panda Dates OVER