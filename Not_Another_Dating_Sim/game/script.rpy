# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define p = Character("[name]")
define r = Character("Rohit")
define n = Character(" ",what_prefix="{i}", what_suffix="{/i}")

define g1 = Character("Ananya") # pink hair
define g2 = Character("Riya") # gunny girl
define g3 = Character("Zoya") # dark hair


# The game starts here.
# p is the player

label start:

    play music "sounds/bgm/2.ogg"

    $ confidence_meter = 50

    n "Hi, welcome to our humble game. Before you begin please tell us your name."

    python:
        name = renpy.input(_("What's your name?"))

        name = name.strip() or __("Lord Voldemort")

    n "Hi [name], great thanks for joining us on this journey "
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    stop music fadeout 1.0
    play music "sounds/bgm/backstorybg.mp3"

    scene startdark

    n "Another gloomy day beckons , ready to witness the same old story again. The sun rising in the east and setting in the west."
    n "Nothing new , Nothing different , Nothing to be happy about .... "

    scene starthome

    n "Well Rohit has asked me to meet at McLaren Pub. Perhaps I should go ... , he is a good guy and I need to come out of this sad depressing shell."
    n "Yeah , you know what I will go."

    stop music fadeout 1.0

    play music "sounds/bgm/3.ogg"

    scene pub2

    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show male smi01 with dissolve
    # $ style.say_dialogue = style.edited
    # $ gtext = randomshuffle("And here we are celebrating my friend Rohit's work anniversary")
       
    # p "[gtext]"
    # $ style.say_dialogue = style.normal
    n "And here we are celebrating my friend Rohit's work anniversary"    

    r "Hey man why so serious? It's been such a hectic couple of months and I just want to relax today."

    p "(nervously) Hey I am really happy for you, it's just I don't like being with so many people." with vpunch
    
    r "Come on, Loosen up. What the ..."
    
    # hide male smi01
    show male smi02 with dissolve

    p "What happened ?"
    
    r "OMG!!! I don't believe it ?"
        
    p "(shaking) What???  " with hpunch
    
    r "Ananya,Riya and Zoya all together. Wow they must be having some sort of reunion together."
    
    p "How do you know them? "

    show male sly01 with dissolve
    r "Oh we were in school together. I wasn't close to them but knew them well."

    r "Come lets catch up with them."

    p "What? No No. What will i do, i don't even know them."

    show male sly02 with dissolve
    r "Arre why are you so concerned?" 
  
    p "(stuttering) I have avoided all... humanity uptill... now and.. you want.... me to talk.... to three strangers."
    # with Fade(5.0) zorder 10
    show blackflash zorder 50
    # > p shaking. Depict by bluring the screen or something

    n "So Rohit pulled me against my will."
    hide male smi02
    
    show pink hair smile01 with moveinright
    g1 "Hey Hey Hey!!!! Look who showed up"
    show pink hair smile01 at ph1

    show ros_akuwaraia1 with dissolve
    g2 "OMG!!! It's been so long. How are you ???"
    show ros_akuwaraia1 at ros1

    show male smi02 with dissolve
    r  "Oh not too bad. Is this some coincidence or were you guys always planning to catch me like this ? xD"

    show male smi02 at m1
 
    show dark hair smi01 at dh1 with dissolve
    g3 "Don't flatter yourself. Well we ran into each other the other day and decided to catch up properly. After all the stress is so high, our social lives have taken a collective dump."

    show pink hair sad01 at phz1
    g1 "Hey is he okay ?"
    show pink hair neutral02 at phz2

    #  Panting. Can be depicted by some random transition of scenes, moving the characters

    n  "Suddenly, Rohit hits me" with vpunch
    p  "Owww !"

    show male smi02 at mz1
    r  "Welcome back. Guys this is my friend [name]. We have been together since childhood."    
    show male smi02 at mz2
    p  "(meekly) Hi !!"

    show ros_akuwaraia1 at rosz1
    g2 "Oh my God, Relax man. We aren't going to eat you. By the way I'm Riya. I'm working to protect people like you.  "
    show ros_akuwaraia1 at rosz2

    # show male smi02 at mz1
    p  "(confused) Sorry ?"
    # show male smi02 at mz2

    show ros_akuwaraia1 at rosz1
    g2 "I mean I'm a corporate lawyer. Hehe "
    show ros_akuwaraia1 at rosz2

    n  "That was a really poor joke."

    show pink hair smile01 at phz1
    g1 "Well I'm Ananya. I am a school teacher"
    show pink hair smile01 at phz2

    show dark hair smi01 at dhz1
    g3 "And you must already know me. I am the famous actress ...."
    show dark hair smi01 at dhz2

    p "Sorry I don't know you. But I feel I have seen you somewhere. "

    show dark hair ang at dhz1
    g3 "Zoya. I'm in the UNESCO Ad that everyone has been talking about. Gosh have you not followed my Instagram page alreadyyyyy."
    show dark hair ang at dhz2

    show male smi02 at mz1
    r "And that's dinner. I am really hungry. Anyone up for some starters."
    
    hide dark hair ang with dissolve
    hide pink hair smile01 with dissolve
    hide ros_akuwaraia1 with dissolve
    hide male smi02 with dissolve
    show male smi02
    r "(pulling [name] closer), this is your chance."

    show male smi02
    p "Seriously man, I'm sweating buckets here"
    r "Live a little buddy."
    hide male smi02
    label selectgirl:

        play music "sounds/bgm/4.ogg"
        n " Which girl do you wanna talk to more ?"

        menu:
        
            "Ananya":
                jump g1_story

            "Riya":
                jump g2_story

            "Zoya":
                jump g3_story
        
        stop music fadeout 1.0
    
    # g1_story
    label g1_story:

        play music "sounds/bgm/3.ogg"
        $ played_pong_minigame = False
        
        # show g1 neutral
        scene pub2 with dissolve
        show pink hair neutral01
        
        n "Riya , Zoya and Rohit leave for starters. You are alone with Ananya."

        p  "Ummm  "
        g1  "Uhhh  "
        p  "(nervous laughter) Uhh  "
        show pink hair smile03 with dissolve
        g1  "Sorry. I must be boring you. uhh  "
        p  "No no not at all. I'm just not used to this.  "
        g1  "Well to be honest me too. He he  "
        p  "So what do you teach?? Arts?  "
        show pink hair neutral01 with dissolve
        g1  "No I teach history to senior students "
        n  "How do you take this conservation forward."

        menu:
        
            "Wow! Must be a real headache keeping those teen ego's in check ":
                # n "Good Choice"

                # show g1 happy
                show pink hair smile01 with dissolve
                g1 "Yeah not many people realize how hard it is.  "
                p  "But I am sure it's rewarding.   "
                g1 "Yeah sure is. Always feel happy to see a successful student.  "
                p  "Yeah most important job in the world.  "

                $ confidence_meter += 10

                

            "Yeah you look the part. A typical History teacher. Not too smart. Ha Ha":
               
                # n "Bad Choice"
                
                # show g1 annoyed
                show pink hair annoyed01 with dissolve
                g1 "Well those who forget history are doomed to repeat it.  "
                p "Like reading pointless escapades of kings before. He He  "
                g1 "It's this exact reason for which I teach History.  "
                p "Well I hope you teach something real like Science.  "
                
                # jump bad_choice
                $ confidence_meter -= 10

            
            "Well you got it easy with the job. Personally the easiest job in history. Ha Ha":
                # n "Worst Choice"

                # show g1 angry/upset
                show pink hair ang01 with dissolve
                g1 "Well it's not as easy as it looks."
                p  "Really? Well all you have to do is look good and read from the book. No ?"
                g1 "Seems like you didn't have good teachers.  "
                p  "Well they did allow us to sleep in class so I guess they were pretty good."

                $ confidence_meter -= 10
        
        show pink hair neutral01 with dissolve
        p  "Anyways you got any hobbies ? "
        g1  "Yeah I like cooking. I also like to watch bollywood movies."
        p  "Oh what is your favourite dish to cook ?  "
        g1  "I like to cook Gujrati food."
        
        $ rigged = ""
        if confidence_meter <= 45:
            $ rigged = "rigged_choice"
        else:
            $ rigged = "choice"
        menu(screen=rigged):

            "Oh that's pretty lame. You should try more awesome things like pasta and burger.  ":
                
                show pink hair annoyed01 with dissolve
                g1  "Well to each their own. "
                p  "Anything not pasta is so stupid. Go for pasta only. "    
                show pink hair annoyed02 with dissolve
                g1  "(visibly annoyed).Hmm sure "

                $ confidence_meter -= 10
                # encrypt at 35
                # > Confidence hit. Show g1 angryp             
                
            "Wow that's actually interesting. I would love to know more.":
                
                show pink hair smile01 with dissolve
                g1  "Oh sure (visibly excited). It's very different to what you would find elsewhere.  "
                p  "Really how ?  "
                g1  "Well we like everything sweet. So you find a bit of sweetness in everything we eat.  "
                p  "Wow, that is so different. The only sweet I've ever had is in form of ice creams. Would love to try sometime.  "
                g1  "Sure. Next time we meet, I'll try to get something for you."

                $ confidence_meter += 4

                # > Show Dhwani excited. Confidence becomes little better


            "You mean dhokla and thepla. Yeah sweet just like you.":

                show pink hair smile03 with dissolve
                g1  "Well you are not wrong about the food.   "
                p  "I actually like Gujrati food. I had some Gujarati friends in college.    "
                g1  "Wow can you speak gujrati then?.  "
                p  "Tārā māṭē kaṁīpaṇa.(Anything for you) "

                $ confidence_meter += 10

                #> Dhwani all red. Confidence skyrockets. Can show bit of shivering

        $ encryptd = False
        if confidence_meter <= 35:
            $ encryptd = True
        show pink hair smile01 with dissolve
        
        g1  "Oh Wow , is that people playing air hockey, come on let's go and play too."

        ## Flash_Back
        # Scene change - arcade game.
        stop music fadeout 1.0
        play music "sounds/bgm/backstorybg.mp3"

        scene arcade1 with Pixellate(2.0,5)
        n  "Your thoughts turn back to 26.05.2008 the last truly happy day of your life. Your parents had taken you out to a gaming arcade for your 11th birthday."

        n  "Ah it was so much fun playing all the games with your mom,dad and sister, such a happy family."

        # Scene change parents fighting
        scene sady with fade        
        n  "However that night you couldn't sleep with all the excitement , and you heard raised voices from your parent's room"

        n  "You peeked and saw your dad throwing a vase at your mom ...... nothing was ever the same again."
        
        # Scene change - present
        scene pub2 with fade
        show pink hair smile01 with dissolve
        stop music fadeout 1.0
        play music "sounds/bgm/3.ogg" 
        
        g1 "Hey you still here , come on let's go."
        

        menu:
            
            "Yes":
                show pink hair smile01 with dissolve
                p "Yeah come on let's play. (in a shaky voice)."
                # scene - changes to 
                scene bary with fade
                call pong_minigame
                
                $ played_pong_minigame = True
                
            "No":
                show pink hair annoyed01 with dissolve
                g1  "Come on don't be a spoilsport."
                p   "No I don't want to play. I don't like it at all."
                show pink hair annoyed02 with dissolve
                $ confidence_meter -= 10

        scene pub2 with fade
        show pink hair neutral01 with dissolve
        
        $ diag = randomshuffle("Anyways what do you like to do on a lazy afternoon?",encrypt=encryptd)
        p  "[diag]"
        $ diag = randomshuffle("I like to drink coffee and read a book.  ",encrypt=encryptd)
        g1 "[diag]"

        $ opt1 = randomshuffle("Me too. I love to read as well.",0.75,encrypt=encryptd)
        $ opt2 = randomshuffle("Hmm. Chetan Bhagat am I right ?",0.85,encrypt=encryptd)
        $ opt3 = randomshuffle("That's so borrriiinnnnggg.",encrypt=encryptd)
        $ style.say_dialogue = style.edited
        menu:
            "[opt1]":
                show pink hair smile01 with dissolve
                $ diag = randomshuffle("Wow, what do you read ?",0.8,encrypt=encryptd)
                g1 "[diag]"
                $ diag = randomshuffle("Well I like to read biographies. My favourite was the one on Steve Jobs by Walter Issacson.",0.8,encrypt=encryptd)
                p  "[diag]"
                $ diag = randomshuffle("Oh I like to read about the Mughal Period.",0.8,encrypt=encryptd)
                g1  "[diag]"
                $ diag = randomshuffle("Guess we are alike on this one.",0.8,encrypt=encryptd)
                p  "[diag]"
                show pink hair smile03 with dissolve
                $ confidence_meter += 10
                # > > Confidence boost. Show Dhwani blushing. 

            "[opt2]":
                
                show pink hair annoyed01 with dissolve
                $ diag = randomshuffle("Well I don't like his novels.",0.8,encrypt=encryptd)
                g1  "[diag]"
                $ diag = randomshuffle("Wow, you have a really poor choice in authors.",0.8,encrypt=encryptd)
                p   "[diag]"
                show pink hair ang01 with dissolve
                $ diag = randomshuffle("Oh really.",0.8,encrypt=encryptd)
                g1 "[diag]"
                $ confidence_meter -= 10

                # > Show Dhwani angry.


            "[opt3]":

                $ diag = randomshuffle("Ok then what do you like?  ",0.8,encrypt=encryptd)
                g1 "[diag]"
                $ diag = randomshuffle("Watching Netflix  ",0.8,encrypt=encryptd)
                p  "[diag]"
                $ diag = randomshuffle("Well i find it boring.  ",0.8,encrypt=encryptd)
                g1 "[diag]"
                $ diag = randomshuffle("Guess we agree to disagree.  ",0.8,encrypt=encryptd)
                p  "[diag]"

            #Dhwani indifferent.Confidence level same.
        stop music fadeout 1.0
        
        $ style.say_dialogue = style.normal
        if confidence_meter >= 35:
            call win_ending pass(girl = g1)
            jump the_end_happy
        else:
            call loss_ending pass(girl = g1)
            jump the_end_sad


    label g2_story:

        play music "sounds/bgm/3.ogg"

        n "Ananya, Zoya and Rohit leave for starters. You are alone with Riya."

        $ played_puzzle_minigame = False
        $ really_bad_choice = False
        $ encrypt_g2 = False
        $ weird = False
        scene pub2 with dissolve
        

        

        show ros_defa1 with dissolve
        p  "Ummm  "
        g2  "So hotshot [name], you must be smart."
        p  "(nervous laughter) Uhh. what can i say. he he  "
        g2  "Well you could tell start by telling me where did you graduate from ?"
        p  "Uh Uh umm"
        show ros_akuwaraia1 with dissolve
        g2  "Man relax. I am not gonna sue you.    "
        p  "Huh? Oh haha. I am actually from IIT-D.."
        g2  "Delhi. Not too bad. I'm impressed.    "
        p  "No actually. It's Dharwad. he he "
        hide ros_akuwaraia1
        
        show ros_defa1 with dissolve
        g2  "Oh I am sorry. Well I hope they have chairs xD. "
        p  "Uhmm uhh  "
        p  "So......  "
        p  "So corporate law and all ? Must be taxing.  "
        g2  "Yeah it's not easy. Really stressful. "

        label convo_start:
        if really_bad_choice == True:
            play music "sounds/bgm/hatestory.mp3"
            scene pub2 red
            show ros_ikaria2 with dissolve 
            g2  "Yeah it's not easy. Really stressful. "

        menu:

            "So is it like Suits (TV-Series). Making mergers and looking smart.":
                if really_bad_choice == True:
                    n "What's happening !!, why did I say it , why is she repeating the same thing again and again."
                    jump convo_start

                hide ros_defa1
                show ros_waraia1 with dissolve
                g2  "Well not sure about smart. But I do love wearing those dresses."
                p  "He He. Btw have you finished the show?"
                g2  "Damn right xD. Yeah completed in a weekend. "
                p  "Wow you are a fan.   "

                $ confidence_meter += 10
                # > > Confidence boost. Show Dhwani blushing. 

            "Yeah, keep the guys happy. Tough indeed. He he":
                hide ros_defa1
                show ros_ikaria4 with dissolve
               
                if really_bad_choice == False:
                    g2  "You do know what you just said, Right?.  "
                    p  "Uhm did I say something bad?  "
                    g2  "It's people like you who make it so hard for girls to survive. It's a real shame.  "
                    p  "I'm so sorry. I didn't mean to say that."
                    
                    $ confidence_meter -= 25

                    g2 "Oh really you didn't mean say that you misogynist creep."
                    g2 "I DARE YOU TO SAY IT AGAIN."

                if really_bad_choice == False:
                    $ really_bad_choice = True
                    jump convo_start                 
                
                if really_bad_choice == True:
                    scene pub2 red
                    show ros_ikaria2g with dissolve
                    g2 "Wow, what sort of monster parents grew up such a child"
                    call loss_ending(girl = g2)
                    stop music fadeout 1.0
                    jump the_end_sad
                # > Show Dhwani excited. Confidence becomes little better


            "Yeah being a secretrary must be tough.":
                if really_bad_choice == True:
                    n "What's happening !!, why did I say it , why is she repeating the same thing again and again."
                    jump convo_start
                
                
                hide ros_defa1
                show ros_ikaria3 with dissolve
                g2  "Excuse me. I have done law from NLU. Ever heard of it? I'm a junior associate at a prestigious law firm  "
                p  "Oh I just thought ....  "
                g2  "And even if I was a secretrary. Even then I deserve to be respected no?  "
                p  "Sorry. I didn't mean it that way. I didn't mean to hurt you. "

                $ confidence_meter -= 10
        # scene pub2
        if confidence_meter <= 40:
            $ encrypt_g2 = True
        show ros_defa1 with dissolve
        $ diag = randomshuffle("Anyways you got any hobbies? ",encrypt=encrypt_g2)
        p  "[diag]"
        $ diag = randomshuffle("Yeah I like travelling. I recently travelled to the States.",encrypt=encrypt_g2)
        
        g2  "[diag]"
        $ diag = randomshuffle("uhh which states?  ",encrypt=encrypt_g2)
        
        p  "[diag]"
        $ diag = randomshuffle("United States of America stupid.",encrypt=encrypt_g2)
        
        g2  "[diag]"
        $ diag = randomshuffle("Oh my bad. Is that how they say it? He he.",encrypt=encrypt_g2)
        
        p  "[diag]"
        $ diag = randomshuffle("What about you?",encrypt=encrypt_g2)
        g2  "[diag]"

        $ opt1 = randomshuffle("Uhmm. Nothing much really. Watching Netflix I guess?",0.75,encrypt=encrypt_g2)
        $ opt2 = randomshuffle("Well me too. Though I haven't really gone beyond the shores yet.",0.85,encrypt=encrypt_g2)
        $ opt3 = randomshuffle(" Uhmm. Does playing cricket count? He he",encrypt=encrypt_g2)
        if encrypt_g2 != False:
            $ style.say_dialogue = style.edited
        menu:

            "[opt1]":
                hide ros_defa1
                show ros_ikaria3 with dissolve
                $ diag = randomshuffle("Wow. Don't you get bored ?",0.7,encrypt=encrypt_g2)
                g2  "[diag]"
                $ diag = randomshuffle("uhmm there are good shows like sacred games,etc. So keeps me busy.",0.7,encrypt=encrypt_g2)
                
                p  "[diag]"
                $ diag = randomshuffle("(unimpressed).Hmm sure",0.7,encrypt=encrypt_g2)
                
                g2  "[diag]"

                $ confidence_meter -= 10
                # > > > Confidence hit. Show labdhi unimpressed. 
 

            "[opt2]":
                hide ros_defa1
                show ros_waraia1 with dissolve
                $ diag = randomshuffle(" Well I haven't roamed around India much. What's your favorite place.",0.7,encrypt=encrypt_g2)
                g2 "[diag]"
                $ diag = randomshuffle(" I like mountains. I find Manali to be quite nice.",0.7,encrypt=encrypt_g2)
                p "[diag]"
                $ diag = randomshuffle(" Yeah but still it's so lame unlike the Alps.  ",0.7,encrypt=encrypt_g2)
                
                g2 "[diag]"
                $ diag = randomshuffle(" Maybe. Every place has it's own charm. So...  ",0.7,encrypt=encrypt_g2)
                p "[diag]"
                $ diag = randomshuffle("Yeah but still everything foreign is so much better.",0.7,encrypt=encrypt_g2)
                g2 "[diag]"

                $ confidence_meter -= 5

                # > Show excited. Confidence becomes little lower


            "[opt3]":
                
                hide ros_defa1
                show ros_ikaria3 with dissolve
                $ diag = randomshuffle("(unimpressed).Typical Indian hobby.",0.7,encrypt=encrypt_g2)
                g2 "[diag]"
                $ diag = randomshuffle("Well it's fun. Did you follow the world cup?",0.7,encrypt=encrypt_g2)
                p  "[diag]"
                $ diag = randomshuffle("Yeah Yeah a bit. Everyone was following so I saw a bit.  ",0.7,encrypt=encrypt_g2)
                g2  "[diag]"
                $ diag = randomshuffle("You don't follow any sports ?",0.7,encrypt=encrypt_g2)
                p  "[diag]"
                $ diag = randomshuffle("Not really. Work takes up all my time.",0.7,encrypt=encrypt_g2)
                g2  "[diag]"

                $ confidence_meter += 5
        $ style.say_dialogue = style.normal
        show ros_defa1 with dissolve
        p  "Hey what's that popping out of your coat pocket?"
        g2  "Ah this thing , it's a sliding puzzle. I use it as a stress-buster. Do you wanna try it ?"  
        stop music fadeout 1.0

        play music "sounds/bgm/backstorybg.mp3"
        # Relevant cutscene backstory
        scene pub2 with fade
        n  "Stress buster huh , well I wish I had something of this sorts when I was younger "
        scene drunky with Pixellate(2.0,5)
        n  "Anything to distract me from the rants of my drunk,senseless father."
        scene gandi-mom with fade
        n "And forget the string of affairs my mom had. All this happening the year of my board exams."
        scene sundary with fade
        n  "Hmm , no [name] you are stronger than this , don't live in the past , don't it will only bring you pain. Think of positive things. "

        scene pub2 with fade
        show ros_defa1 with dissolve
        stop music fadeout 1.0
        
        play music "sounds/bgm/3.ogg"
        
        $ style.say_dialogue = style.edited
        g2 "Hello !! , Earth to [name] , Earth to [name]. Do you wanna try it."
        $ style.say_dialogue = style.normal
        
        menu:
            
            "Yes":
                hide ros_defa1
                show ros_waraia1 with dissolve
                p "Yeah sure I will give it a try. (in a shaky voice)."
                # scene - changes to karaoke
                scene bar_indoor with fade
                call fifteen_game
                
                $ played_puzzle_minigame = True
                
            "No":
                hide ros_defa1
                show ros_komarua1 with dissolve
                g2  "Come on don't be a spoilsport."
                p   "No I don't want to do it. I don't like it at all."

                $ confidence_meter -= 20
        scene pub2 with fade
        if confidence_meter > 40:
            $ encrypt_g2 = False
        if confidence_meter < 30:
            $ weird = True
        
        if  weird  == True:
            scene pub2 with fade:
                xpan 0
                linear 2.0 xpan 360
                repeat
            show ros_defa1 at xy
        else:
            show ros_defa1 with dissolve
        if encrypt_g2 != False:
            $ style.say_dialogue = style.edited
        $ diag = randomshuffle("So what's your favorite movie?",0.6,encrypt=encrypt_g2)
        p  "[diag]"
        $ diag = randomshuffle("Oh I love rom coms and sci-fi. So my favurite movies are Princess Diaries and Interstellar.",0.6,encrypt=encrypt_g2)
        g2  "[diag]"
        $ diag = randomshuffle("Nice. Yeah even like I to watch movies.  ",0.6,encrypt=encrypt_g2)
        p  "[diag]"
        $ diag = randomshuffle("Oh what's your favourite one?",0.6,encrypt=encrypt_g2)
        g2  "[diag]"
        $ opt1 = randomshuffle("Well I loved Koi Mil Gaya. It really inspired me as a kid.",0.75,encrypt=encrypt_g2)
        $ opt2 = randomshuffle("My favourite is Iron Man",0.85,encrypt=encrypt_g2)
        $ opt3 = randomshuffle("I liked Hera Pheri.",encrypt=encrypt_g2)
        menu:

            "[opt1]":
                $ diag = randomshuffle("Interesting. It's basically a ripoff of ET, but sure.",0.8,encrypt=encrypt_g2)
                g2  "[diag]"
                p  "Actually that's not entirely true. It was initially a plan of Satyajit Ray in collaboration with some American production house. Then those guys actually leaked the script to Steven Spielberg.  ?"
                p  "Even Rakesh Roshan mentioned it in his press conference.  ?"
                hide ros_defa1
                show ros_akuwaraia1 with dissolve
                $ diag = randomshuffle("I have to say, i didn't see that one coming.",0.8,encrypt=encrypt_g2)
                g2  "[diag]"
                p  "Actually it's a shame as to how often we Indian's don't get credit. Radio, Airplanes, the list goes on. ?"
                $ diag = randomshuffle("(embarrased) I feel embarassed to not know about this.",0.8,encrypt=encrypt_g2)
                g2  "[diag]"
                $ confidence_meter += 10
                # > Confidence boost. Show Labdhi blushing. 


            "[opt2]":
                $ diag = randomshuffle("Oh so you are one of those Marvel fanboys.",0.8,encrypt=encrypt_g2)
                g2  "[diag]"
                $ diag = randomshuffle("It's not just that. It inspired a young kid to become an engineer and is pretty entertaining  ",0.8,encrypt=encrypt_g2)
                p  "[diag]"
                $ diag = randomshuffle("You aren't wrong there to be honest.",0.8,encrypt=encrypt_g2)
                g2 "[diag]" 
               
                $ confidence_meter -= 5

                # > (Labdhi indifferent Confidence a bit high


            "[opt3]":

                hide ros_defa1
                show ros_ikaria3 with dissolve

                g2 "Isn't it a bit too forced and misogynist.  "
                $ diag = randomshuffle("Well, the idea of a movie is to entertain and it's a good light hearted one watch.  ",0.8,encrypt=encrypt_g2)
                p  "[diag]"
                g2 "Still, I think there shouldn't be any room for regressive thoughts.    "
                $ diag = randomshuffle("Guess we agree to disagree. He he",0.8,encrypt=encrypt_g2)
                p  "[diag]"
                
                $ confidence_meter -= 10
                # > Labdhi indifferent Confidence level lowers.
        
        stop music fadeout 1.0
        
        $ style.say_dialogue = style.normal
        if confidence_meter >= 35:
            call win_ending pass(girl = g2)
            jump the_end_happy
        else:
            call loss_ending pass(girl = g2)
            jump the_end_sad

    label g3_story:
        
        play music "sounds/bgm/3.ogg"

        n "Riya , Ananya and Rohit leave for starters. You are alone with Zoya."

        $ played_karoake_minigame = False
        $ encrypt_g3 = False
        $ weird = False

        scene pub2 with dissolve
        show dark hair neu01 with dissolve

        p  "Ummm  "
        g3  "Sooooo  "
        p  "(nervous laughter) Uhh. sooo.... uhh  "
        g3  "Well are you gonna talk or stay like that ?    "
        p  "Uh Uh umm"
        show dark hair ann01 with dissolve
        g3  "Gosh are you gonna stay dumb like that?    "
        p  "Oh sorry. ummm"
        
        g3  "OMG, this so weird. Anyways are you on instagram?    "
        p  " umm. Yeah yeah but I don't use it too often.  "
        g3  "Oh well then follow me. Or you can even not, I mean I have 30k followers.   "
        p  "But everyone counts right?    "
        show dark hair neu03 with dissolve
        g3  "(embarrased) Oh yeah totally. Please follow me.   "
        p  "So how much time on average do you spend there?  "
        g3  "Well, mostly my manager manages my account. But i like to read comments and give fans what they want."
        
        menu:

            "Well it's important to be connected to them.":
                
                g3  "If the fans turn on you, then it's really hard to gain back their trust.    "
                p  "True that. I guess all celebrities must feel that way.   "
                g3  "That's right. So why don't you do me a favor and follow me on Tiktok. My handle is zoya_rocks.   "
                p  "umm uhh.    "
                show dark hair ann01
                g3  "Gosh you aren't on TikTok are you?  "
                p  " Sorry I'm not. umm uhh, I could follow you on Linkedin.  "
                g3  "You are such a nerd.              "

                $ confidence_meter -= 5
                
                
                # > > Confidence goes down. g3 unimpressed 


            "But shouldn't you focus more on other things like your acting.":
                
                g3  "I think I know what's important.    "
                p  "Sorry. I just meant since you are an actress, that should be your strength,right?    "
                show dark hair ang with dissolve
                g3  "Listen, just because you are an engineer and you think you are SO SMART, you don't get to tell me what I should do or what I shouldn't.   "
                p  "umm uhh.Sorry you are right I shouldn't.    "
                
                show dark hair sad01 with dissolve
                g3  "(apologetic) I am sorry, I shouldn't have shouted. "
                g3 "It's just there is so much pressure on me at the moment.   "
                p  " I understand. It's okay. Life is pretty hard on us sometimes isn't it?  "
                g3  "Yeah it sometimes feel like such a huge mountain, an impossible obstacle. It's unbearable.  "
                p  "Well mountains are meant to be climbed aren't they?"
                
                $ confidence_meter += 10

                show dark hair smi01 with dissolve
                # > (Labdhi indifferent) Confidence a bit high


            "Well, that comes at cost of self respect doesn't it. He he":

                show dark hair ang with dissolve
                g3 "What do you know about self respect huh?  "
                p  "Oh i didn't mean to say..  "
                g3  "Do you even know what do I have to go through every single day? "
                p  "Sorry. I didn't mean it that way. I didn't mean to hurt you.    "
                
                show dark hair sad02
                g3  "What i have to listen every single day .."
                p  "Hey, listen i didn't mean to say like that. umm I'm quite an idiot. I'm really sorry"
                
                $ confidence_meter -= 10
                # > Labdhi indifferent.Confidence level lowers.
        if confidence_meter <= 40:
            $ encrypt_g3 = True
        $ diag = randomshuffle("Anyways you got any hobbies ?",0.8,encrypt=encrypt_g3)
        p  "[diag]"

        show dark hair neu01 with dissolve

        $ diag = randomshuffle("I love dancing and singing.Ever since I was a kid, I used to find every opportunity I could, to dance.",0.8,encrypt=encrypt_g3)
        g3  "[diag]"
        $ diag = randomshuffle("Ohh nice.",0.8,encrypt=encrypt_g3)
        p  "[diag]"
        $ diag = randomshuffle("What about you ?    ",0.8,encrypt=encrypt_g3)
        g3  "[diag]"
        $ diag = randomshuffle( "Uhh I don't know.",0.8,encrypt=encrypt_g3)
        p  "[diag]"
        $ diag = randomshuffle("Come on. I am trying to convince myself you are not as lame as you look.    ",0.8,encrypt=encrypt_g3)
        g3  "[diag]"
        $ opt1 = randomshuffle("Uhmm. Nothing much really. Watching Netflix I guess?",0.75,encrypt=encrypt_g3)
        $ opt2 = randomshuffle("I did do some acting in school. I guess you could count that.",0.85,encrypt=encrypt_g3)
        $ opt3 = randomshuffle(" Uhmm. Does playing cricket count? He he",encrypt=encrypt_g3)
        

        menu:

            "[opt1]":
                
                $ diag = randomshuffle("What's your favorite show there?",0.9,encrypt=encrypt_g3)
                g3  "[diag]"
                p  "Stranger Things. It's just ...  "
                
                show dark hair smi01 with dissolve
                
                $ diag = randomshuffle( "(impressed). so cuuuuttttteeeeeee!!!!",0.9,encrypt=encrypt_g3)
                g3  "[diag]"
                p  "Uhm yeah, you could say that as well.  "
                $ diag = randomshuffle( "Though it's not much of a hobby. Unless you can win a quiz based on Netflix.",0.9,encrypt=encrypt_g3)
                g3  "[diag]"
                p  "Maybe I could. I don't know"
            
                $ confidence_meter += 5
            

            "[opt2]":
                
                show dark hair smi01 with dissolve
                
                g3  "Wow you mean like school plays.Yeah i used to be the star in them..    "
                $ diag = randomshuffle( "I wasnt any great. A bit here and there.     ",0.9,encrypt=encrypt_g3)
                p  "[diag]"
                g3  "Well as an accomplished actress I can tell you it's not about the role, it's about how you perform it.  "
                $ diag = randomshuffle( "uhh umm Yeah I guess you are right.   ",0.9,encrypt=encrypt_g3)
                p  "[diag]"
                
                g3  "To be honest, I didn't think you would be involved in acting."
                $ diag = randomshuffle( "No no, just a bit. He he ",0.9,encrypt=encrypt_g3)
                p  "[diag]"

                # > Show Khushi smiling. Confidence increases.

                $ confidence_meter += 10


            "[opt3]":

                $ diag = randomshuffle( "(unimpressed). Oh I just looovvveeee Virat Kohli.   ",0.8,encrypt=encrypt_g3)
                g3 "[diag]"
                # $ diag = randomshuffle( "No no, just a bit. He he ",0.9,encrypt=encrypt_g3)
                p  "Yeah he is such a good batsman. It's a strugg....    "
                # $ diag = randomshuffle( "No no, just a bit. He he ",0.9,encrypt=encrypt_g3)
                g3  "He is so cute. I am so jealous of Anushka."
                $ diag = randomshuffle( "You just like him because he is cute ?",0.8,encrypt=encrypt_g3)
                p  "[diag]"
                # $ diag = randomshuffle( "No no, just a bit. He he ",0.9,encrypt=encrypt_g3)
                show dark hair ann02
                g3  "Duh. Also his abbs. OMGGGG!!!!"

                # > Khushi smiles. Confidence decreases.  
                $ confidence_meter -= 5
        
        show dark hair smi01
        g3  "Hey is that music I hear , Come on let's go and try out karaoke"
        stop music fadeout 1.0

        play music "sounds/bgm/backstorybg.mp3"
        # scene pub2

        ## Flash_Back

        # Scene change - school event.
        scene stage1 with Pixellate(2.0,5)
        n  "You suddenly had a flashback to your 7th grade annual function event."

        n  "You remember how you finally had the guts to go on stage and sing your hearts out, you had practiced and learnt all the lyrics."

        # Scene change - on stage public humiliation , people laughing two or three scenes.
        scene sadkiddo with fade
        n  "But seeing the audience of over 500 , you forgot everything and ran away from the stage."
        scene bully with fade
        n  "It's all coming back the jeering, taunts and bullying that you had to face the entire year. That was the year when you developed the stutter."
        

        # Scene change - present
        # scene pub2 with fade:
        #     xpan 0
        #     linear 2.0 xpan 360
        #     repeat
        # show dark hair smi01 at xy
        stop music

        g3 "Come on let's go for karaoke ?"
        
        menu:
            
            "Yes":
                

                show dark hair neu03 with dissolve

                p "O .. Ok . Okay .. sure let's g .. go."
                # scene - changes to karaoke
                scene karaoke with fade
                g3 "Go on it's your turn"

                call simon(complete=8, toadd=2)
                
                $ played_karoake_minigame = True

            "No":

                show dark hair ann01 with dissolve

                g3  "Come on don't be a spoilsport."
                p   "No .. N .. No I don't want to do ka .. kara..oke. I don't like it at all."

                $ confidence_meter -= 10
        if confidence_meter > 40:
            $ encrypt_g3 = False
        if confidence_meter < 30:
            $ weird = True
        
        if  weird  == True:
            scene pub2 with fade:
                xpan 0
                linear 2.0 xpan 360
                repeat
            show dark hair ann01 at xy
        else:
            scene pub2 with fade
        
            show dark hair ann01 with dissolve
        
        
        play music "sounds/bgm/3.ogg"
        
        p  "Anyways, umm "
        
        
        $ diag = randomshuffle( "What? You take hella lot of time to say things.",0.8,encrypt=encrypt_g3)
        g3  "[diag]"
        p  "So what's your cheat day meal like?   "
        if  weird  == True:
            scene pub2 with fade:
                xpan 0
                linear 2.0 xpan 360
                repeat
            show dark hair neu03 at xy
        else:
            show dark hair neu03 with dissolve
        
        $ diag = randomshuffle("(surprised) Hmm Interesting. Didn't see that one coming.",0.8,encrypt=encrypt_g3)
        g3  "[diag]"
        p  "So? Pizza?   "
        g3  "(embarassed) Actually it's chole bhature. he he"
        $ opt1 = randomshuffle("My mom used to make the best chole bhature.",0.75,encrypt=encrypt_g3)
        $ opt2 = randomshuffle("Wow. My turn to say didn't see that one coming ",0.85,encrypt=encrypt_g3)
        $ opt3 = randomshuffle("And Rajma chawal? he he",encrypt=encrypt_g3)
        if encrypt_g3 != False:
            $ style.say_dialogue = style.edited
        menu:

            "[opt1]":
                $ diag = randomshuffle("Everyone's Mom does the best cooking. I'm sorry 'used to' ?",0.8,encrypt=encrypt_g3)            
                g3 "[diag]"
                $ diag = randomshuffle("Ah yeah. Well she left me some years back. I don't even know if she is dead or alive.",0.8,encrypt=encrypt_g3)
                p  "[diag]"
                $ diag = randomshuffle("Sorry, don't bother yourself  ",0.8,encrypt=encrypt_g3)
                p  "[diag]"
                $ style.say_dialogue = style.normal
                show dark hair sad01
                g3  "Oh I'm sorry. I didn't know.    "
                g3  "To be honest, I kind of understand how you feel.  "
                p  "Your mom also left you ?    "
                g3  "(embarrased) Not exactly. But i spend all my time with my cook. You could even say she raised me.    "
                p  "Guess we both miss Chole Bhature too much eh?  "
                
                show dark hair smi01 with dissolve
                g3  "(Laughing) Yeah, now you made me hungry            "
                
                $ confidence_meter += 10
                # > Confidence boost. Show Khushi blushing. 


            "[opt2]":
                $ diag = randomshuffle("What?",0.7,encrypt=encrypt_g3)
                g3  "[diag]"
                $ diag = randomshuffle("I didn't expect you to say that that's all?",0.7,encrypt=encrypt_g3)
                p  "[diag]"
                
                show dark hair ang
                g3  "(shouting)I am an INDIAN GIRL at hearttttt.   "
                $ diag = randomshuffle("uhh yeah sure.",0.7,encrypt=encrypt_g3)
                p   "[diag]"
                
                n  "That's cringy"
                # > > (Khushi indifferent) Confidence lowers

                $ confidence_meter -= 5


            "[opt3]":

                show dark hair smi01 with dissolve
                g3 "Ya that toooo.  "
                $ diag = randomshuffle("So how often do you get to eat ?  ",0.6,encrypt=encrypt_g3)
                p  "[diag]"
                $ style.say_dialogue = style.normal
                g3  "Once every 2-3 months.    "
                $ diag = randomshuffle("uhh. Wow, you have my respect. Unbelievable.",0.9,encrypt=encrypt_g3)
                p  "[diag]"

                #> Khushi happy.Confidence level increases.
                $ confidence_meter += 5
        $ style.say_dialogue = style.normal
        scene pub2 with fade
        show dark hai neu01
    
        stop music fadeout 1.0
    
        if confidence_meter >= 35:
            call win_ending pass(girl = g3)
            jump the_end_happy
        else:
            call loss_ending pass(girl = g3)
            jump the_end_sad


    
    label win_ending(girl):
        play music "sounds/bgm/8.ogg"
        if girl == g1:
            show pink hair smile04
        if girl == g2:
            show ros_waraia2
        if girl == g3:
            show dark hair smi02
        girl "Anyways, I had a wonderful time."
        p "Sure,me too. Hey are you free tomorrow afternoon"
        girl  "mmmmm"
        girl  "(softly) yeah"
        if girl == g1:
            p  "well, lets have a good old gujrati thali then."
        if girl == g2:
            p  "Well, maybe we can  rewatch Koi Mil Gaya then."
        if girl == g3:
            p  "Well, we can maybe try out this Chole Bhatura stand then?"

        girl "Sounds like a date, done 😊"
        return

    label loss_ending(girl):
        play music "sounds/bgm/monika-end.ogg"
        scene bar_exit
        if girl == g1:
            show pink hair neutral02
        if girl == g2:
            show ros_ikaria3
        if girl == g3:
            show dark hair neu03
        girl  "Well, I have to go."
        p  "(low confidence) umm okay."
        return

    label the_end_happy:
    scene endhappy
    n "Wow , I'm so giddy right now. HeHe , I guess it's important to try new things , no point in living in the past."
    jump the_end

    label the_end_sad:
    scene startdark
    n "Hmm .. looks like this was a waste of time after all , back to the same old depressing shell ...."
    jump the_end

    label the_end:
    n "The End, thanks for playing."
    return

image blackflash:

    Solid("#000")
    alpha 0.0
    linear 0.25 alpha 0.4
    # linear 0.75 alpha 0.6
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

transform xy:
    parallel:
        xalign 0.0 yalign 1.0
        pause 1.0
        xalign 1.0
        pause 1.0
    parallel:
        # xalign 0.0 yalign 1.0
        # alpha 1.0
        linear 1.0 alpha 0.0
        # pause .5
        linear 1.0 alpha 1.0
        # pause .5
    repeat
transform wobbly:
    xtile 3
    xzoom .75 yzoom 1.25
    linear 1.0 xzoom 1.25 yzoom .75
    linear 1.0 xzoom .75 yzoom 1.25
    repeat
 