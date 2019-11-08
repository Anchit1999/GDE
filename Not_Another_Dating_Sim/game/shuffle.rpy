init python:
    import random

    def shuffletext(dialogue):
        s = dialogue.split(' ')
        random.shuffle(s)
        output = ""
        return output.join(s)