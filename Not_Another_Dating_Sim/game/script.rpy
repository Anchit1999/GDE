# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define p = Character("[name]")
define h = Character("Hero")
define i = Character("Hero1")


# The game starts here.
# p is player

label start:

    e "Hi, welcome to our humble game. Before you begin please tell us your name."

    python:
        name = renpy.input(_("What's your name?"))

        name = name.strip() or __("Lord Voldemort")

    e "Hi great thanks for joining us on this journey [name]"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene pub2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show dark hair ang
    with fade

    h "I am angry"
    hide dark hair ang

    show dark hair ann01
    with dissolve
    h "I am annoyed01"
    hide dark hair ang01

    show dark hair ann02
    with fade
    h "I am annoyed02"
    hide dark hair ang02

    show dark hair neu01
    with pixellate
    h "I am Neutral01"
    hide dark hair neu01

    show dark hair neu02
    with hpunch
    h "I am Neutral02"
    hide dark hair neu02

    show dark hair sad01
    with blinds
    h "I am sad01"
    hide dark hair sad01

    show dark hair sad02
    with squares
    h "I am sad02"
    hide dark hair sad02

    show dark hair smi01
    with zoomin
    h "I am smi01"
    hide dark hair smi01

    show dark hair smi02
    with vpunch
    h "I am smi01"
    hide dark hair smi02

    
    label selectgame:

    e "Select the minigame you wish to play"


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

    e "Your Score increased by 10"

    return
