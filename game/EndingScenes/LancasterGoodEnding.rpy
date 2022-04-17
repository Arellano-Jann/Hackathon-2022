label lancaster_good_ending:
    scene zoom morning
    with fade

    show dl happy
    dL "Good morning, [name]."

    play sound "audio/d/gpa.mp3"
    show dl neutral
    dL "So what's your gpa?"

    p "I'll admit that it's not very good..."

    dL "I understand."

    play sound "audio/d/wewannahavecontroloverthat.mp3"
    dL "We want to have control over that."

    play sound "audio/d/right.mp3"
    dL "Right, tell you what."
    dL "Because of your efforts, I will give you an A in my classes."

    show dl happy
    dL "You deserve it, [name]!"

    play sound "audio/d/talk about things.mp3"
    show dl neutral
    dL "I appreciate your honesty."

    # Zeus
    scene galaxy
    with fade
    play music "audio/thunder.opus" fadein 1 volume .2

    show zeus
    z "Good for you! ...except you didn't get a date."
    z "Although... I suppose I'll be kind today."
    z "After all, you learned the lesson of honesty!"
    z "I'll call it a win."

    jump end_credits