﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define p = Character("[name]")
define r = Character("Rohit")
define n = Character("Narrator")

define g1 = Character("g1")
define g2 = Character("g2")
define g3 = Character("g3")


# The game starts here.
# p is the player

label start:

    $ confidence_meter = 25

    n "Hi, welcome to our humble game. Before you begin please tell us your name."

    python:
        name = renpy.input(_("What's your name?"))

        name = name.strip() or __("Lord Voldemort")

    n "Hi great thanks for joining us on this journey [name]"
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene pub2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # show m1 image neutral
    with fade

    p "And here we are celebrating my friend Rohit's work anniversary"    

    r "Hey man why so serious? Its been such a hectic couple of months and I just want to relax today."

    p "(nervously) Hey I am really happy for you,its just I dont like being with so many people."
    
    r "Come on, Loosen up. What the ..."
    
    # show m1 image blush

    with fade

    p "What happened ?"
    
    r "OMG!!! I dont believe it ?"
    
    p "(shaking) What???  "
    
    r "G1,G2 and G3 all together. Wow they must be having some sort of reunion together."
    
    p "How do you know them? "

    r "Oh we were in school together. I wasnt close to them but knew them well."

    r "Come lets catch up with them."

    p "What? No No. What will i do, i dont even know them."

    r " Arre why are you so concerned?" 
  
    p " (stuttering) I have avoided all humanity uptill now and you want me to talk to 3 beautifull girls."
    
    # > Hero shaking. Depict by bluring the screen or something  

    n "So Rohit pulled me and I was totally uncomfortable"

    # show g1 neutral
    # show g2 neutral
    # show g3 neutral
    
    g1 "Hey Hey Hey!!!! Look who showed up"  
    g2 "OMG!!! Its been so long. How are you ???"

    r  "Oh not too bad. Is this some coincidence or were you guys always planning to catch me like this?? "
    g3 "Dont flatter yourself. Well we ran into each other the other day and decided to catch up properly. After all the stress is so high, our social lives have taken a collective dump."
    g1 "Hey is he okay ?"

    #  Panting. Can be depicted by some random transition of scenes, moving the characters

    n  "Suddenly, Rohit hits me"
    p  "Owww !"
    r  "Welcome back. Guys this is my friend Hero. We have been together since childhood. He is an engineer at XYZ company."    
    p  "(meekly) Hi !!"

    g1 "Oh my God, Relax man. We arent going to eat you. By the way I'm g1. I'm working to protect people like you.  "
    
    r  "(confused) Sorry ?"
    
    g1 "I mean I'm a corporate lawyer. Hehe "

    n  "That was a really poor joke."

    g2 "Well I'm g2. I am a school teacher"

    g3 "And you must already know me. I am the famous actress ...."

    p "Sorry I dont know you. But I feel I have seen you somewhere. "

    g3 "(tad angry) g3. Im in the UNESCO ad that everyone has been talking about. Gosh have you not followed my Instagram page alreadyyyyy."

    r "And that's dinner. I am really hungry. Anyone up for some starters."
    
    r "(pulling Hero closer), this is your chance."
    
    p "Seriously man, i'm sweating buckets here"

    r "Live a little buddy."

    label selectgirl:

        n " Which girl do you wanna talk to more ?"

        menu:
        
            "g1":
                jump g1_story

            "g2":
                jump g2_story

            "g3":
                jump g3_story


    label g1_story:

        $ played_music_minigame = False
        # show g1 neutral

        n "g2 , g3 and Rohit leave for starters"


        p  "Ummm  "
        g1  "Uhhh  "
        p  "(nervous laughter) Uhh  "
        g1  "Sorry. I must be boring you. uhh  "
        p  "No no not at all. I'm just not used to this.  "
        g1  "Well to be honest me too. He he  "
        p  "So what do you teach?? Arts?  "
        g1  "No I teach history to senior students "

        n  "How do you take this conservation forward."

        menu:
        
            "Wow. Must be a real headache keeping those teen ego's in check ":
                # n "Good Choice"

                # show g1 happy
                g1 "Yeah not many people realize how hard it is.  "
                p  "But I am sure it's rewarding.   "
                g1 "Yeah sure is. Always feel happy to see a successful student.  "
                p  "Yeah most important job in the world.  "

                $ confidence_meter += 10

                

            "Yeah you look the part. A typical History teacher. Not too smart. Ha Ha":
               
                # n "Bad Choice"
                
                # show g1 annoyed
                g1 "Well those who forget history are doomed to repeat it.  "
                p "Like reading pointless escapades of kings before. He He  "
                g1 "Its this exact reason for which I teach History.  "
                p "Well I hope you teach something real like Science.  "
                
                # jump bad_choice
                $ confidence_meter -= 5

            
            "Well you got it easy with the job. Personally the easiest job in history. Ha Ha":
                # n "Worst Choice"

                # show g1 angry/upset
                g1 "Well it's not as easy as it looks."
                p  "Really? Well all you have to do is look good and read from the book. No ?"
                g1  "Seems like you didnt have good teachers.  "
                p  "Well they dressed up well and read well so i guess they were pretty good."

                
                $ confidence_meter -= 10
        
        p  "Anyways you got any hobbies ? "
        g1  "Yeah I like cooking. I also like to watch bollywood movies."
        p  "Oh what is your favourite dish to cook ?  "
        g1  "I like to cook Gujrati food."
        
        menu:

            "Oh thats pretty lame. You should try more awesome things like pasta and burger.  ":
                
                g1  "Well to each their own. "
                p  "Anything not pasta is so stupid. Go for pasta only. "    
                g1  "(visibly annoyed).Hmm sure "

                $ confidence_meter -= 10
                # > Confidence hit. Show g1 angryp             
                
            "Wow thats actually interesting. I would love to know more.":
                
                g1  "Oh sure (visibly excited). Its very different to what you would find elsewhere.  "
                p  "Really how ?  "
                g1  "Well we like everything sweet. So you find a bit of sweetness in everything we eat.  "
                p  "Wow, that is different. The only sweet ive ever had is in form of ice cream. Would love to try sometime.  "
                g1  "Sure. Next time we meet,ill try to get something for you."

                $ confidence_meter += 5

                # > Show Dhwani excited. Confidence becomes little better


            "You mean dhokla and thepla. Yeah sweet just like you  ":

                g1  "(gets horny) Well you are not wrong about the food.   "
                p  "I actually like Gujrati food. I had some Gujarati friends in college.    "
                g1  "Wow can you speak gujrati then?.  "
                p  "Tārā māṭē kaṁīpaṇa.(Anything for you) "

                $ confidence_meter += 10

                #> Dhwani all red. Confidence skyrockets. Can show bit of shivering

        g1  "I love music , Come on let's go and do karoake"

        ## Flash_Back

        # Scene change - school event.

        n  "You suddenly had a flashback to your 7th grade annual function event."

        n  "You remember how you finally had the guts to go on stage and sing your hearts out, you had practiced and learnt all the lyrics."

        # Scene change - on stage public humiliation , people laughing two or three scenes.

        n  "But seeing the audience of over 500 , you forgot everything and ran away from the stage."

        n  "The jeering, taunts and bullying that you had to face the entire year. That was the year when you developed the stutter."
        
        # Scene change - present
        
        n "Do you still want to play the minigame."
        
        menu:
            
            "Yes":

                p "Let's do karoake"
                # scene - changes to karoake
                g1 "Go on it's your turn"

                call fifteen_game
                
                $ played_music_minigame = True

            "No":

                g1  "Come on don't be a spoilsport."
                p   "No I don't want to do karoake. I don't like it at all."

                $ confidence_meter -= 10

        n "The End"

        # good_choice:



        # bad_choice:

        # worst_choice

        


    # with hpunch
    # with blinds
    # with squares
    # with zoomin
    # with vpunch
  
    # label music_minigame:
    #     p "Let's do karoake"
    #     call simon pass (complete=8, toadd=2)

        
    # label pong_minigame:

    #     p "Let's play pong"
    #     jump play_game2

    # label play_game1:

        
    #     jump continue_game

    # label play_game2:

    #     call demo_minigame

    #     jump continue_game
        
    # label continue_game:


    # n "Your Score increased by 10"

    return
