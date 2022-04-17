# points
$ goodpts = 0;
$ badpts = 0;

label lloyd_morning:
    # play background music
    scene kc morning
    with fade
    
    show lloyd happy
    lloyd "Hey [name]! It's nice to see you here!"
    lloyd "To what do I owe the pleasure?"

    p "You know..."
    p "...same old same old"
    p "maybe looking for something more than the typical"

    show lloyd neutral
    # play sound uhhh
    
    p "Nothing! I didn't say anything!"
    p "I just need some help with my homework... yes homework!"
    p "That is if you can help me out!"

    lloyd "I would but I uhhhh have physics homework to do"
    show lloyd happy
    menu:
        lloyd "I can help you out some other time though"

        "He needs to help me now!":
            # badpts += 1
            p "You have to help me, I don't care, you are super smart so you don't need to do physics"
            show lloyd angry
            lloyd "You are so rude! Fine! But this is the last time I will ever help you!"
        
        "Try to convince him, he's a busy man":
            # goodpts += 1
            p "But I would really appreciate it, you are literally the smartest person in the entire world!"
            show lloyd uwu
            #play sound oh i'm not that smart
            lloyd "... you're too kind... alright alright I'll help you out"

    p "Great!...Let's get going!"

    # $ lloyd_morning_flag = True
    # jump afternoon
    jump lloyd_afternoon
