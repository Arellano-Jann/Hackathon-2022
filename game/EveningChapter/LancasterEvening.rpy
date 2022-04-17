label lancaster_evening:
    play music "audio/AC_DC - You Shook Me All Night Long (Instrumental).opus" fadein 0.5 volume .2
    scene kc night
    with fade

    "{i}You spent the rest of the day feeling bad for what happened earlier...{/i}"
    "{i}Suddenly, you see a familiar face.{/i}"

    play sound "audio/d/uhhwhy.mp3"
    show dl peeved
    dL "Uhh... why are you here?"

    menu:
        p "{i}This is my last chance!{/i}"

        "Confess your feelings":
            p "I just... like you!!"

            play sound "audio/d/notgoodpractice.mp3"
            dL "That's highly inappropriate and not good practice."

            jump lancaster_bad_ending
        
        "Admit you really just need an A and wanted to get on his good side":
            play sound "audio/d/right.mp3"
            show dl neutral
            dL "Right. That makes a lot of sense, [name]."
    
    play sound "audio/d/ill do that.mp3"
    show dl happy
    dL "I'm glad we were able to talk about this."

    show dl neutral
    dL "Let's discuss this further tomorrow."

    jump lancaster_good_ending