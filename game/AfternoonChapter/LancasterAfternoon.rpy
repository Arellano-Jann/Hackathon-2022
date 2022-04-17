label lancaster_afternoon:
    scene breadboard
    with fade

    play sound "audio/d/right.mp3"
    show dl neutral
    dL "Right. Thanks for coming to office hours, [name]."

    play sound "audio/d/wewannahavecontroloverthat.mp3"
    dL "We wanna have control over these skills."

    play sound "audio/d/oksilence.mp3"
    dL "Okay... let's get started."

    menu:
        p "{i}This is really important...{/i}"

        "Purposefully mess up":
            "{i}You roughly put a chip in, bending the pins.{/i}"

            show dl peeved
            play sound "audio/d/freshman.mp3"
            dL "Are you a freshman or a senior?"

            play sound "audio/d/dont need to know.mp3"
            dL "I don't need to know any of that."

            play sound "audio/d/notgoodpractice.mp3"
            dL "That's not good practice."

            play sound "audio/d/thisisourstuffdontmesswit.mp3"
            dL "This is our stuff, don't mess with it."

            play sound "audio/d/baddog.mp3"
            show dl neutral
            dL "Okay... maybe this isn't the best major for you."

            play sound "audio/d/ucanmanipulate.mp3"
            show dl peeved
            dL "Manipulate those two wires and cross them together."

            scene black
            with fade

            "{i}You follow his instructions and cross them, instantly being electrocuted"

            z "How disappointing..."
            z "Did you really think you could go after a professor?"
            z "SHAMEFUL!"
            z "You deserve your fate."
            z "I wish I could have smited you myself, but I guess the Doctor did that for me."

            jump end_credits

        "Put in effort":
            "{i}You move your hands quickly and confidently, putting together the circuit{/i}"

            play sound "audio/d/wecandothingslikethat.mp3"
            show dl blushing
            dL "We can do things like that, but you're missing one step."
    
    scene breadboard touch
    with fade

    "{i}Your hands brush together on the breadboadrd.{/i}"

    play sound "audio/d/uhh.mp3"
    show dl blushing
    dL "Uhh..."

    play sound "audio/d/whatrwedoinguhh.mp3"
    dL "What we're doing uhh..."

    play sound "audio/d/notgoodpractice.mp3"
    show dl peeved
    dL "It's not good practice."

    play sound "audio/d/right.mp3"
    dL "You should leave."

    jump lancaster_evening