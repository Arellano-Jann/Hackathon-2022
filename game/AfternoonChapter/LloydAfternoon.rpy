label lloyd_afternoon:
    # play background music
    scene kc night
    with fade

    show lloyd happy
    lloyd "[name], it's getting kinda late"
    show lloyd neutral
    lloyd "I could really use some food right now, got gonna lie"

    menu:
        p "{i}He must be hungry{/i}"

        "Suggest the Den":
            $ goodpts += 1
            p "Do you want to go to the Den?"
            p "I can swipe you in"
            play sound "audio/l/yum.mp3"
            lloyd "Sounds great! Let's go!"
        
        "Say nothing and hope he suggests a place":
            lloyd "How does Den food sound?"
            menu:
                p "{i}ugh Den food, but it's Lloyd{/i}"
                "Pretend to like Den":
                    $ goodpts += 1
                    p "Yum sounds so good right now"
                    show lloyd happy
                    lloyd "Great! Let's go then!"
                "Yuck! Hell nah!":
                    $ badpts += 1
                    p "YUCK! Hell nah! I'm not gonna be eating Den food!"
                    

    # $ lloyd_evening_flag = True
    # jump evening
    jump lloyd_evening