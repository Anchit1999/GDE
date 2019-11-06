label simon(complete=8, toadd=2):
    $ sequence=[]
    $ yourguess=0
label simonturn:
    # add signs to the sequence, enlarging it each turn.
    $ seqiter=0
    python:
        for i in range(toadd):
            roll=renpy.random.randint(0,3)
            sequence.append(roll)
label simonshow:
    $ i=0
    while i<len(sequence):
        $ thesign=sequence[i]
        # display the actual sequence, sign by sign
        # .. neutral screen (all greyed out)
        show screen simonvoid
        $ renpy.pause(0.5, hard=True)
        hide screen simonvoid
        # ... a button is lighted on!
        show screen simondisplay
        # ... so, play the relative sound
        if thesign==0:
            play sound "sounds/music_minigame_sounds/a.wav"
        if thesign==1:
            play sound "sounds/music_minigame_sounds/b.wav"
        if thesign==2:
            play sound "sounds/music_minigame_sounds/c.wav"
        if thesign==3:
            play sound "sounds/music_minigame_sounds/d.wav"
        $ renpy.pause(0.5, hard=True)
        hide screen simondisplay
        $ i+=1
    $ i=0 # Yeah, the very cornerstone of the game is that line!!
label simonguess:
    $ thesign=sequence[i]
    call screen simoncheck
    $ dasign=_return
    if dasign=="bust":
        "Too slow!"
        return
    elif dasign!=thesign:
        "Oh no! You missed it!"
        return
    if dasign==thesign:
        $ i+=1
        if i==len(sequence):
            jump simonend
    jump simonguess
label simonend:
    if len(sequence)==complete:
        "You won!"
        return
    jump simonturn
    
screen simondisplay():
    text "SIMON SAYS..." xalign 0.5 yalign 0.2
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        if thesign==0:
            add "images/music_minigame/a.png"
        else:
            add "images/music_minigame/e.png"
        
        if thesign==1:
            add "images/music_minigame/b.png"
        else:
            add "images/music_minigame/e.png"
        
        if thesign==2:
            add "images/music_minigame/c.png"
        else:
            add "images/music_minigame/e.png"
        
        if thesign==3:
            add "images/music_minigame/d.png"
        else:
            add "images/music_minigame/e.png"
screen simonvoid():
    text "Let's see how good you are ..." xalign 0.5 yalign 0.2
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        for i in range(4):
            add "images/music_minigame/e.png"
screen simoncheck():
    timer 3.0 action Return("bust")
    bar value AnimatedValue(value=0, range=3, old_value=3, delay=3.0) xalign 0.5 xsize 500
    text "!! REPEAT !!" xalign 0.5 yalign 0.2
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        imagebutton idle "images/music_minigame/e.png" hover "images/music_minigame/a.png" action Return(0) activate_sound "sounds/music_minigame_sounds/a.wav"
        imagebutton idle "images/music_minigame/e.png" hover "images/music_minigame/b.png" action Return(1) activate_sound "sounds/music_minigame_sounds/b.wav"
        imagebutton idle "images/music_minigame/e.png" hover "images/music_minigame/c.png" action Return(2) activate_sound "sounds/music_minigame_sounds/c.wav"
        imagebutton idle "images/music_minigame/e.png" hover "images/music_minigame/d.png" action Return(3) activate_sound "sounds/music_minigame_sounds/d.wav"

