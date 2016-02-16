## Elephant Date 1

label elephantdate1
	show bg savannah day
		"Far away you can see an Elephant gazing into the distance."
		"You approach him. It quickly becomes clear that he wasn't far away."
		"He's just very small."
	show elephant normal
		e "Oh, a human."
		"He looks away, sighing."
		e "I suppose you've come to me looking for love."
		e "Alas... you're too late."
		menu:
			"Too late?!?"
				jump elephantdate1_Pass
			"Actually I was looking for a bathroom..."
				jump elephantdate1_Fail

label elephantdate1_Pass
		e "Yes, my heart belongs to another."
		e "Ah... that silver skinned temptress."
		e "Her golden eyes gaze into my very soul."
	show elephant angry
		e "But does she love me in return?"
		e "I cannot read her heart if she will not answer my letters."
		"Elephant throws a bundle of papers to the ground."
		"They're all letters adressed to 'M'"
		menu:
			"Let me deliver these for to you."
				jump elephantdate1_Choice2_Pass
			"Yeah you should probably dump those."
				jump elephantdate1_choice2_Fail
label elephantdate1_Choice2_Pass
	show elephant normal
		e "You... you, a stranger, would help me fulfil my heart's desire?"
		e "Yes! If you can make sure she reads them..."
		e "Please human!"
		e "She can be found by the entrance at night."
		e "Tell her how I feel..."
		"Elephant disapears into the distance"
		"Wow, he's written a LOT of letters."

label elephantdate1_Fail

		e "ah..."
		e "It's to... the left"
		"Somehow Elephant manages to fade into the distance?"
		"Well, time to go pee."

label elephantdate1_choice2_Fail
		e "I suppose you're right..."
		e "Please... leave me, I need to be alone for a while..."


## Elephant Date 2 Minus Elephant

	show bg enterance night
		"You approach the entrance of the zoo."
		"There doesn't seem to be anyone here."
		"You look around. The only thing you see is..."
	show mercedes blush
		"A car."
		"... silver skin..."
		"... golden eyes..."
		"You examine the front of the car..."
		"It's a mercedes."
		"'M'."
		"How... HOW DO YOU DELIVER A LOVE LETTER TO A CAR?!?!?!"
		menu
			"This is stupid."
					jump elephantdate2_Fail
			"LOVE WILL PREVAIL"
					jump elephantdate2_pass

	label elephantdate2_Fail
			"This isn't worth it."

	label elephantdate2_pass
		"Well, even if it is an inanimate object, maybe it can still love?"
		"Where can you stick these letters?"
		menu:
			"The engine"
				jump elephantdate2_Engine
			"The glove compartment"
				jump elephantdate2_glove
			"The Tail Pipe"
				jump elephant2_tailpipe
	label elephantdate2_Engine
		"You consider putting the letters inside the hood of the car."
		"The engine is sort of the heart of a car right?"
		"Then you remember that engines are very hot, and paper is very flamable."
		"Better put them in the glove compartment."
			jump elephantdate2_glove

	label elephantdate2_tailpipe
		"You consider putting the letters inside the tailpip."
		"But that's gross and will definitely blow up the car."
		"Better put them in the glove compartment."
			jump elephantdate2_glove 

	label elephantdate2_glove
		"Luckily the car is unlocked."
		"You open the side door and the glove compartment and tuck the letters inside."
		"One falls out. You look at it."
		"WOW..."
		"Oh wow. You didn't know you could do that with a trunk."
		"Jeez. Elephant is very... explict."
		"Also his spelling is terrible."
		"You quickly leave the scene of the confession."
	label elephantdate2_Fail 
		"This is stupid."
		"You swear to never help out love struck pachyderms again."

## Elephant Date 3
	label elephantdate3
		"Elephant is waiting for you."
	show elephant blush
		e "How did it go?! What did she say?!?!"
	show elephant normal
		"He coughs."
		e "I mean, has she made her feelings clear?"
	menu: 
		"Crystal Clear."
			jump elephantdate3_choice1_clear
		"She's a car."
			jump elephantdate3_choice1_Car
	label elephantdate3_choice1_Car
		e "A car? no my friend, I'm afraid you're mistaken."
		e "She's the most beautiful elephant I have ever laid my eyes on."
			jump elephantdate3_choice1_Pass

	label elephantdate3_choice1_clear
		e "I would expect nothing less from one so beautiful."
			jump elephantdate3_choice1_Pass

	label elephantdate3_choice1_Pass
		e "I must know- no I'm too afraid to find out-"
		e "But I can't live in suspense forever..."
		e "WHAT DID SHE SAY?!"
	menu: 
		"She feels the same way."
			jump elephantdate3_choice2_Fail

		"She's. A. Car."
			jump elephantdate3_choice2_Car

	label elephantdate3_choice2_Fail
		show elephant blush
		e "I-I-I-I REALLY?!?!"
		"Elephant's swooning, best to move out of the way."
		e "I can't believe someone that wonderful would feel the same."
		e "Thank you cutie! You've made me the happiest elephant in the world!"
		"He runs off into the distance."
		"You don't know if lying to the elephant was the best option, but surely it can't hurt."

	label elephant date3_choice2_Car
		show elephant angry
		e "I can't believe you're persisting with these lies!"
		e "I thought we were friends, yet you insist on such cruelty."
	menu:
		"Sorry, my mistake she totally loves you."
			jump elephantdate3_choice2_Fail

		"She has headlights! And doors! And a PLUSH LEATHER INTERIOR."
			jump elephantdate3_choice3_Car
	labe elephantdate3_choice3_Car
		"You have stunned Elephant into silence."
		"..."
		"..."
		"He starts muttering to himself."
		e "... this explains so much."
		e "Even if she is a car... I still love her."
		"VROOOM!"
	show mercedes blush
		"Seriously?!"
		m "Vroom Vroom Vrooooooooooom!"
		"The car reves her engine."
		e "It's you! The woman of my dreams."
		"She's a car. She's definitely a car."
		m "Vroom vroom vroom."
		e "You read my letters!"
		m "Vrrroooooooooom."
		e "You loved my letters!"
		m "Vrooom vrooom vrooooooom."
		e "You love me!!!!"
		"Somehow you're not at all surprised."
		e "Cutie! You did it! You united me and my love. But..."
	show elephant blush
		e "I find my heart has love enough for another."
		e "Will you join us in a menage a trois of love?"
	menu:
		"Three's a crowd"
			jump elephantdate3_choice4_NoLove
		"Three's company too."
			jump elephantdate3_choice4_Love

	label elephantdate3_choice4_NoLove
	show elephant normal
		e "I understand my friend. We will never forget your kindness."
		m "Vroom!"
		"Elephant and his beau drive off into the sunset."
		"Or rather he runs after her as she drives into the sunset."
		"That is a very fast car."

	label elephantdate3_choice4_Love
		e "My loves! You have made me the happiest elephant in all the zoo!"
		m "Vroom!!"
		"You drive off into the sunset with your new lovers."
		"Or rather they drive off and you run after them."
		"That is a very fast car. "