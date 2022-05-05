﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define name = Character("[name]")
define pumpkin = Character("Pumpkin")
define meow = Character("Meowricio")
define coco = Character("Coco")
define jerry = Character("Jerry")
define doug = Character("Doug")
define snow = Character("Snow")
define catbot = Character("Catbot")

# just for funny
define e1 = Character("Employer 1")
define e2 = Character("Employer 2")
define e3 = Character("Employer 3")

#points system
default cyberpoints = 0


# The game starts here.

label start:
    $ name = renpy.input("What's your name?", "Catya", length=15)
    "[name]! I love that!"

    # add in character selection here. Need the assets.

    catbot "Hi there! My name is Catbot!"

    catbot "I’m the friendly virtual assistant living in your phone. I’ll show up occasionally to help you along the story."

    catbot "Would you like me to explain how this game works?"

    menu:
     "Yes":
        menu:
            "In this game, you make choices like this:"

            "Ok":
                name "Ok"
            "Woah":
                name "Woah"
        catbot "These choices will be related to cyber security and digital literacy."
        catbot "Don’t worry if you make “wrong” choices. Every choice you make is a learning opportunity!"
        catbot "And even if you make a “wrong” choice, you can always go back and select a different choice!"
        catbot "In addition to these choices, there will be fun minigames along the way!"
        name "Cool! I’m ready!"
        catbot "Let’s start!"
        pass


     "No":
         catbot "Okay! Let’s start meow!"
         pass

    "Ah, Kitty City. The land of opportunities, fresh fish, and of course…high rent."

    "My name is [name]. I’m just a small-town cat with big dreams."

    "I moved here to go to college for a degree in Biology but since graduating, I’ve been having trouble finding a job."

    "I had a couple of interviews but here’s how most of them went:"

    e1 "Knowing about the Krebs cycle won't help you here…"

    name "Why not?"

    e1 "This is a bank..."

    name "Oh..."

    e2 "Sorry, but…the position has already been filled."

    name "Wait…then why am I here?"

    e3 "Who are you again?"

    name "[name]!"

    e3 "Oh I think I invited the wrong cat to interview. Sorry haha."

    "I guess it doesn’t help that I don’t have much work experience."

    "But how do I get work experience without getting a job? Ugh."

    "Oh well. At least my aunt was nice enough to pay me for babysitting her daughter."

    "Speaking of which…what is she doing on my computer?"

    name "Hey Coco, what are you doing?"

    coco "Yo, [name]. Have you ever heard of Meowcube?"

    name "Yes. It’s that game where everything is a cube right?"

    coco "Well you can also adventure and dress up your character but you’re old so I don’t expect you to understand."

    name "Hey!"

    coco "Anywaaay. Someone messaged me and they told me that if I give them my login information, they can get me 10000 Meowdollars."

    name "Wow…is that a lot?"

    coco "Ohohoh! You have no idea! 10000 Meowdollars can get me the limited edition super rare rainbow turbo boosted unicorn pet!"

    name "Wow, Coco…"

    menu:
        "This sounds like a scam!":
            name "I don’t think you should do it."

            coco "Huh? Why not?"

            name "It’s too good to be true, Coco. There’s a good chance that they just want to steal your login info."

            coco "And I won’t get my Meowdollars?"

            name "Nope."

            coco "Then what should I do?"

            menu:
                "Ignore it":
                    name "You should just ignore them. You should never share your login information with anyone."

                    coco "But what if they do it again? I think I should report them. I don’t want them to hack my friends."

                    name "That’s a good idea, Coco."

                    catbot "Hi, [name]."

                    catbot "It’s a better idea to report the situation and ignore any links or requests from the scammer."

                    name "Got it."


                "Report it, block them, and don’t send them any information":
                    name "You should report them, block them, and make sure to not send them any information or click on any links they send you. You should never share your login information with anyone."

                    coco "Okay…fine. I guess you’re right."

                    catbot "That was a good call, [name]! Things that are too good to be true usually are! It is important to not share your login information with anyone-- especially strangers on the internet!"

                    $ cyberpoints += 1


                "Insult them":
                    name "Are you kidding me? You should insult them! How dare they scam children!"

                    coco "Ohohoh. They have no idea what’s coming for them."

                    catbot "Hey [name]. It’s a better idea to report the situation and ignore any links or requests from the scammer."

                    name "I see."

                    "10 minutes later."

                    coco "Waaaah!"

                    name "Oh no! What’s wrong?"

                    coco "They called me names! And! And! They threatened that they would come find me if…if I don’t send them my login info."

                    name "Coco…I think you should report them, block them, and do not talk with them any further. You should never share your login information with anyone."

                    coco "Okay…okay…"

        "You should totally do it!":
            name "That’s amazing! You should do it!"

            coco "Right? It’s awesome!"

            "Five minutes later…"

            coco "Waaaah!"

            name "What’s wrong?"

            coco "I lost all my items!"

            name "Oh no! I think they might have been a scammer! Sorry."

            coco "What do I doooo?"

            menu:
                "Change your login information":
                    name "You should change your password so they can’t login again. If the password is the same as your email’s, change it too."

                    coco "*sniffle* Okay."

                    catbot "Good choice. If you do end up giving away your login information, make sure to change your password!"

                    $ cyberpoints += 1

                "I don’t know":
                    name "I don’t know, Coco. Maybe you can make a new account?"

                    coco "I don’t wanna make a new account! I’ll lose all my progress!"

                    name "That’s fair…maybe it’s better if you change your password. That way you can save your progress."

                    coco "Wow. That’s actually a good idea…I’ll do that."


    pass

    "After Coco took care of the Meowcube problem, she went to take a nap."

    "*Ding*"

    "Phone reminder: Rent is due in 14 days."

    name "Right…rent is due soon. I don’t think babysitting money is going to be enough to cover it. I hope I hear back from a job soon…I desperately need it."

    name "Ughhh"

    "Right as I was about to get up…"

    "*Ding*"

    name "An email?"

    "Dear, [name],

    After carefully going over your application and reviewing your interview, we would like you to invite you to work with us at Phish n’ Chips Inc. as an intern.

    Please reply as soon as you are available.

    Best,

    Pumpkin
    CEO"

    name "Ohmygosh! Ohmygosh! This can’t be happening."

    "A grin spreads across my face. I would have screamed for joy if Coco weren’t sleeping."

    menu:
        "Reply to email":
            "Dear Pumpkin,

            I would love to work for you! When do I start?

            Best,

            [name]"

            pass

    "*Ding*"

    "Splendid! Training starts tomorrow at 9am. Please bring your laptop and your enthusiasm.

    Cheers,

    Pumpkin
    CEO"

    name "Things are finally going my way!"

    "I cannot wait for tomorrow."

    "I have to tell my best friend."

    # !!! here we would have to add in a phone

    name "Meowricio!"

    meow "Oh hey, [name]! What’s up!"

    name "Guess who is employed?"

    meow "YESSSS! Give me all the details!"

    name "It’s at Phish n’ Chips."

    meow "Phish n' Chips? What do they do?"

    name "They manufacture computer chips!"

    meow "Ohhh! Right. I’ve heard of them!"

    meow "When do you start?"

    name "Tomorrow!"

    meow "Awesome!! You’ll do great!"

    name "Thanks, Meowricio :)"

    meow "fknknal.ca/isthisyou?"

    menu:
        "Click on the link":
            "I click on the link and instantly get logged out of my account."

            name "What’s going on?!"

            "After logging back in."

            meow "Hey! Sorry about that! I think I got hacked! You didn’t click the link…did you?"

            "I checked my messages…the link was sent to my other friends as well…"

            name "Oh no! Oh no!"

            catbot "Beware of random links! They could get you hacked or steal your information! You can see where they lead to by hovering over them or using a link scanner."

            name "What should I do?"

            menu:
                "Only delete all the messages":
                    catbot "Close! If you get hacked, change your password immediately and delete all those messages with the links! Let your friends know that you’ve been hacked!"

                    name "Thanks! I’ll do that."


                "Panic":
                    "I scream."

                    name "Oh no! Oh no!"

                    catbot "Hey [name]! Let’s take it one step at a time. If you get hacked, change your password immediately and delete all those messages with the links! Let your friends know that you’ve been hacked!"

                    name "Thanks! I’ll do that."

                "Change your password and delete all the messages with the links":
                    catbot "That’s right! If you get hacked, change your password immediately and delete all those messages with the links! Let your friends know that you’ve been hacked!"

                    name "Thanks! I’ll do that."

                    $ cyberpoints += 1

        "What is this?":
            name "What’s this link?"

            meow "Oh noes! DON’T click on it! I think I got hacked."

            meow "Ahhhh! What should I do?"

            menu:
                "Only delete all the messages":
                    catbot "This answer could be better. If you get hacked, change your password immediately and delete all those messages with the links! Let your friends know that you’ve been hacked!"

                "Change your password and delete all the messages with the links":
                    catbot "That’s right! If you get hacked, change your password immediately and delete all those messages with the links! Let your friends know that you’ve been hacked!"

                    name "Meowricio! You should change your password. Then, delete all those messages and let everyone else know that you got hacked."

                    meow "Meow! You’re right! What would I do without you?"

                    $ cyberpoints += 1


    "Phew. That is settled. Now it is time for bed."

    "The next day."

    name "Phish n’ Chips…This must be it."

    # scene change

    "The scent of coffee and fish wafts through the air."

    "A group of cats sitting at a small rectangular table. There’s only 5 cats here…including me. Is this the entire team?"

    "At the head of the table, I see a fluffy orange cat in a suit and tie. That must be Pumpkin!"

    name "I guess I should sit down."

    "I sit down next to a timid-looking cat and a…strange looking cat."

    "The orange cat clasps their paws together and grins when I arrive."

    pumpkin "Hi [name]! So glad that you could make it! I’m Pumpkin."

    "I shake paws with Pumpkin."

    pumpkin "Everyone! Let’s go around and introduce ourselves."

    "An elegant cat in pearls raises her paw."

    snow "I’m Snow. I’m the Vice President of Phish n’ Chips."

    "I shake paws with Snow."

    "The nervous cat beside me goes next."

    jerry "H-hi. I’m J-jerry."

    "I offer my paw to shake but Jerry fist bumps it instead."

    jerry "O-oh my bad…s-sorry."

    name "All good…"

    snow "You have to say your role too, Jerry."

    jerry "I-I’m the supply manager. I also do m-maintenance on the machines."

    "The strange looking cat beside you goes next."

    doug "I’m Doug. I’m the security manager."

    name "Nice to meet you."

    "Doug does not shake my paw."

    pumpkin "Whoopee! It’s so nice to see a fresh face around here. [name], you will be working mainly with Jerry and Doug for your internship."

    snow "Here’s a To-Do List to help you get started."

    # (add something to screen with todo list)

    snow "You can follow me to your office space."

    "I follow Snow to a room with 3 cubicles. She points to one nearest to the door."

    snow "Okay, newbie. You can work here. Let me know if you need anything."

    name "Okay, thanks Snow."

    "Let’s do our first To-Do…"

    # [Set up wifi game]

    "Nice! Now that I have my wifi secured, I can do To-Do number 2!"

    # [Account set-up game]

    name "Nice! I have my new account! Now all I need to do is…"

    "My laptop screen blacks out."

    name "Oh no!"

    "There aren’t any other computers here either. I guess they only manufacture computer chips…"

    "I could ask Snow."

    menu:
        "Ask Snow for a charger":
            "I wander out and see Snow writing things down on a clipboard."

            name "Hi Snow! I was wondering if I could borrow a charger for my laptop!"

            snow "Oh. Is your laptop out of battery? I don’t carry chargers on me but maybe you can ask Doug. He’s working in the cubicle next to you."

            name "Sounds good. Thank you."

            snow "By the way, when you are setting up a password, don’t forget to turn on multi factor authentication."

            name "Why is that?"

            snow "It sets up an extra layer of protection. If someone got your login information, the multifactor authentication could stop them from actually accessing your precious data!"

            name "Got it, thanks."

            pass

    "I go back into the office and just as Snow said, Doug is sitting in a cubicle."

    "When did he get in here? Anyway, let’s see if he has a charger."

    name "Hey Doug, do you have an extra charger? My laptop died and I need to…"

    doug "Check emails, woof? I mean meow…"

    "Doug takes one look at my laptop and shakes his head."

    doug "My laptop’s a different brand from yours."

    name "Oh no…"

    doug "But you’re in luck, buddy. I brought a spare laptop that you can borrow."

    name "Awesome! Thanks!"

    "Doug points to a dark room."

    doug "I set my laptop up over there woof. I mean meow. Just be careful when you login...there might be some cybersecurity risks in there that you need to take care of first."

    # [Click on all the cyber security hazards game]

    doug "Well done. Here you go."

    "I turn on the laptop and get to the login screen."

    # [A screen where you login and you cannot proceed unless you click on the “do not remember password” check mark]

    # Catbot (if they don’t check it): Don’t forget to click on the do not remember password button! If Doug has your login saved, he can access your information!

    # [The email game; you have to remember to LOGOUT in order to end the game]

    doug "Hey, [name]. Are you done with your emails?"

    name "Yeah! Thanks for letting me borrow your laptop, Doug!"

    doug "No problemo. Did you log out?"

    name "Yep."

    doug "…Good. I think Jerry might have a task for you."

    name "What task?"

    doug "I don’t know. Something about research and files. I’m too busy right now so maybe you can help him out. He’s in the supply room."

    name "Okay."

    # scene transition

    jerry "Oh h-hey, [name]."

    name "Hey, Jerry. Doug said you needed help?"

    jerry "Y-yeah! I am trying to find this really good software b-but it’s out of our company’s budget…"

    jerry "I found this site that is offering a free download of it. I-I wanted your opinion on it."

    name "Jerry…"

    menu:
        "Don’t do it":
            name "Jerry, it’s not worth it. There’s a chance that the files could contain viruses or malicious code."

            jerry "W-what type of malicious code?"

            name "There could be spyware or Trojans!"

            jerry "Oh I-I’ve heard about Trojans! They can steal data and create backdoors in our computer. My b-brother got his banking information stolen because of some s-shady code that was in the file."

            name "Yeah…let’s not download that file. We can probably find a free and safe alternative to that paid software."

            jerry "Y-you’re right!"

            $ cyberpoints += 1

        "Do it":
            name "Free software is good software. I think you should download it."

            jerry "I a-agree."

            "After the file finishes downloading, Jerry’s screen freezes."

            jerry "O-oh no! What’s happening?"

            catbot "Be careful when downloading files on the internet! Downloaded files might contain viruses or malicious code. This could mean spyware and Trojans designed to steal data or create backdoors in the computers."

            jerry "I-I should have updated my firewall."

            name "Sorry, Jerry…"

            jerry "It’s okay…I’ll just cry…I’ll ask Doug for help…"

            jerry "H-he’s a good cat. Very reliable. Very cat-like."

    jerry "A-anyway…I-I think it’s home time for you right?"

    name "Oh yeah, you’re right."

    jerry "B-bye…"

    name "Bye, Jerry."

    "Back at home…"

    "I still have some assignments on the To-Do List."

    "Looks like I need to do some research on clients."

    # [Traversing the web (add in something about secure and insecure networks). A puzzle game where you have to get through all the right doors]

    "Nice. I compiled everything into a zip file. Now I just need to send it over…"

    "*Ding*"

    pumpkin "[name]! How was your first day?"

    name "It was fun! I learned a lot."

    pumpkin "I’m glad to hear! Can you send over the research file?"

    name "Yeah sure! Where should I send it?"

    pumpkin "You can just send it over text."

    "Hmmm. The file contains confidential information…"

    menu:
        "Send it through text":
            "Right when I am about to send the file to Pumpkin’s number…"

            catbot "Woah woah woah! SMS messages are not secured or encrypted! They could be intercepted by hackers! This is dangerous-- especially for sending confidential information!"

            name "Oh no! What should I do instead?"

            catbot "You can attach the file to an encrypted email. It’s safer that way."

            name "Okay! I’ll do that."

            catbot "Do you have any questions?"

            menu:
                "What does encrypted mean?":
                    name "What does encrypted mean?"

                    catbot "Encrypted means that the message you send will be unreadable to unwanted eyes! Only authorized cats that have a secret code can read your message."

                    name "I see! Thanks, Catbot!"

                    catbot "I got you."

                    catbot "Anyway, I’ll leave you to it."

                    "After encrypting the email…"

                    catbot "Nice work!"

                "Nope":
                    catbot "Okay. I’ll leave you to it."

        "Send it through email":
            name "I’ll send it through email."

            pumpkin "Whatever works for you."

            catbot "Don’t forget to encrypt the email! That way, if your email gets intercepted, cats that aren’t supposed to see your files won’t be able to understand them!"

            name "Gotcha."

            "After encrypting the email…"

            catbot "Nice work! Encrypting files-- especially confidential ones, is important."

        "Suggest encrypting the files before sending it through email":

            name "I’ll send it over to your email."

            pumpkin "Okie dokie."

            "After encrypting the email…"

            catbot "Nice work! Encrypting files-- especially confidential ones, is important. That way, if your email gets intercepted, cats that aren’t supposed to see your files won’t be able to understand them!"

            $ cyberpoints += 1

    pass

    "Finally…I am done with my tasks."

    "I wonder what tomorrow holds for me."

    "The next day…"

    "Pumpkin is pacing around the office."

    "They seemed worried."

    name "Pumpkin? What happened?"

    "They stop and walk over to face me."

    pumpkin "[name]. I’m sorry but…there was a data breach. A lot of our information got exposed."

    pumpkin "Our investors are mad, [name]. Our customers are mad. Our stock prices are crashing!"

    "They shake their head."

    pumpkin "Unfortunately, we have to let you go."

    "I am dumbfounded. I’ve only worked one day."

    name "How are you going to respond to the breach?"

    pumpkin "Doug…is working on containing it. He’s assessing the risks…and letting the relevant cats know what has happened."

    pumpkin "If we didn’t have to shut down…he’d also make sure it wouldn’t happen again…"

    pumpkin "Waaah! This has never happened before!"

    "Pumpkin sobbed and blew his nose into a tiny handkerchief."

    pumpkin "Anyway…you should pack up…"

    name "Yeah…I guess so…"

    # [Cleaning minigame]

    name "Hey, Pumpkin…are you going to be alright?"

    pumpkin "Yeah…sorry your internship had to end so suddenly…"

    if cyberpoints == 3:
        jump good

    else:
        jump bad

    label good:
        pumpkin "But! Don’t worry."

        "Pumpkin hands me a business card."

        pumpkin "I’ve sent you a referral to this fishing company. I think they’d be happy to hire you."

        name "Thanks! And uh…sorry."

        pumpkin "No…it’s okay. We’ll figure it out."

        pumpkin "Bye now."

        "A few days later…"

        "Kitty City. The land of opportunities, fresh fish, and rent that I can afford."

        "I learned a lot that day at Phish n’ Chips."

        "There are some bad cats out there! As long as the internet exists, there are going to be risks."

        "But by learning how to reduce those risks…"

        "By being cyber smart…"

        "I feel more ready to navigate my new job and the internet!"

        "Congratulations! You got the good ending!"

        "Feel free to play again to see how other choices impact the story!"

        # can insert fishing game here

        return

    label bad:

        "At home."

        name "Ughh. What do I do now?"

        "Kitty City. The land of opportunities, fresh fish, and rent that I can’t afford."

        name "I think I’ll have to work on my digital literacy skills…"

        "Meow! You got the bad ending!"

        "That’s okay!"

        "Feel free to play again to see how other choices impact the story!"

        return

    

     # scene transition







    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.



    # This ends the game.

    return
