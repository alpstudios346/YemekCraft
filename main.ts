namespace SpriteKind {
    export const Cake = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite3, otherSprite3) {
    info.changeLifeBy(-15)
    info.changeScoreBy(10)
    otherSprite3.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Cake, function (sprite, otherSprite) {
    info.changeLifeBy(5)
    info.changeScoreBy(10)
    otherSprite.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite2, otherSprite2) {
    info.changeLifeBy(1)
    info.changeScoreBy(1)
    otherSprite2.destroy()
})
function randomAssets () {
    melon = sprites.create(assets.image`melon`, SpriteKind.Food)
    melon.x = randint(0, scene.screenWidth())
    melon.y = randint(0, scene.screenHeight())
    carrot = sprites.create(assets.image`carrot`, SpriteKind.Food)
    carrot.x = randint(0, scene.screenWidth())
    carrot.y = randint(0, scene.screenHeight())
    chance = randint(0, 100)
    if (chance < 20) {
        cake = sprites.create(assets.image`cake`, SpriteKind.Cake)
        cake.x = randint(0, scene.screenWidth())
        cake.y = randint(0, scene.screenHeight())
    } else {
        creeper = sprites.create(assets.image`enemy`, SpriteKind.Enemy)
        creeper.x = randint(0, scene.screenWidth())
        creeper.y = randint(0, scene.screenHeight())
    }
}
let creeper: Sprite = null
let cake: Sprite = null
let chance = 0
let carrot: Sprite = null
let melon: Sprite = null
let level = 0
let inventory: number[] = []
info.setLife(100)
info.startCountdown(500)
let steve = sprites.create(assets.image`steve`, SpriteKind.Player)
steve.setStayInScreen(true)
controller.moveSprite(steve)
scene.setBackgroundColor(6)
game.onUpdateInterval(2000, function () {
    randomAssets()
})
