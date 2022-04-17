label lloyd_afternoon:
    scene black
    with fade
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
            show lloyd happy
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
                    play sound "audio/l/mm.mp3"
                    lloyd "Great! Let's go then!"

                "Yuck! Hell nah!":
                    $ badpts += 1
                    p "YUCK! Hell nah! I'm not gonna be eating Den food!"
                    play sound "audio/l/uegh 1.mp3"
                    show lloyd angry
                    lloyd "Well then... what do YOU want to eat [name] then?"
                    p "{i}SHOOT! I shoulnd't have said that! I might end up getting smited{/i}"
                    p "Actually...Den food sounds really good!"
                    play sound "audio/l/uh huh.mp3"
                    show lloyd disgusted
                    lloyd "uh huh, sure..."
                    p "I'm sorry, I'm just so hungry that I wasn't thinking straight"
                    p "Let's get going"
    
    scene black
    with fade

    scene den no table
    with fade

    play sound "audio/l/yum.mp3"
    show lloyd happy
    lloyd "mmmm...the food is quite good today"
    
    p "I agree... Den food is never this good"
    p "But anyways, do you play League?"

    play sound "audio/l/laugh.mp3"
    lloyd "Do I play League?!"
    lloyd "I sure do!"
    lloyd "Show me your rank"

    p "uhhhh...sure"

    show lloyd disgusted
    play sound "audio/l/wow ur rank is shit.mp3"
    lloyd "wow... who would've known"

    menu:
        p "{i}Is that an insult?{/i}"

        "Brush it off":
            p "I know.. I just don't play as much anymore"
            p "You know with college and everything"
            show lloyd happy
            play sound "audio/l/laugh.mp3"
            lloyd "For sure, for sure... I get it, but ayyy you're not too bad"
        
        "Stand up for yourself":
            $ badpts += 1
            p "*gasp* How dare you!"
            p "What the fuck! You are literally the worst!"
            p "Why am I even friends with you!"
            show lloyd angry
            play sound "audio/l/shut it.mp3"
            lloyd "Gosh, can't you take a joke"
            lloyd "I was just kidding"
            p "{i}Shoot, I screwed up!{/i}"
            p "Sorry... I'm so so so sorry"
    show lloyd neutral
    lloyd "Let's just finish eating"

    scene black
    with fade

    # $ lloyd_evening_flag = True
    # jump evening
    jump lloyd_evening