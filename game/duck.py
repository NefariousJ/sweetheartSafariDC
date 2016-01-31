## Duck Date 1
scene bg enterance day
	"That fence looks like a solid place to lean and chill."
menu:
	"Lean and chill"
	jump to duckdate1
	"Nah."
jump mainmenu

label duckdate1
	"You lean on the fence like the hella cool high school student you are"
	"Sure you should be romancing some animals so you can escape"
	"But there's always time for looking cool"
	"Wait you're looking so COOL someone sidles up to you."
show duck normal
	d "Howdy ho cutie. Do you know where I could get some dopealicious"
show duck angry
	d "QUACK"
show duck normal
	"..."
	"Did that duck just quack or ask you for drugs?"
menu 
	"Quack is wack"
		jump duckdate1_choice1_drugsarewack

	"Do you mean... crack?"
		jump duckdate1_choice1_drugsarequack

label duckdate1_choice1_drugsarewack
	d "Drugs are mega cool"
		jump duckdate1_choice2

label duckdate1_choice1_drugsarequack
	d "Are you making fun of me or something?"
		jump duckdate1_choice2
label duckdate1_choice2
	d "After a long day I just want to do some"
show duck angry
	d "QUACK"
show duck normal
	d "ya feel doggo?"

menu:
	"Friendship is my antidrug"
		jump duckdate1_choice2_antidrug
	"Oh I feel alright"
		jump duckdate1_choice2_Ifeel

label duckdate1_choice2_antidrug
	d "You have a will of iron."
	d "If you find some, you know where to find me."
	"Wait, didn't she find you?"
	End duckdate1

label duckdate1_choice2_Ifeel
	d "Yes! You'll show me where to get some..."
show duck angry
	d "QUACK"
show duck normal
	d "later right?"
	d "That'd be super hip."
	"She leaves before you can tell her you have no idea how to get quack."
	"... or what quack is supposed to be."
	Set $drugs to true
	End duckdate1

### Duck Date 2 

scene bg enterance day

	"Look it's your favorite leaning fence."
	"Maybe you should do some more leaning."
	"Surely that weird duck won't come back."

menu: 
	"Be cool"
		jump duckdate2
	"Don't be cool"
		jump mainmenu

label duckdate2
	"Just gettin' in some nice relaxation time-"
	"Aw man it's that duck again"
show duck normal
	d "Hey cutie, you got any..."
show duck angry
	d "QUACK"
show duck normal
	if $drugs is true
	d "So are you going to show me some"
show duck angry
	d "QUACK"
show duck normal
	d "Cutie?"
menu:
	"Actually I lied..."
	jump duckdate2_choice1_lies

	"Right this way!"
	jump to duckdate2_thisway

	else
	d "Did you find some?"
menu:
	"Just say no"
	jump to duckdate2_choice1_no

	"Yeah there's some right this way"
	jump to duckdate2_thisway

label duckdate2_choice1_lies
	d "You lied... oh, I see."
	d "So you don't have any..."
	d "Well, I'm sure you'll find some."
	jump duckdate2_choice2

label duckdate2_choice1_no
	d "But everyone enjoys it!"
	d "We should try some! Do you know where I can find some?"

menu:
	"I DON'T HAVE ANY 'QUACK'"
	jump duckdate2_choice2_NoQuack

	"Yes fine let's get some quack"
	jump duckdate2_thisway

label duckdate2_thisway
	"You lead her around the zoo."
scene bg cafe day
	"To the cafe..."
scene bg pool day
	"To the pool"
scene bg space day
	"Even up into outerspace"
scene bg enterance day 
	"After 3 hours she finally realizes you're leading her nowhere..."
	END Failstate

label duckdate2_choice2_NoQuack
	d "..."
	d "..."
show duck cute 
	d "okay"
	"She leaves with a light flush on her cheeks."
	"What a weird bird."
	Date End

## Duck Date3

label duckdate3
	"You decide to fit a bit more hella cool fence leaning in."
	"Wait, there's someone in your spot."
show duck normal
	d "Hey... cutie can we talk?"
	"This seems suspicious but okay..."
	d "I want to tell you the truth."
	d "I don't actually want any"
show duck angry
	d "QUACK"
show duck normal
	d "I'm actually part of an undercover cop program"
	d "21 flap street"
	d "We've been putting undercover cops in zoos all around the country"
	d "My cunning disguise was good. But perhaps it was too good."
	d "At first I was just trying to use you to find the source but..."
	d "No matter how hard I tried you never gave in."
	d "Your iron will is just so..."
	d "attractive."
	d "Tell me cutie... do I have a chance?"
menu:
	"My antidrug... is you."
		jump duckdate3_LoveEnd

	"I can't believe you'd lie like that..."
		jump duckdate3_RejectionEnd

label duckdate3_LoveEnd
	d "Really cutie! I can't believe it."
show duck cute
	d "Come here..."
	"You spend a long time with duck, you're still picking the feathers out of your clothes later."
	End duckdate3_LoveEnd

label duckdate3_RejectionEnd
	d "I understand. My alterego was very convincing..."
	d "I'll always wonder, what might have been"
	"She leaves, dejected. Thank goodness."
	End duckdate3_RejectionEnd
