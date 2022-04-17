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
            #play sound "audio\dl\" umm?
            dL "Uhhh..."
            
            #play sound "audio/dl/" I don't need to know
            dL "I don't need to know."

        "It won't happen again!"
            #play sound "audio\dl\" that's not good practice
            dL "That's not good practice."
    

    
    jump lancaster_afternoon