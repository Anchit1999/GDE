# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define p = Character("[name]")
define r = Character("Rohit")
define n = Character(" ",what_prefix="{i}", what_suffix="{/i}")

define g1 = Character("g1") # pink hair
define g2 = Character("g2") # gunny girl
define g3 = Character("g3") # dark hair


# The game starts here.
# p is the player

label start:

    $ confidence_meter = 25

    n "Hi, welcome to our humble game. Before you begin please tell us your name."

    python:
        name = renpy.input(_("What's your name?"))

        name = name.strip() or __("Lord Voldemort")

    n "Hi great thanks for joining us on this journey name"
    
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

    r "Arre why are you so concerned?" 
  
    p "(stuttering) I have avoided all humanity uptill now and you want me to talk to 3 beautifull girls."
    # with Fade(5.0) zorder 10
    show blackflash zorder 50
    # > p shaking. Depict by bluring the screen or something

    n "So Rohit pulled me and I was totally uncomfortable"
    hide male smi02
    
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
    r  "Welcome back. Guys this is my friend [name]. We have been together since childhood. He is an engineer at XYZ company."    
    show male smi02 at mz2
    p  "(meekly) Hi !!"

    show ros_akuwaraia1 at rosz1
    g2 "Oh my God, Relax man. We arent going to eat you. By the way I'm g2. I'm working to protect people like you.  "
    show ros_akuwaraia1 at rosz2

    show male smi02 at mz1
    r  "(confused) Sorry ?"
    show male smi02 at mz2

    show ros_akuwaraia1 at rosz1
    g2 "I mean I'm a corporate lawyer. Hehe "
    show ros_akuwaraia1 at rosz2

    n  "That was a really poor joke."

    show pink hair smile01 at phz1
    g1 "Well I'm g1. I am a school teacher"
    show pink hair smile01 at phz2

    show dark hair smi01 at dhz1
    g3 "And you must already know me. I am the famous actress ...."
    show dark hair smi01 at dhz2

    p "Sorry I dont know you. But I feel I have seen you somewhere. "

    show dark hair ang at dhz1
    g3 "(tad angry) g3. Im in the UNESCO ad that everyone has been talking about. Gosh have you not followed my Instagram page alreadyyyyy."
    show dark hair ang at dhz2

    show male smi02 at mz1
    r "And that's dinner. I am really hungry. Anyone up for some starters."
    
    r "(pulling p closer), this is your chance."

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

    # g1_story
    label g1_story:

        $ played_pong_minigame = False
        # show g1 neutral
        scene pub2 with dissolve
        show pink hair neutral01
        
        n "g2 , g3 and Rohit leave for starters"

        p  "Ummm  "
        g1  "Uhhh  "
        p  "(nervous laughter) Uhh  "
        show pink hair neutral02
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
                show pink hair smile01
                g1 "Yeah not many people realize how hard it is.  "
                p  "But I am sure it's rewarding.   "
                g1 "Yeah sure is. Always feel happy to see a successful student.  "
                p  "Yeah most important job in the world.  "

                $ confidence_meter += 10

                

            "Yeah you look the part. A typical History teacher. Not too smart. Ha Ha":
               
                # n "Bad Choice"
                
                # show g1 annoyed
                show pink hair annoyed01
                g1 "Well those who forget history are doomed to repeat it.  "
                p "Like reading pointless escapades of kings before. He He  "
                g1 "Its this exact reason for which I teach History.  "
                p "Well I hope you teach something real like Science.  "
                
                # jump bad_choice
                $ confidence_meter -= 5

            
            "Well you got it easy with the job. Personally the easiest job in history. Ha Ha":
                # n "Worst Choice"

                # show g1 angry/upset
                show pink hair ang01
                g1 "Well it's not as easy as it looks."
                p  "Really? Well all you have to do is look good and read from the book. No ?"
                g1  "Seems like you didnt have good teachers.  "
                p  "Well they dressed up well and read well so i guess they were pretty good."

                
                $ confidence_meter -= 10
        
        show pink hair neutral01
        p  "Anyways you got any hobbies ? "
        g1  "Yeah I like cooking. I also like to watch bollywood movies."
        p  "Oh what is your favourite dish to cook ?  "
        g1  "I like to cook Gujrati food."
        
        menu:

            "Oh thats pretty lame. You should try more awesome things like pasta and burger.  ":
                
                show pink hair annoyed01
                g1  "Well to each their own. "
                p  "Anything not pasta is so stupid. Go for pasta only. "    
                show pink hair annoyed02
                g1  "(visibly annoyed).Hmm sure "

                $ confidence_meter -= 10
                # > Confidence hit. Show g1 angryp             
                
            "Wow thats actually interesting. I would love to know more.":
                
                show pink hair smile01
                g1  "Oh sure (visibly excited). Its very different to what you would find elsewhere.  "
                p  "Really how ?  "
                g1  "Well we like everything sweet. So you find a bit of sweetness in everything we eat.  "
                p  "Wow, that is different. The only sweet ive ever had is in form of ice cream. Would love to try sometime.  "
                g1  "Sure. Next time we meet,ill try to get something for you."

                $ confidence_meter += 5

                # > Show Dhwani excited. Confidence becomes little better


            "You mean dhokla and thepla. Yeah sweet just like you  ":

                show pink hair smile03
                g1  "(gets horny) Well you are not wrong about the food.   "
                p  "I actually like Gujrati food. I had some Gujarati friends in college.    "
                g1  "Wow can you speak gujrati then?.  "
                p  "Tārā māṭē kaṁīpaṇa.(Anything for you) "

                $ confidence_meter += 10

                #> Dhwani all red. Confidence skyrockets. Can show bit of shivering

        show pink hair smile01
        g1  "Oh Wow , is that people playing air hockey, come on let's go and play too."

        ## Flash_Back
        scene pub2 with fade
        # Scene change - arcade game.

        n  "Your thoughts turn back to 26.05.2008 the last truly happy day of your life. Your parents had taken you out to a gaming arcade for your 11th birthday "

        n  "Ah it was so much fun playing all the games with your mom dad and sister, such a happy family."

        # Scene change parents fighting

        n  "However that night you couldn't sleep with all the excitement , and you heard raised voices from your parent's room"

        n  "You peeked and saw your dad throwing a vase at your mom ...... nothing was ever the same again."
        
        # Scene change - present
        scene pub2 with fade
        n "Do you still want to play air hockey ?"
        
        menu:
            
            "Yes":
                show pink hair smile01
                p "Yeah come on let's play. (in a shaky voice)."
                # scene - changes to karoake
                
                call pong_minigame
                
                $ played_pong_minigame = True
                
            "No":
                show pink hair annoyed01
                g1  "Come on don't be a spoilsport."
                p   "No I don't want to play. I don't like it at all."
                show pink hair annoyed02
                $ confidence_meter -= 10

        # n "The End"
        show pink hair neutral01
        p  "Anyways what do you like to do on a lazy afternoon?  "
        g1 "I like to drink coffee and read a book.  "

        menu:

            "Me too. I love to read as well.":
                show pink hair smile01
                g1  "Wow what do you read.    "
                p  "Well I like to read biographies. My favourite was the one on Steve Jobs by Walter Issacson.  "
                g1  "Oh i like to read on the Mughal Period.  "
                p  "Guess we are alike on this one."
                show pink hair smile03
                $ confidence_meter += 10
                # > > Confidence boost. Show Dhwani blushing. 

            "Hmm. Chetan Bhagat am I right ?":
                
                show pink hair annoyed01
                g1  "Well I dont like his novels.  "
                p   " Wow, you must be mad then  "
                show pink hair ang01
                g1  "Oh really."
                $ confidence_meter -= 10

                # > Show Dhwani angry.


            "That's so borrriiinnnnggg.":

                g1 "Ok then what do you like?  "
                p  "Watching netflix  "
                g1  "Well i find it boring.  "
                p  "Guess we agree to disagree.  "

            #Dhwani indifferent.Confidence level same.
        
        if confidence_meter >= 35:
            call win_ending pass(girl = g1)
            jump the_end
        else:
            call loss_ending pass(girl = g1)
            jump the_end


    label g2_story:

        $ played_puzzle_minigame = False
        
        scene pub2 with dissolve
        show ros_defa1

        p  "Ummm  "
        g2  "So hotshot XYZ, you must be smart  "
        p  "(nervous laughter) Uhh. what can i say. he he  "
        g2  "Well you could tell start by telling me where you did your graduation from?    "
        p  "Uh Uh umm"
        show ros_akuwaraia1
        g2  "Man relax. I am not gonna sue you.    "
        p  "Huh? Oh haha. I am actually from IIT-D.."
        g2  "Delhi. Not too bad. Im impressed.    "
        p  "No actually. Its Dharwad. he he "
        show ros_defa1
        g2  "Oh I am sorry. Well i hope they atleast have chairs xD. "
        p  "Uhmm uhh  "
        p  "So......  "
        p  "So corporate law and all? Must be taxing.  "
        g2  "Yeah its not easy. Really stressful. "

        menu:

            "So is it like Suits. Making mergers and looking smart.":
                
                g2  "Well not sure about smart. But I do love wearing those dresses."
                p  "He He. Btw have you finished the show?"
                g2  "Damn right xD. Yeah completed in a weekend. "
                p  "Wow you are a fan.   "

                $ confidence_meter += 10
                # > > Confidence boost. Show Dhwani blushing. 

            "Yeah, keep the guys happy. Tough indeed.He he":
                    
                g2  "You do know right what you just said,Right?.  "
                p  "Uhm did I say something bad?  "
                g2  "Its people like you who make it so hard for girls to survive. Its a real shame.  "
                p  "Im so sorry. I didnt mean to say that."
                
                $ confidence_meter -= 5

                # > Show Dhwani excited. Confidence becomes little better


            "Yeah being a secretrary must be tough.":

                g2  "Excuse me. I have done law from NLU.Ever heard of it?Im a junior associate at DEF law firm  "
                p  "Oh I just thought..  "
                g2  "And even if I was a secretrary. Even then I deserve to be respected no?  "
                p  "Sorry. I didnt mean it that way. I didnt mean to hurt you. "

                $ confidence_meter -= 10

        p  "Anyways you got any hobbies? "
        g2  "Yeah I like travelling. I recently travelled to the States.  "
        p  "uhh which states?  "
        g2  "United States of America stupid.    "
        p  "Oh my bad. Is that how they say it? He he."
        g2  "What about you?"

        menu:

            "Uhmm. Nothing much really. Watching netflix I guess?":
                
                g2  "Wow. Dont you get bored ?    "
                p  "uhmm there are good shows like sacred games,etc. So keeps me busy.  "
                g2  "(unimpressed).Hmm sure"

                $ confidence_meter -= 10
                # > > > Confidence hit. Show labdhi unimpressed. 
 

            "Well me too. Though I havent really gone beyond the shores yet.":
                    
                g2 " Well I havent roamed around India much. Whats your favorite place.    "
                p " I like mountains. I find Manali to be quite nice.    "
                g2 " Yeah but still its so lame unlike the Alps.  "
                p " Maybe. Every place has its own charm. So...  "
                g2 "Yeah but still everything foreign is so much better."

                $ confidence_meter -= 5

                # > Show excited. Confidence becomes little lower


            " Uhmm. Does playing cricket count? He he":

                g2 "(unimpressed).Typical Indian hobby.   "
                p  "Well its fun. Did you follow the world cup?    "
                g2  "Yeah Yeah a bit. Everyone was following so i saw a bit.  "
                p  "You dont follow any sports ?  "
                g2  "Not really. Work takes up all my time."

                $ confidence_meter += 5
        
        p  "Hey what's that popping out of your coat pocket?"
        g2  "Ah this thing , it's a sliding puzzle. I use it as a stress-buster. Do you wanna try it ?"  
        
        # Relevant cutscene backstory

        n  "Stress buster huh , well I wish I had something of this sorts when I was younger "

        n  "Anything to distract me from the rants of my drunk,senseless father. And forget the string of affairs my mom had. All this happening the year of my board exams."

        n  "Hmm , no p you are stronger than this , don't live in the past , don't it will only bring you pain. Think of positive things. "

        g2 "Hello !! , Earth to p , Earth to p. Do you wanna try it."

        menu:
            
            "Yes":

                p "Yeah sure I will give it a try. (in a shaky voice)."
                # scene - changes to karoake
                
                call fifteen_game
                
                $ played_puzzle_minigame = True
                
            "No":

                g1  "Come on don't be a spoilsport."
                p   "No I don't want to do it. I don't like it at all."

                $ confidence_meter -= 10

        p  "So whats your favorite movie?"
        g2  "Oh I love rom coms and sci-fi. So my favurite movies are Princess Diaries and Interstellar.  "
        p  "Nice. Yeah even like I to watch movies.  "
        g2  "Oh whats your favourite one?"
        
        menu:

            "Well i loved Koi Mil Gaya. It really inspired me as a kid.":
                
                g2  "Interesting. Its basically a ripoff of ET,but sure.    ?"
                p  "Actually thats not entirely true. It was initially a plan of Satyajit Ray in collaboration with some American production house. Then those guys actually leaked the script to Steven Spielberg.  ?"
                p  "Even Rakesh Roshan mentioned it in his press conference.  ?"
                g2  "I have to say, i didnt see that one coming.    ?"
                p  "Actually its a shame as to how often we Indians dont get credit. Radio, Airplanes, the list goes on.  ?"
                g2  "(embarrased) I feel embarassed to not know about this.?"
                            

                $ confidence_meter += 10
                # > Confidence boost. Show Labdhi blushing. 


            "My favourite is Iron Man":
                
                g2  "Oh so you are one of those Marvel fanboys.    "
                p  "Its not just that. It inspired a young kid to become an engineer and is pretty entertaining  "
                g2  "You arent wrong there to be honest.        "
               
                $ confidence_meter -= 5

                # > (Labdhi indifferent) Confidence a bit high


            "I liked Hera Pheri.":

                g2 "Isnt it a bit too forced and misogynist.  "
                p  "Well, the idea of a movie is to entertain and its a good light hearted one watch.  "
                g2  "Still, I think there shouldnt be any room for regressive thoughts.    "
                p  "Guess we agree to disagree. He he"
                
                $ confidence_meter -= 10
                # > Labdhi indifferent.Confidence level lowers.
    
        if confidence_meter >= 35:
            call win_ending pass(girl = g2)
            jump the_end
        else:
            call loss_ending pass(girl = g2)
            jump the_end

    label g3_story:
        
        $ played_karoake_minigame = False

        p  "Ummm  "
        g3  "Sooooo  "
        p  "(nervous laughter) Uhh. sooo.... uhh  "
        g3  "Well are you gonna talk or stay like that ?    "
        p  "Uh Uh umm"
        g3  "Gosh are you gonna stay dumb like that?    "
        p  "Oh sorry. ummm"
        g3  "OMG, this so weird. Anyways are you on instagram?    "
        p  " umm. Yeah yeah but I dont use it too often.  "
        g3  "Oh well then follow me. Or you can even not, I mean I have 30k followers.   "
        p  "But everyone counts right?    "
        g3  "(embarrased) Oh yeah totally. Please follow me.   "
        p  "So how much time on average do you spend there?  "
        g3  "Well, mostly my manager manages my account. But i like to read comments and give fans what they want."
        
        menu:

            "Well its important to be connected to them.":
                
                g3  "If the fans turn on you, then its really hard to gain back their trust.    "
                p  "True that. I guess all celebrities must feel that way.   "
                g3  "Thats right. So why dont you do me a favor and follow me on Tiktok. My handle is cutiepie420.   "
                p  "umm uhh.    "
                g3  "Gosh you arent on TikTok are you?  "
                p  " sorry im not. umm uhh, I could follow you on Linkedin.  "
                g3  "You are such a nerd.              "

                $ confidence_meter -= 5
                # > > Confidence goes down. g3 unimpressed 


            "But shouldn't you focus more on other things like your acting.":
                
                g3  "I think I know whats important.    "
                p  "Sorry. I just meant since you are an actress, that should be your strength,right?    "
                g3  "(angry)Listen, just because you are an engineer and you think you are SO SMART, you dont get to tell me what I should do or what I shouldnt.   "
                p  "umm uhh.Sorry you are right I shouldnt.    "
                g3  "(apologetic)I am sorry, I shouldnt have shouted. "
                g3 "Its just theres so much pressure on me at the moment.   "
                p  " I understand. Its okay. Life is pretty hard on us sometimes isnt it?  "
                g3  "Yeah it sometimes feel like such a huge ******* mountain. Its unbearable.  "
                p  "Well mountains are meant to be climbed arent they?"
                
                $ confidence_meter += 10

                # > (Labdhi indifferent) Confidence a bit high


            "Well, that comes at cost of self respect doesnt it. He he":

                g3 "What do you know about self respect huh?  "
                p  "Oh i didnt mean to say..  "
                g3  "Do you even know what do I have to go through every single day? "
                p  "Sorry. I didnt mean it that way. I didnt mean to hurt you.    "
                g3  "(upset) what i have to listen every single day  "
                p  "Hey, listen i didnt mean to say like that. umm Im quite an idiot. Im really sorry"
                
                $ confidence_meter -= 10
                # > Labdhi indifferent.Confidence level lowers.
        
        p  "Anyways you got any hobbies? "
        g3  "I love dancing and singing.Ever since I was a kid, I used to find every opportunity I could, to dance.  "
        p  "ohh nice.  "
        g3  "What about you ?    "
        p  "uhh I dont know."
        g3  "Come on. I am trying to convince myself you are not as lame as you look.    "
        

        menu:

            "Uhmm. Nothing much really. Watching netflix I guess?":
                
                g3  "Whats your favorite show there?     "
                p  "Stranger Things. Its just ...  "
                g3  "(impressed). so cuuuuttttteeeeeee!!!!"
                p  "Uhm yeah, you could say that as well.  "
                g3  "Though its not much of a hobby. Unless you can win a quiz based on Netflix.  "
                p  "Maybe I could. I dont know  "
            
                $ confidence_meter += 5
            

            "I did do some acting in school. I guess you could count that.":
                
                g3  "Wow you mean like school plays.Yeah i used to be the star in them..    "
                p  "I wasnt any great. A bit here and there.     "
                g3  "Well as an accomplished actress I can tell you its not about the role, its about how you perform it.  "
                p  "uhh umm Yeah I guess you are right.   "
                g3  "To be honest, I didnt think you would be involved in acting."
                p  "No no, just a bit. He he     "

                # > Show Khushi smiling. Confidence increases.

                $ confidence_meter += 10


            " Uhmm. Does playing cricket count? He he":

                g3 "(unimpressed).Oh I just looovvveeee Virat Kohli.   "
                p  "Yeah he is such a good batsman. Its a strugg....    "
                g3  "He is so cute. I am so jealous of Anushka  "
                p  "You just like him because he is cute?  "
                g3  "Duh. Also his abbs. OMGGGG!!!!"

                # > Khushi smiles. Confidence decreases.  
                $ confidence_meter -= 5
        
        g3  "I love music , Come on let's go and do karoake"

        ## Flash_Back

        # Scene change - school event.

        n  "You suddenly had a flashback to your 7th grade annual function event."

        n  "You remember how you finally had the guts to go on stage and sing your hearts out, you had practiced and learnt all the lyrics."

        # Scene change - on stage public humiliation , people laughing two or three scenes.

        n  "But seeing the audience of over 500 , you forgot everything and ran away from the stage."

        n  "The jeering, taunts and bullying that you had to face the entire year. That was the year when you developed the stutter."
        
        # Scene change - present
        
        g3 "Come on let's go for karoake ?"
        
        menu:
            
            "Yes":

                p "Okay sure let's go."
                # scene - changes to karoake
                g3 "Go on it's your turn"

                call simon(complete=8, toadd=2)
                
                $ played_karoake_minigame = True

            "No":

                g3  "Come on don't be a spoilsport."
                p   "No I don't want to do karoake. I don't like it at all."

                $ confidence_meter -= 10

    
        p  "Anyways, umm   "
        g3  "What? You take hell lot of time to say things.    "
        p  "So whats your cheat day meal like?   "
        g3  "(surprised)Hmm Interesting. Didnt see that one coming."
        p  "So? Pizza?   "
        g3  "(embarassed) Actually its chole bhature.he he"
    
        menu:

            "My mom used to make the best chole bhature.":
                            
                g3 "Everyone's Mom does the best cooking. Im sorry used to?    "
                p  "Ah yeah. Well she left me some years back. I dont even know is she is dead or alive.    "
                p  "Sorry, dont bother yourself  "
                g3  "Oh Im sorry. I didnt know.    "
                g3  "To be honest, I kind of understand how you feel.  "
                p  "Your mom also left you ?    "
                g3  "(embarrased) Not exactly. But i spend all my time with my cook. You could even say she raised me.    "
                p  "Guess we both miss Chole Bhature too much eh?  "
                g3  "(Laughing) Yeah, now you made me hungry            "
                
                $ confidence_meter += 10
                # > Confidence boost. Show Khushi blushing. 


            "Wow. My turn to say didnt see that one coming ":
                
                g3  "What?     "
                p  "I didnt expect you to say that thats all?     "
                g3  "(shouting)I am a PUNJABI GIRL at hearttttt.   "
                p  "uhh yeah sure."
                n  "Thats cringy"
                # > > (Khushi indifferent) Confidence lowers

                $ confidence_meter -= 5


            "And Rajma chawal? he he":

                g3 "Ya that toooo.  "
                p  "So how often do you get to eat ?  "
                g3  "Once every 2-3 months.    "
                p  "uhh. Wow, you have my respect. Unbelievable.  "

                #> Khushi happy.Confidence level increases.
                $ confidence_meter += 5
    
    
    
        if confidence_meter >= 35:
            call win_ending pass(girl = g3)
            jump the_end
        else:
            call loss_ending pass(girl = g3)
            jump the_end


    
    label win_ending(girl):

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
        girl  "Well, I have to go."
        p  "(low confidence) umm okay."
        return

    label the_end:
    n "The End"


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
