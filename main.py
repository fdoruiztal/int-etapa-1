lex_2: game.LedSprite = None
lex_1: game.LedSprite = None
lex: game.LedSprite = None
clark = game.create_sprite(0, 2)

def on_forever():
    while input.button_is_pressed(Button.AB):
        clark.change(LedSpriteProperty.Y, 1)
        basic.pause(100)
    while input.button_is_pressed(Button.A):
        clark.change(LedSpriteProperty.X, -1)
        basic.pause(100)
    while input.button_is_pressed(Button.B):
        clark.change(LedSpriteProperty.X, 1)
        basic.pause(100)
    while input.logo_is_pressed():
        clark.change(LedSpriteProperty.Y, -1)
        basic.pause(100)
    if clark.is_touching(lex):
        lex.delete()
        game.add_score(1)
basic.forever(on_forever)

def on_every_interval():
    global lex, lex_1, lex_2
    lex = game.create_sprite(randint(1, 4), randint(0, 4))
    lex_1 = game.create_sprite(randint(1, 4), randint(0, 4))
    lex_2 = game.create_sprite(randint(1, 4), randint(0, 4))
loops.every_interval(3000, on_every_interval)
