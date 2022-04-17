label lancaster_morning:
    play music "audio/AC_DC - You Shook Me All Night Long (Instrumental).opus" fadein 0.5 volume .2
    scene zoom morning
    with fade

    p "{i}I hope I don't really get smited. I still have a life ahead of me.{/i}"
    p "{i}But even if I do get smited at least I get to see my favorite teacher today.{/i}"

    show dl neutral
    dL "Hello class!"

    show dl peeved
    play sound "audio/d/right.mp3"
    dL "I see that [name] is late yet again..."

    menu:
        "I'm sorry, I'm just... distracted":
            play sound "audio/d/uhh.mp3"
            dL "Uhhh..."
            
            play sound "audio/d/dont need to know.mp3"
            dL "I don't need to know."

            show dl neutral
            play sound "audio/d/wewannahavecontroloverthat.mp3"
            dL "We wanna have control over that."

            play sound "audio/d/right.mp3"
            dL "Right..."

            show dl peeved
            play sound "audio/d/umm.mp3"
            dL "I think you should leave, [name]."

            jump lancaster_bad_ending

        "It won't happen again!":
            play sound "audio/d/notgoodpractice.mp3"
            dL "That's not good practice."
    
    play sound "audio/d/right.mp3"
    show dl neutral
    dL "Just don't let it happen again."
    dL "Meet me after class, I'd like to talk to you"

    p "I'm sorry da-- I mean... Dr. Canlaster."

    show dl peeved
    dL "..."

    play sound "audio/d/but leave it alone.mp3"
    show dl neutral
    dL "Anyways."

    play sound "audio/d/wecandothingslikethat.mp3"
    dL "Today we are going to talk about flip flops. This is actually a very intricate topic that's going to need your full, undivided attention."

    dL "This will also, more likely than not, end up on the final so don't say I didn't warn you."
    p "{i}Oh no. I've been worried about this unit the whole semester...{/i}"
    p "{i}I hope I can learn this to get a good score on the test...{/i}"

    scene zoom morning
    with fade
    
    play sound "audio/d/ucanmanipulate.mp3"
    show dl neutral
    dL "...you can manipulate..."

    scene zoom morning
    with fade

    play sound "audio/d/weretryingto.mp3"
    show dl neutral
    dL "...We're trying to..."

    scene zoom morning
    with fade

    play sound "audio/d/right.mp3"
    show dl neutral
    dL "Right. And that ends today's lecture, have a good day."
    dL "[name], come with me to my office hours. We need to work on your breadboard."
    
    jump lancaster_afternoon