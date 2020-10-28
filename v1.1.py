import play  # подключаем play

play.screen.height = 600
play.screen.width = 1000
play.set_backdrop((255, 50, 255))

back_sprite=[]
x = 0

direction='right'
number_k = 0
number = 0

box_img = './img/box.png'

k_sprite = ['./img/sprite/sprite_0.png',
            './img/sprite/sprite_1.png',
            './img/sprite/sprite_2.png',
            './img/sprite/sprite_3.png',
            './img/sprite/sprite_4.png',
            './img/sprite/sprite_5.png']
k_sprite_left=['./img/sprite/left/sprite_0.png',
            './img/sprite/left/sprite_1.png',
            './img/sprite/left/sprite_2.png',
            './img/sprite/left/sprite_3.png',
            './img/sprite/left/sprite_4.png',
            './img/sprite/left/sprite_5.png']

k_heli = ['./img/heli/heli0.png', './img/heli/heli1.png', './img/heli/heli2.png', './img/heli/heli3.png',
          './img/heli/heli4.png', './img/heli/heli5.png']
k_lava = ['./img/lava/lava1.png',
          './img/lava/lava1.png',
          './img/lava/lava2.png', ]

wall1 = play.new_image(image='./img/platform.png', x=-100, y=0, size=15)
wall2 = play.new_image(image='./img/platform.png', x=250, y=-200, size=15)
wall3 = play.new_image(image='./img/platform.png', x=400, y=130, size=15)
wall4 = play.new_image(image='./img/platform.png', x=350, y=-100, size=15)
wall5 = play.new_image(image='./img/platform.png', x=500, y=-100, size=15)
wall6 = play.new_image(image='./img/platform.png', x=650, y=-100, size=15)
wall7 = play.new_image(image='./img/platform.png', x=800, y=-100, size=15)
wall_list = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]

i = 31
j = 32
while play.screen.height - i > 0:
    box = play.new_image(image=box_img, x=play.screen.left + 32, y=play.screen.bottom + i)
    wall_list.append(box)
    box.start_physics(can_move=True, obeys_gravity=False, stable=True, friction=0)
    # box3 = play.new_image(image=box_img, x=play.screen.right - 8, y=play.screen.bottom + i)
    # box3.start_physics(can_move=False)
    while play.screen.width - j > 0:
        box2 = play.new_image(image=box_img, x=play.screen.left + j, y=play.screen.bottom + 30)
        box2.start_physics(can_move=True, obeys_gravity=False, stable=True, friction=0)
        box4 = play.new_image(image=box_img, x=play.screen.left + j, y=play.screen.top - 8)
        box4.start_physics(can_move=True, obeys_gravity=False, stable=True, friction=0)
        wall_list.append(box2)
        wall_list.append(box4)
        j += 40
    i += 40





sprite_box = play.new_box(color='black', x=0, y=53, width=17, height=40, transparency=100)

sprite = play.new_image(image=k_sprite[number_k], x=1000, y=50, size=20)

heli = play.new_image(image=k_heli[number], x=1000, y=50, size=600)

lava = play.new_image(image=k_lava[number], x=600, y=-269, size=600)
# tree = play.new_image('./img/tree.png', size=300, x=200, y=-200)

wall1.start_physics(can_move=True, obeys_gravity=False, stable=True, friction=0)
wall2.start_physics(can_move=True, obeys_gravity=False, stable=True, friction=0)
wall3.start_physics(can_move=True, obeys_gravity=False, stable=True, friction=0)
wall4.start_physics(can_move=True, obeys_gravity=False, stable=True, friction=0)
wall5.start_physics(can_move=True, obeys_gravity=False, stable=True, friction=0)
wall6.start_physics(can_move=True, obeys_gravity=False, stable=True, friction=0)
wall7.start_physics(can_move=True, obeys_gravity=False, stable=True, friction=0)

sprite_box.start_physics(can_move=True, stable=True, x_speed=0, y_speed=0, bounciness=0.1, friction=0, mass=10)

lava.start_physics(can_move=True, obeys_gravity=False, stable=True, friction=0)


wall_list.append(lava)

def update():
    global number, number_k,direction

    if number == 6:
        number = 0

    if number_k == 6:
        number_k = 0
    if direction=='right':
        sprite.image = k_sprite[number_k]
    else:
        sprite.image = k_sprite_left[number_k]
    lava.image = k_lava[number // 2]
    heli.image = k_heli[number]

    number += 1

def helicopter():
    if heli.x > -500:
        heli.show()
        heli.x -= 10
    else:
        heli.hide()


def keypads():
    global number_k,x, direction,sprite
    if play.key_is_pressed('space'):
        for wall in wall_list:
            if sprite_box.is_touching(wall) and sprite_box.y > wall.y:
                sprite_box.physics.y_speed = 50

    if play.key_is_pressed("d"):
        direction='right'


        number_k += 1

        if x>= 0:
            sprite_box.physics.x_speed = 0

            for wall in wall_list:
                wall.physics.x_speed = -10


        else:
            sprite_box.physics.x_speed = 10
            for wall in wall_list:
                wall.physics.x_speed = 0
            x += 5

    elif play.key_is_pressed("a"):
        direction='left'
        number_k += 1


        if x==0:
            for wall in wall_list:
                wall.physics.x_speed = 10

        else:
            sprite_box.physics.x_speed = -10
            for wall in wall_list:
                wall.physics.x_speed = 0

        x -= 5

    else:
        number_k = 0
        sprite_box.physics.x_speed = 0
        for wall in wall_list:
            wall.physics.x_speed = 0


def draw_platform(x,y):
    for wall in wall_list:
        if wall.x<play.screen.left:


            if wall.y==play.screen.bottom + 30:
                new_wall=play.new_image(image=box_img, x=play.screen.right+32, y=play.screen.bottom + 30)
                new_wall.start_physics(can_move=True, obeys_gravity=False, stable=True, friction=0)
                wall_list.append(new_wall)
            wall_list.remove(wall)

def spite_x_y():
    pass

@play.repeat_forever
async def do():
    global number_k, number, box2, x

    helicopter()

    keypads()
    update()
    draw_platform(x,wall_list)


    sprite.x = sprite_box.x - 6
    sprite.y = sprite_box.y - 3
    x=sprite.x//1


    await play.timer(seconds=1 / 90)


play.start_program()
