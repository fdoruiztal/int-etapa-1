let lex_2: game.LedSprite = null
let lex_1: game.LedSprite = null
let lex: game.LedSprite = null
let clark = game.createSprite(0, 2)
basic.forever(function () {
    while (input.buttonIsPressed(Button.AB)) {
        clark.change(LedSpriteProperty.Y, 1)
        basic.pause(100)
    }
    while (input.buttonIsPressed(Button.A)) {
        clark.change(LedSpriteProperty.X, -1)
        basic.pause(100)
    }
    while (input.buttonIsPressed(Button.B)) {
        clark.change(LedSpriteProperty.X, 1)
        basic.pause(100)
    }
    while (input.logoIsPressed()) {
        clark.change(LedSpriteProperty.Y, -1)
        basic.pause(100)
    }
})
loops.everyInterval(3000, function () {
    lex = game.createSprite(randint(1, 4), randint(0, 4))
    lex_1 = game.createSprite(randint(1, 4), randint(0, 4))
    lex_2 = game.createSprite(randint(1, 4), randint(0, 4))
    basic.clearScreen()
})
