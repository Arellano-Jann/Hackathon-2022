# points
$ goodpts = 0;
$ badpts = 0;

label lloyd_morning:
    scene kc morning
    with fade

    show lloyd happy
    lloyd "Hey [name]! It's nice to see you here!"
    lloyd "To what do I owe the pleasure?"

    p ""

    jump afternoon
