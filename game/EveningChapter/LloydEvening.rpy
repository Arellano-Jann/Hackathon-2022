label lloyd_evening:
    # play background music
    scene den no table
    with fade

    show lloyd happy
    play sound "audio/l/moan.mp3"
    lloyd "ahhhh, that was deeellliiiccciiiooouuusss!!"
    p "Tell me about it! I am so stuffed!"
    p "Will you still be able to help me finish my homework?"
    play sound "audio/l/sure.mp3"
    lloyd "Let's get back to the KC then"

    scene kc night

    $ lloyd_flag = True
    $ lloyd_flag = False # set to False for bad ending
    jump evening