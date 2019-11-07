# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define h = Character("Dhwani")
define i = Character("Hero1")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene pub2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show dark hair ang
    # with fade

    # h "I am angry"
    # hide dark hair ang

    # show dark hair ann01
    # with dissolve
    # h "I am annoyed01"
    # hide dark hair ang01

    # show dark hair ann02
    # with fade
    # h "I am annoyed02"
    # hide dark hair ang02

    # show dark hair neu01
    # with pixellate
    # h "I am Neutral01"
    # hide dark hair neu01

    # show dark hair neu02
    # with hpunch
    # h "I am Neutral02"
    # hide dark hair neu02

    # show dark hair sad01
    # with blinds
    # h "I am sad01"
    # hide dark hair sad01

    # show dark hair sad02
    # with squares
    # h "I am sad02"
    # hide dark hair sad02

    # show dark hair smi01
    # with zoomin
    # h "I am smi01"
    # hide dark hair smi01

    show pink hair ang01 at left
    show ros_akuwaraia1
    show male ang01 at right
    with vpunch
    h "I am smi02"
    # hide dark hair smi02
    call fifteen_game
    call simon pass (complete=10, toadd=2)

    # This ends the game.

    return
