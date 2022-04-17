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
            p "EEWW! Who would ever watch such things!"
            play sound "audio/l/laugh.mp3" volume 2
            lloyd "oh..uhh.. of course it wouldn't be me"
            lloyd "It...it... it must've been one of my friends"
            show lloyd neutral
            play sound "audio/l/ahem.mp3" volume 1.5
            play sound "audio/l/hold on.mp3" volume 2
            lloyd "Hold up! You don't watch octopus videos?!?!"
            lloyd "They are so informational!"
            p "Uhhh... no they are not!"
            p "They are like the worst videos anyone could ever see!"
            lloyd "Then let's watch one so you become educated!"
            p "Heck no! I'm not gonna be watching that!"
            show lloyd angry
            play sound "audio/l/ur disgusting.mp3" volume 2
            lloyd "YOU KNOW WHAT!! I'M DONE WITH YOU!!"

            jump lloyd_bad_ending
            


        "I should get him to watch some with me":
            p "We could...uhhh...you know..."
            p "watch some videos"
            $ goodpts += 1
            show lloyd happy
            play sound "audio/l/u want to what.mp3"  volume 1.5
            lloyd ".... I mean we could"
            play sound "audio/l/i mean i guess.mp3"  volume 2
            lloyd "totally, we could check out what it's about"
            scene kc night
            with fade
            show lloyd uwu
            play sound "audio/l/detail on tentacles2.mp3" volume 2
            lloyd "..."
            p "ohh...uhhh...yeaaa"
            p "I guess.. I uhhh... never really noticed"
            play sound "audio/l/dont think i saw that.mp3" volume 2
            p "Nope...I don't think I have either"
            play sound "audio/l/what have I got into.mp3" volume 2
            lloyd "uhhh"
            p "Well... uhhhh... that is something...."
            play sound "audio/l/this seems like hentai.mp3" volume 1.5
            lloyd "I...uhhh... think we've watche denough for now"
            p "I totally agree"


    if(badpts > goodpts):
        jump lloyd_bad_ending
    elif(goodpts > badpts):
        jump lloyd_good_ending
    # $ lloyd_flag = True
    # $ lloyd_flag = False # set to False for bad ending
    # jump evening