# The script of the game goes in this file.

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


    show male smi01 with dissolve

    p "And here we are celebrating my friend Rohit's work anniversary"    

    r "Hey man why so serious? Its been such a hectic couple of months and I just want to relax today."

    p "(nervously) Hey I am really happy for you,its just I dont like being with so many people."
    
    r "Come on, Loosen up. What the ..."
    
    # hide male smi01
    show male smi02 with dissolve

    p "What happened ?"
    
    r "OMG!!! I dont believe it ?"
        
    p "(shaking) What???  " with hpunch
    
    r "G1,G2 and G3 all together. Wow they must be having some sort of reunion together."
    
    p "How do you know them? "

    r "Oh we were in school together. I wasnt close to them but knew them well."

    r "Come lets catch up with them."

    p "What? No No. What will i do, i dont even know them."

    r " Arre why are you so concerned?" 
  
    p " (stuttering) I have avoided all humanity uptill now and you want me to talk to 3 beautifull girls."
    # with Fade(5.0) zorder 10
    show blackflash zorder 50
    # > Hero shaking. Depict by bluring the screen or something

    n "So Rohit pulled me and I was totally uncomfortable"
    hide male smi02
    # show g1 neutral
    # show pink hair smile01 at left
    # show g2 neutral
    # show ros_akuwaraia1
    # show g3 neutral
    # show dark hair smi01 at right
    
    show pink hair smile01
    g1 "Hey Hey Hey!!!! Look who showed up"
    show pink hair smile01 at ph1

    show ros_akuwaraia1 with dissolve
    g2 "OMG!!! Its been so long. How are you ???"
    show ros_akuwaraia1 at ros1

    show male smi02 with dissolve
    r  "Oh not too bad. Is this some coincidence or were you guys always planning to catch me like this?? "

    show male smi02 at m1
 
    show dark hair smi01 at dh1 with dissolve
    g3 "Dont flatter yourself. Well we ran into each other the other day and decided to catch up properly. After all the stress is so high, our social lives have taken a collective dump."

    show pink hair smile01 at phz1
    g1 "Hey is he okay ?"
    show pink hair smile01 at phz2

    #  Panting. Can be depicted by some random transition of scenes, moving the characters

    n  "Suddenly, Rohit hits me"
    p  "Owww !"

    show male smi02 at mz1
    r  "Welcome back. Guys this is my friend Hero. We have been together since childhood. He is an engineer at XYZ company."    
    show male smi02 at mz2
    p  "(meekly) Hi !!"

    show pink hair smile01 at phz1
    g1 "Oh my God, Relax man. We arent going to eat you. By the way I'm g1. I'm working to protect people like you.  "
    show pink hair smile01 at phz2

    show male smi02 at mz1
    r  "(confused) Sorry ?"
    show male smi02 at mz2

    show pink hair smile01 at phz1
    g1 "I mean I'm a corporate lawyer. Hehe "
    show pink hair smile01 at phz2

    n  "That was a really poor joke."

    show ros_akuwaraia1 at rosz1
    g2 "Well I'm g2. I am a school teacher"
    show ros_akuwaraia1 at rosz2

    show dark hair smi01 at dhz1
    g3 "And you must already know me. I am the famous actress ...."
    show dark hair smi01 at dhz2

    p "Sorry I dont know you. But I feel I have seen you somewhere. "

    show dark hair ang at dhz1
    g3 "(tad angry) g3. Im in the UNESCO ad that everyone has been talking about. Gosh have you not followed my Instagram page alreadyyyyy."
    show dark hair ang at dhz2

    show male smi02 at mz1
    r "And that's dinner. I am really hungry. Anyone up for some starters."
    
    r "(pulling Hero closer), this is your chance."
    show male smi02 at mz2
    p "Seriously man, i'm sweating buckets here"
    show male smi02 at mz1
    r "Live a little buddy."
    show male smi02 at mz2
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

        # good_choice:



        # bad_choice:

        # worst_choice

        


    # with hpunch
    # with blinds
    # with squares
    # with zoomin
    # with vpunch
  
    
    label selectgame:

    n "Select the minigame you wish to play"


    menu:

        "music minigame":
            jump music_minigame

        "pong minigame":
            jump pong_minigame

    label music_minigame:

        p "Let's do karoake"

        jump play_game1

    label pong_minigame:

        p "Let's play pong"

        jump play_game2

    label play_game1:

        call simon pass (complete=8, toadd=2)
        
        jump continue_game

    label play_game2:

        call demo_minigame

        jump continue_game
        
    label continue_game:
            # ... the game continues here.
    # This ends the game.

    n "Your Score increased by 10"

    return

image blackflash:
    Solid("#000")
    alpha 0.0
    linear 0.25 alpha 0.2
    linear 0.75 alpha 0.6
    linear 1.0 alpha 0.8
    linear 0.25 alpha 0.0

transform place(x=None,y=None,z=1.0):
    xalign x
    yalign y
    linear .25 zoom z

transform ph1:
    place(x=-0.1)

transform phz1:
    place(x=-0.1,z=1.05)

transform phz2:
    place(x=-0.1,z=1.0)

transform dh1:
    place(x=0.25,y=1.0)

transform dhz1:
    place(x=0.25,y=1.0,z=1.05)

transform dhz2:
    place(x=0.25,y=1.0,z=1.0)

transform ros1:
    place(x=1.3)

transform rosz1:
    place(x=1.3,z=1.05)

transform rosz2:
    place(x=1.3,z=1.0)

transform m1:
    place(x=0.65)

transform mz1:
    place(x=0.65,z=1.05)

transform mz2:
    place(x=0.65,z=1.0)
