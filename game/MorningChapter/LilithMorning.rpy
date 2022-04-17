label lilithmorning:
    scene bg joe morning
    play music "audio/stardewheavy.opus" loop fadein 0.5 volume 0.75
    
    play sound "ugh.mp3"
    show btggf angry
    l "Ugh... Another shitty day."

    show btggf neutral
    l "Oh... uh... hello?"

    play sound "eyes are up here.mp3"
    show btggf angry
    l "My eyes are up here, buddy."

    show btggf cheeky
    l "Whatever."

    menu:
        p "{i}I should make a good first impression...{/i}"
        
        "Make a rude comment":
            p "Is that a halloween costume?"
            
            show btggf angry
            play sound "halloween.mp3"
            l "Ugh! No. I just dress like this."

            show btggf cheeky
            play sound "phase dad.mp3"
            l "You sound just like my dad."

        "Make  a kind comment":
            p "You're so hot..."

            play sound "creepy.mp3"
            l "You're being creepy..."

            show btggf neutral
            play sound "thx ig.mp3"
            l "But thanks... I guess?"
    
    play sound "ugh.mp3"
    show btggf cheeky
    l "Wow, don't even ask for my name?"

    show btggf neutral

    p "I'm sorry! Um... my name is [name]. What's yours?"

    l "That's more like it."

    play sound "mm soft.mp3"
    lil "I'm Lilith."

    show btggf cheeky
    lil "But everyone calls me the... 'btggf'..."

    play sound "cant even.mp3"
    show btggf angry
    btggf "Don't ask why."

    menu:
        p "{i}This seems like a sensitive subject for her...{/i}"

        "Ask her why":
            play sound "laugh medium2.mp3"
            show btggf neutral

            play sound "laugh long.mp3"
            show btggf angry

            btggf "You asked for it..."

            #satanic ritual 
        "Leave it alone and ask what her major is":
            blah