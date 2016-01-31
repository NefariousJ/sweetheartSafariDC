## Snake DATE 1

label snakedate1:
    sn "Psss, you think you're bad as me?"

    scene bg forest day
    with fade
    show snake normal
    with dissolve

    sn "The tall grass hides me from my prey."
    sn "I just lie in wait until…"
    sn "PSSSS!!!"
    sn "I jump out and strike!"

menu:
    "You kill them?!":
        jump snakedate1_choice1_kill
            
    "That's pretty badassss.":
        jump snakedate_choice1_badass
        
label snakedate1_choice1_kill:
    sn "Nah, I usually let them go."
    sn "Every other animal in here is bigger than I am…"
    jump snakedate1_choice2
        
label snakedate_choice1_badass:
    sn "Oh, you think sssso?"
    sn "PSSS!!"
    sn "I'm glad someone agreesss."
    jump snakedate1_choice2
        
label snakedate1_choice2:
    sn "It'sss hard for a bad ssnake like mysself to fit in."
    sn "The other animalss are sso sself-important."
    sn "Alwayss thinking of themsselvess, never inviting me to partiesss…"
    
menu:
    "The others treat you badly?":
        jump snakedate1_choice2_treat
            
    "I'm sssorry to hear that.":
        jump snakedate1_choice2_sorry
        
label snakedate1_choice2_treat:
    sn "Who needss them, anyways?"
    sn "I'm all about that bad boy lifestyle."
    sn "Sssnakesss!"
    "Snake tries to throw up a gang sign without arms."
    "…It doesn't work out."
    jump snakedate1_choice3
        
label snakedate1_choice2_sorry:
    sn "Are you teassing me?"
    sn "That's pretty sssneaky. I like that."
    jump snakedate1_choice3
    
label snakedate1_choice3:
    sn "I've been thinking about recruiting a new gang member."
    sn "Ssomeone who'ss loyal and bad to the bone!!"
    sn "Ssomeone who can shake off hatersss like they're shedding sskin!"
    
menu:
    "That'ss me!":
        jump snakedate1_success
        
    "Sssorry, not interested.":
        jump snakedate1_failure
        
label snakedate1_success:
    sn "Really? That'sss sssuper."
    sn "Let'sss exxchange cccell numberss."
    "You ssspend the resst of the afternoon sssmoking with Snake."
    jump whatever
    
label snakedate1_failure:
    sn "I knew it. You're jussst like the otherss."
    sn "Looks like there's more than one ssnake in the grasssssss."
    "Snake sssliters off."
    jump whatever
    
## Snake DATE 2

label snakedate2:
    sn "I'm sso glad you can ssspare ssome time to ssee me."
    
    scene bg savannah day
    with fade
    show snake normal
    with dissolve
    
    sn "There they are. Thossse jerksss."
    sn "Hippo, Giraffe, and Elephant: The Biggest Jerks In The Animal Kingdom."
    sn "Ssometimes I wish they'd dissappear."
    
menu:
    "What happened?":
        jump snakedate2_choice1_happened
        
    "Let'ss get 'em":
        jump snakedate2_choice1_getem
        
label snakedate2_choice1_happened:
    sn "They alwayss ignore me."
    sn "A ssnake like me, sslithering in the grass…"
    sn "No one bothers to even watch where they're ssstepping."
    jump snakedate_choice2
    
label snakedate2_choice1_getem:
    sn "Ha, if only. I'm not ass tough as I look…"
    jump snakedate_choice2
    
label snakedate_choice2:
    sn "I have a bit of a confession to make, Cutie."
    sn "You sssee…or rather, you see…"
    sn "I don't actually have this ridiculous hissing accent."
    sn "…And I'm not all that tough either."
    sn "I put it all on as an act, because I'm afraid of others."
    sn "Who could accept a lonely, slithery snake like me?"
    sn "I keep trying to shed my skin, but in the end I can't change who I am deep down."
    sn "Issn't that ssssssssad?"
    
menu:
    "I ssssstill think you're pretty tough.":
        jump snakedate2_success
    
    "Sssssucksssssss to be you…":
         jump snakedate2_failure
         
label snakedate2_success:
    sn "That'ss kind of you to ssay."
    sn "Ha, when I get flusstered my acccccent comessss back."
    sn "I guessss I'm pretty nervousss to be around you ssssometimess…"
    sn "…"
    sn "…What?"
    sn "Sssstop sstaring at me, I'm getting embarasssed…"
    "You wrap Snake around your neck and pull him in for a slithery smooch."
    sn "Sssssay…that'sssss not bad."
    sn "Hope you don't mind tongue…"
    "You and Snake sssslither around for a while."
    jump whatever
    
label snakedate2_failure:
    sn "Are you serious?"
    sn "I shed my layers in front of you and all you can do issss mock me?"
    sn "A bad boy like me doesssn't have to put up with thisss."
    sn "I'm out of here."
    "Snake sslithers away."
    jump whatever
    
## Snake Dates OVER