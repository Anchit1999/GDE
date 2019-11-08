##### The game screen.
screen fifteen_scr:

    ##### Timer.
    if timer_on:
        timer 1.0 action If(fifteen_timer > 0, [SetVariable("fifteen_timer", fifteen_timer-1), Return("smth")], Return("time_is_up") ) repeat True
        text str(fifteen_timer) xalign 0.1 yalign 0.1

    ##### Game field.
    frame:
        xalign 0.5 yalign 0.5
        background Solid("#ccc") #Frame("pic_1.png", 5, 5) # The background might be set as a solid color or a frame, that uses predefined displayable or file name, also you can delete this line to have default frame background.

        grid grid_width grid_height spacing 0:
            for every_tile in tiles_list:
                if every_tile["tile_value"] == empty_tile_value and not fifteen_is_solved:
                    null

                else:
                    button:
                        #####
                        #
                        # To use just numbers (classic fifteen game) - uncomment next 4 lines and comment out lines that are used to show an image.
                        # It is neccessary to set the size of buttons.
                        # (The background might be set as a solid color or a frame, that uses predefined displayable or file name, also you can delete this line to have default button background.)
                        #xminimum 70 xmaximum 70
                        #yminimum 70 ymaximum 70
                        #background Solid("#c00")
                        #text str(every_tile["tile_value"]) xalign 0.5 yalign 0.5
                        #
                        #####


                        #####
                        #
                        # Next lines are used to show an image.
                        left_padding 0 right_padding 0 top_padding 0 bottom_padding 0
                        left_margin 0 right_margin 0 top_margin 0 bottom_margin 0
                        add LiveCrop( ( (every_tile["tile_value"]-1)%grid_width*tile_width,
                                        (every_tile["tile_value"]-1)//grid_width*tile_height,
                                        tile_width,
                                        tile_height),
                                        chosen_img)
                        #
                        #####


                        action [ If (every_tile["tile_number"] not in top_row,
                                   true = If (tiles_list[every_tile["tile_number"]-grid_width]["tile_value"] == empty_tile_value,
                                     true = [SetDict( tiles_list[every_tile["tile_number"]-grid_width], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                     false = None),
                                   false = None),
                                 If (every_tile["tile_number"] not in bottom_row,
                                   true = If (tiles_list[min(len(tiles_list)-1, every_tile["tile_number"]+grid_width)]["tile_value"] == empty_tile_value,
                                     true = [SetDict( tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+grid_width))], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                     false = None),
                                   false = None),
                                 If (every_tile["tile_number"] not in left_column,
                                   true = If (tiles_list[every_tile["tile_number"]-1]["tile_value"] == empty_tile_value,
                                     true = [SetDict( tiles_list[every_tile["tile_number"]-1], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                     false = None),
                                   false = None),
                                 If (every_tile["tile_number"] not in right_column,
                                   true = If (tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+1))]["tile_value"] == empty_tile_value,
                                     true = [SetDict( tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+1))], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                     false = None),
                                   false = None), Return("smth")
                               ]

    ##### A button that will let player quit the game (especially useful if there will be no timer to finish the game).
    textbutton "Quit" action Jump("quit_fifteen_game") xalign 0.9 yalign 0.1

    ##### A button that will show the whole image, should be used only if game uses images (not numbers).
    textbutton "Show/hide image" action If( renpy.get_screen("full_image"), Hide("full_image"), Show("full_image") ) xalign 0.5 yalign 0.1


##### Screen that contains an image to show (not useful in classic fifteen game).
#
screen full_image:
    add chosen_img xalign 0.5 yalign 0.5 at pic_trans


transform pic_trans:
    alpha 0.0 zoom 0.7
    on show:
        parallel:
            linear 1.0 alpha 1.0
        parallel:
            linear 0.6 zoom 1.2
            linear 0.4 zoom 1.0
    on hide:
        linear 0.5 alpha 0.0
#
#####


