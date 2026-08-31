@namespace
class SpriteKind:
    Cake = SpriteKind.create()

def on_on_overlap(sprite3, otherSprite3):
    info.change_life_by(-1)
    info.change_score_by(15)
    otherSprite3.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    info.change_score_by(10)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Cake, on_on_overlap2)

def on_on_overlap3(sprite2, otherSprite2):
    info.change_score_by(1)
    otherSprite2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

def randomAssets():
    global melon, carrot, chance, cake, creeper
    melon = sprites.create(assets.image("""
        melon
        """), SpriteKind.food)
    melon.x = randint(0, scene.screen_width())
    melon.y = randint(0, scene.screen_height())
    carrot = sprites.create(assets.image("""
        carrot
        """), SpriteKind.food)
    carrot.x = randint(0, scene.screen_width())
    carrot.y = randint(0, scene.screen_height())
    chance = randint(0, 100)
    if chance < 20:
        cake = sprites.create(assets.image("""
            cake
            """), SpriteKind.Cake)
        cake.x = randint(0, scene.screen_width())
        cake.y = randint(0, scene.screen_height())
    else:
        creeper = sprites.create(assets.image("""
            enemy
            """), SpriteKind.enemy)
        creeper.x = randint(0, scene.screen_width())
        creeper.y = randint(0, scene.screen_height())
def calculate_level(xp: number):
    return xp / 10
creeper: Sprite = None
chance = 0
cake: Sprite = None
carrot: Sprite = None
melon: Sprite = None
level = 0
inventory: List[number] = []
info.set_life(3)
info.start_countdown(60)
melon = sprites.create(assets.image("""
    melon
    """), SpriteKind.food)
carrot = sprites.create(assets.image("""
    carrot
    """), SpriteKind.food)
cake = sprites.create(assets.image("""
    cake
    """), SpriteKind.Cake)
steve = sprites.create(assets.image("""
    steve
    """), SpriteKind.player)
steve.set_stay_in_screen(True)
controller.move_sprite(steve)
scene.set_background_color(6)

def on_update_interval():
    randomAssets()
game.on_update_interval(2000, on_update_interval)
