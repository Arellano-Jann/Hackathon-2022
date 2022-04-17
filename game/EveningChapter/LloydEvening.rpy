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
    p "Obviously you're not smelling as bad as me because you don't take as long as I do to finish the homework"

    show lloyd uwu
    play sound "audio/l/im not that smart.mp3" volume 2
    lloyd "You're too generous"

    show lloyd happy
    lloyd "But anyways, I'll just show you what I did"

    p "Whoa Whoa Whoa!"
    p "What's that tab I see?"
    p "uhhh... Octopus videos?"

    play sound "audio/l/ehh.mp3"
    show lloyd uwu
    lloyd "uhhh... that's not mine!"

    menu:
        p "{i}hmmm I'm not sure if he's actually serious about it{/i}"

        "Should I be grossed out?":
            $ badpts += 1


        "I should get him to watch some with me":
            $ goodpts += 1


    if(badpts > goodpts):
        jump lloyd_bad_ending
    elif(goodpts > badpts):
        jump lloyd_good_ending
    # $ lloyd_flag = True
    # $ lloyd_flag = False # set to False for bad ending
    # jump evening