label fifteen_game:

    ##### Game settings.
    #
    # Let's set the size of game field in tiles, for example 9 tiles (3 x 3).
    $ grid_width = 3
    $ grid_height = 3

    # Next 4 lines are used to set an image to solve (could be deleted for clasic fifteen game).
    # It is recommended that all images will be smaller than screen size.
    $ chosen_img = renpy.random.choice ( ("images/fifteen_minigame/abstract.png", "images/fifteen_minigame/flower.png") )
    $ chosen_img_width, chosen_img_height = renpy.image_size(chosen_img)
    $ tile_width = chosen_img_width/grid_width
    $ tile_height = chosen_img_height/grid_height
    #

    # Some useful calculations:
    $ top_row = []
    python:
        for i in range(0, grid_width):
            top_row.append (i)
    $ bottom_row = []
    python:
        for i in range(0, grid_width):
            bottom_row.append ( (grid_width*(grid_height-1)+i) )
    $ left_column = []
    python:
        for i in range(0, grid_height):
            left_column.append (grid_width*i)
    $ right_column = []
    python:
        for i in range(0, grid_height):
            right_column.append (grid_width*(i+1)-1)


    # Let's set the game field - all the tiles are on their places.
    $ tiles_list = []
    python:
        for i in range (0, grid_height):
            for j in range (0, grid_width):
                tiles_list.append ( {"tile_number":(i*grid_width+j), "tile_value":(i*grid_width+(j+1))} )


    # Let's set a missed tile - it can be a random one or the last one (as in classic fifteen game).
    $ empty_tile_value = renpy.random.randint ( 1, grid_width*grid_height )
    #$ empty_tile_value = grid_width*grid_height
    #

    # Some variables:
    # will let us control if the missed tile should be shown
    $ fifteen_is_solved = False
    # sets the timer to make game more difficult
    $ fifteen_timer = 300
    # will let us control the timer
    $ timer_on = False

    # This will show the game screen.
    show screen fifteen_scr

    # To be sure that puzzle can be solved, just randomly move some tiles.
    # This process could be shown to player - uncomment the line that sets the pause between moves.
    # The number of moves should be great enought to shuffle tiles good,
    # also it should be odd to avoid situation when random moves will bring all the tiles back on their starting positions.
    $ shuffle_moves = 21
    label tiles_shuffle:
        if shuffle_moves >0:
            python:
                possible_moves_list = []
                for j in tiles_list:
                    if j["tile_value"] == empty_tile_value:
                        if j["tile_number"] not in top_row:
                            possible_moves_list.append ("top")
                        if j["tile_number"] not in bottom_row:
                            possible_moves_list.append ("bottom")
                        if j["tile_number"] not in left_column:
                            possible_moves_list.append ("left")
                        if j["tile_number"] not in right_column:
                            possible_moves_list.append ("right")
                        move_tile = renpy.random.choice (possible_moves_list)
                        if move_tile == "top":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]-grid_width]["tile_value"]
                            tiles_list[j["tile_number"]-grid_width]["tile_value"] = empty_tile_value
                        elif move_tile == "bottom":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]+grid_width]["tile_value"]
                            tiles_list[j["tile_number"]+grid_width]["tile_value"] = empty_tile_value
                        elif move_tile == "left":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]-1]["tile_value"]
                            tiles_list[j["tile_number"]-1]["tile_value"] = empty_tile_value
                        elif move_tile == "right":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]+1]["tile_value"]
                            tiles_list[j["tile_number"]+1]["tile_value"] = empty_tile_value
                        shuffle_moves -= 1
                        #renpy.pause(0.1)           # If used pause should be not so long.
                        renpy.jump("tiles_shuffle")

    # Now we can start the timer.
    $ timer_on = True

    # The game loop.
    label fifteen_game_loop:
        $ result = ui.interact()
        $ fifteen_timer = fifteen_timer
        if result == "time_is_up":
            jump fifteen_lose
        python:
            for j in tiles_list:
                if j["tile_value"]-1 != j["tile_number"]: # will continue the game if at least one tile is not in its place
                    renpy.jump("fifteen_game_loop")
        jump fifteen_win

label fifteen_win:
    # This will turn off the timer.
    $ timer_on = False
    $ renpy.pause(0.1, hard = True)
    $ renpy.pause(0.1, hard = True)

    # This will show the missed tile in its place.
    $ fifteen_is_solved = True
    # hide ros_waraia1
    show ros_waraia1
    g2 "Wow you were better than I hoped. I'm impressed"
    $ confidence_meter += 10

    hide screen fifteen_scr
    return

label fifteen_lose:
    $ timer_on = False
    $ renpy.pause(0.1, hard = True)
    $ renpy.pause(0.1, hard = True)
    # hide ros_waraia1
    show ros_defa1
    g2 "It's ok. Better Luck next time"
    $ confidence_meter += 5
    
    hide screen fifteen_scr
    return
    # jump fifteen_game

label quit_fifteen_game:
    hide screen fifteen_scr
    
    # hide ros_waraia1
    show ros_defa1
    g2 "It's ok. Better Luck next time"
    $ confidence_meter += 5
    
    return
