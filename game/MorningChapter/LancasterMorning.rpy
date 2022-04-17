label lancaster_morning:

    scene zoom morning
    with Fade(0.5, 1.0, 0.5)

    p "{i}Phew, made it just on time.{/i}"
    p "{i}I hope I don't really get smited. I still have a life ahead of me.{/i}"
    p "{i}But even if I do get smited at least I get to see my favorite teacher today.{/i}"

    # show lancaster neutral
    dL "Hello class!"
    dL "I see that [name] is late yet again..."

    menu:
        "I'm sorry, I'm just... distracted":
            blah.
        ""
    
    jump lancaster_afternoon