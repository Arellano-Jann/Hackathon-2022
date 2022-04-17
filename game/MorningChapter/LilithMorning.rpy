label lilith_morning:
    scene joe morning
    play music "audio/stardew.opus" fadein 0.5
    
    play sound "audio/ugh.mp3"
    show btggf angry
    l "Ugh... Another shitty day."

    show btggf neutral
    l "Oh... uh... hello?"

    play sound "audio/eyes are up here.mp3"
    show btggf angry
    l "My eyes are up here, buddy."

    show btggf cheeky
    l "Whatever."

    menu:
        p "{i}I should make a good first impression...{/i}"
        
        "Make a rude comment":
            p "Is that a halloween costume?"
            
            show btggf angry
            play sound "audio/halloween.mp3"
            l "Ugh! No. I just dress like this."

            show btggf cheeky
            play sound "audio/phase dad.mp3"
            l "You sound just like my dad."

        "Make a kind comment":
            p "You're so hot..."

            play sound "audio/creepy.mp3"
            l "You're being creepy..."

            show btggf neutral
            play sound "audio/thx ig.mp3"
            l "But thanks... I guess?"
    
    play sound "audio/ugh.mp3"
    show btggf cheeky
    l "Wow, don't even ask for my name?"

    show btggf neutral

    p "I'm sorry! Um... my name is [name]. What's yours?"

    l "That's more like it."

    play sound "audio/mm soft.mp3"
    lil "I'm Lilith."

    show btggf cheeky
    lil "But everyone calls me the... 'btggf'..."

    play sound "audio/ugh.mp3"
    show btggf angry
    btggf "Don't ask why."

    menu:
        p "{i}This seems like a sensitive subject for her...{/i}"

        "Ask her why":
            play sound "audio/laugh medium2.mp3"
            show btggf neutral

            play sound "audio/laugh long.mp3"
            show btggf angry

            btggf "You asked for it..."

            $ lilith_flag = False
            jump ending_scenes

        "Leave it alone and ask what her major is":
            play sound "audio/mm soft.mp3"
            show btggf neutral
            btggf "Thanks for dropping it."

    play sound "audio/mm soft.mp3"
    #show btggf proud
    btggf "Believe it or not, I'm an AMAZING artist."

    show btggf neutral
    menu:
        btggf "Do you maybe want to grab food sometime? I can show you my work."

        "Yes":
            play sound "audio/understand me.mp3"
            show btggf loving
            btggf "I knew you'd understand me!"

            show btggf neutral
            btggf "Let's do it."

        "No":
            play sound "audio/i knew it.mp3"
            show btggf cheeky
            btggf "I knew it..."

            show btggf angry
            btggf "I knew it!"
            btggf "You asked for it..."

            $ lilith_flag = False
            jump ending_scenes
    
    p "Let's go right now!"

    play sound "audio/nice medium.mp3"
    show btggf loving
    btggf "I love the enthusiasm!"

    play sound "audio/putting on docs.mp3"
    show btggf neutral
    btggf "Let me put my docs on... my doc martens?"

    $ lilith_afternoon_flag = True
    jump afternoon