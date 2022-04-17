label lancaster_bad_ending:
    play music "audio/Simple Minds - Don't you forget about me (instrumental).opus" fadein 0.5 volume .2

    scene black
    with fade

    play sound "audio/d/right.mp3"
    show dl peeved
    dL "I don't think you should be here..."
    dL "I'm officially expelling you from my class!"

    play sound "audio/d/but leave it alone.mp3"
    dL "So leave it alone."

    # Zeus
    scene galaxy
    with fade
    play music "audio/thunder.opus" fadein 1 volume .2

    show zeus
    z "How disappointing..."
    z "Did you really think you could go after a professor?"
    z "SHAMEFUL!"
    z "You deserve your fate."

    jump end_credits