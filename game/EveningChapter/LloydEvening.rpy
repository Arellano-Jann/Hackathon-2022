label lloyd_evening:
    # play background music
    scene den no table
    with fade

    show lloyd happy
    play sound "audio/l/moan2.mp3" volume 1.5
    lloyd "ahhhh, that was deeellliiiccciiiooouuusss!!"
    p "Tell me about it! I am so stuffed!"
    p "Will you still be able to help me finish my homework?"
    play sound "audio/l/sure.mp3" volume 2
    lloyd "Let's get back to the KC then"

    scene kc night
    with fade

    show lloyd neutral
    p "This CS project is really killing me right now!"
    p "I feel like I haven't showered for days!"
    
    play sound "audio/l/im a cs major.mp3" volume 2
    show lloyd disgusted
    p "But you're like, so smart"
    p "obviously you're not smelling as bad as me becuase you don't take as long as I do to finish the homework"

    show lloyd uwu
    play sound "audio/l/im not that smart.mp3" volume 2
    
    lloyd "But anyways, I'll just show you what I did"




    $ lloyd_flag = True
    $ lloyd_flag = False # set to False for bad ending
    jump evening