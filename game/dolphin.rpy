## Dolphin DATE 1

label dolphindate1:
    d "Alright! Race you to the bottom and back!"
    
    scene bg pools day
    with fade
    show dolphin normal
    with dissolve
    
    d "Wow, you're a pretty good swimmer!"
    d "Where'd you learn those moves?"

menu:
    "Yeah, I work out.":
        jump dolphindate1_choice1_workout
    
    "I'm just a natural-born swimmer!":
        jump dolphindate1_choice1_natural
        
label dolphindate1_choice1_workout:
    d "Me too! I'm a real exercise nut."
    d "I could just swim around all day."
    d "I mean, I'm pretty much required to swim around to move freely, but hey!"
    d "Might as well enjoy it, right?"
    jump dolphindate1_choice2
    
label dolphindate1_choice1_natural:
    d "Ha! I love your enthusiasm."
    d "All you're missing is a pair of flippers!"
    jump dolphindate1_choice2
    
label dolphindate1_choice2:
    d "What are you looking at?"
    d "Oh, you noticed my book?"
    d "I may not look it, but I'm a pretty big nerd!"
    d "I love reading and video games, but others only ask me for personal training advice."
    d "It's like, I love getting swoll for the summer, but a girl's got other passions!"
    d "I mean, what do you see when you look at me?"
    
menu:
    "A jock.":
        jump dolphindate1_choice2_jock
        
    "A nerd.":
        jump dolphindate1_choice2_nerd
    
    "You're just you.":
        jump dolphindate1_choice2_you
        
label dolphindate1_choice2_jock:
    d "Oh, really? Yeah, I guess at first glance…"
    jump dolphindate1_success
    
label dolphindate1_choice2_nerd:
    d "Only because I just told you that!"
    jump dolphindate1_success
    
label dolphindate1_choice2_you:
    d "Hmmm…"
    d "You know, no one's said that to me before!"
    jump dolphindate1_success
    
label dolphindate1_success:
    d "Regardless, you're a pretty cool guy."
    d "If you want, I can show you my vintage Sega Genesis!"
    d "Though I can't turn it on, what with us being underwater and all…"
    "You spend some time looking at old video games with Dolphin."
    "…"
    d "That was a lot of fun, Cutie."
    d "I'm glad you're so open-minded."
    d "Going with the flow is the only way to live life!"
    d "Don't get so hung up on preconceived notions of people."
    d "Right?"
    d "Anyways, hopefully we can hang out again!"
    "You swim one more lap with Dolphin and then say goodbye."
    jump whatever
    
## Dolphin DATE 2