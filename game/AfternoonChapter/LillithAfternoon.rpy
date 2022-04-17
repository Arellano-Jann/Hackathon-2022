label lilith_afternoon:
    play music "audio/stardewheavy.opus"
    #scene bg eating_area fade
    #show btggf pride
    
    play sound "audio/shame loud.mp3"
    show btggf cheeky
    btggf "So anyway yeah, I've done things I'm ashamed of."

    show btggf neutral
    menu:
        btggf "We should probably grab some food... what do you feel like having?"

        "Pizza in a cup":
            play sound "audio/mm soft.mp3"
            btggf "This is pretty good."

        "Pizza in a cup but tastier":
            play sound "audio/oh yeah.mp3"
            show btggf loving
            btggf "This is so good!! YUM!!!"
    
    play sound "audio/smth in pizza i think.mp3"
    show btggf angry
    btggf "Ugh... I think there was something... in that pizza..."

    show btggf cheeky
    menu:
        btggf "I don't feel so good..."

        "Leave her":
            show btggf angry
            btggf "After everything we did together?? Are you kidding me??"
            btggf "You're scum."

            play sound "audio/ugh.mp3"
            show btggf cheeky
            btggf "I don't know why I ever thought you'd be any good for me."

            show btggf angry
            btggf "Now you're going to pay."

            $ lilith_flag = False
            jump ending_scenes

        "Help her":
            play sound "audio/spit.mp3"
            "You spit in her mouth to make her feel better."

            show btggf angry
            "She sits there in silence for a second."

            "..."
            "......"
            "........."

            play sound "audio/awooga.mp3"
            show btggf loving
            btggf "AWOOGA!!"
        
            play sound "audio/gurgle.mp3"
            btggf "{i}gurgles{/i}"
            
            show btggf neutral
            btggf "Just what I needed."

    show btggf cheeky
    btggf "I don't normally do this..."
    btggf "But I'd like to show you something..."

    $ lilith_evening_flag = True
    $ lilith_flag = True
    jump evening