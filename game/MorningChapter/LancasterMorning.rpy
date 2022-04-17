label lancaster_morning:

    scene zoom morning
    with Fade(0.5, 1.0, 0.5)

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

        "It won't happen again!":
            #play sound "audio\dl\" that's not good practice
            dL "That's not good practice."
    
    dL "Just don't let it happen again."
    dL "Meet me after class, I'd like to to you"
    p "I'm sorry daddy--I mean Dr. Lancaster."
    dL "..."
    dL "Anyways."
    dL "Today we are going to talk about flip flops. This is actually a very intricate topic that's going to need your full, undivided attention."
    dL "This will also more likely than not end up on the final so don't say I didn't warn you."
    p "{i}Oh no. I've been worried about this unit the whole semester. I hope I can learn this to get a good score on the test and please my Lan--I mean Mr--I mean Dr. Lancaster.{/i}"
    
    jump lancaster_afternoon