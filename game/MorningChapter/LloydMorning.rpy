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

    # play sound uhhh
    
    p "Nothing! I didn't say anything!"
    p "I just need some help with my homework... yes homework!"
    p "That is if you can help me out!"

    menu:
        lloyd "I would but"
        #play sound uhhh


    $ lloyd_morning_flag = True
    jump afternoon
