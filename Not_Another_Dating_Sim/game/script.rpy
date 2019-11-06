# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define p = Character("[name]")
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

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy


    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    
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
