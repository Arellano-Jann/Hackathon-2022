# This file is the before anything happens
# Ask user for name

# name of the character.

define l = Character("???")
define lil = Character("Lillith")
define btggf = Character("BTGGF")
define lloyd = Character("Lloyd")
define dL = Character("Dr. Lancaster")
define p = Character("[name]")
define z = Character("Zeus")

# Background

# The game starts here by asking user name.
# https://sonalsart.com/how-do-i-enter-text-in-renpy/#:~:text=How%20do%20I%20enter%20text%20in%20Renpy%3F%20With,be%20saved%20in%20a%20variable%20or%20otherwise%20processed.
label start:
    play music "audio/misato.opus" fadein 0.5
    # asks user for their name
    $ name = renpy.input("Hello, before we begin, What is your name?")
    $ name = name.strip()

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene kc morning
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # show z 

    # Dream...
    z "[name]! [name]!"
    z "You lonely, lonely disgraceful disappointment!"
    z "I sentence!!! I sentence YOU!"
    z "If by the end of the day, YOU don't find a date... YOU SHALL NOT LIVE"
    z "So by the time the clock strikes midnight, YOU shall be smited!!"
    z "Turned to ashes and forever forgotten"
    z "[name]! [name]! YOU HAVE BEEN WARNED!!" with pause(1.5)

    # should fade to black
    image black = Solid("#00000000")


    # wakes up in bedroom, remember to put in pic
    p "{i}huhhhh...{/i}"

    menu:
        p "{i}What am I doing?{/i}"
        "Freak out":
            p "{i}AHHHHH!!! I'M GONNA DIE!!! {/i}"
            p "{i}I AM NEVER GONNA GET A DATE!!{/i}"
    
        "Be confident":
            p "{i}It's ok....{/i}"
            p "{i}I got this... {/i}"
            p "{i}I WILL LIVE!{/i}"
    
    p "{i}What's the worst that could happen?{/i}"
    p "{i}It's only college{/i}"

    p "{i}oh shoot! I have to go to school!{/i}"
    p "{i}AND I'M LATE! {/i}"

    menu:
        p "{i}Where do I need to go?{/i}"

        "Go to class":
            p "{i}I need to get to class!!{/i}"
            p "{i}I AM GOING TO BE SO LATE TO CLASS!{/i}"
            jump lancaster_morning

        "Go to the WPEB":
            p "{i}I wonder if Lloyd's at WPEB{/i}"
            p "{i}I could really use his help on this homework{/i}"
            jump lloyd_morning
        
        "Go to the Joe":
            p "{i}Well I'm already late{/i}"
            p "{i}Might as well grab some food at the Joe or something{/i}"
            jump lillithmorning

    # retur_creditsn


label end_credits:
    return