import play
from random import randint


play.screen.height = 600
play.screen.width = 1000

background='./img/menu/background.jpeg'

fon=play.new_image(image=background)

k_rain= ['./img/rain/sprite_0.png',
            './img/rain/sprite_1.png',
            './img/rain/sprite_2.png',]



one_of_rain_k=['./img/menu/one/sprite_0.png',
                './img/menu/one/sprite_1.png',
                './img/menu/one/sprite_2.png',
                './img/menu/one/sprite_3.png',
                './img/menu/one/sprite_4.png',
                './img/menu/one/sprite_5.png',
                './img/menu/one/sprite_6.png',
               './img/menu/one/sprite_7.png']
number_k_one=5


rain_list=[]

button_play_k=['./img/menu/button/sprite_0.png','./img/menu/button/sprite_1.png']

button_play=play.new_image(image=button_play_k[0],y=100)


one_of_rain=play.new_image(image=one_of_rain_k[number_k_one],y=100)
def back():
    rain = play.new_image(image=k_rain[randint(0, 2)], size=50, x=randint(play.screen.left, play.screen.right + 400),
                          y=play.screen.top)
    rain_list.append(rain)
    for i in rain_list:
        if i.y > play.screen.bottom and i.x > play.screen.left:
            i.x -= 5
            i.y -= 7
        else:
            i.hide()
            del (i)

def buttons():
    if button_play.is_touching(play.mouse):
        button_play.image = button_play_k[1]
    else:
        button_play.image = button_play_k[0]

@play.repeat_forever
def do():
    # global number_k_one
    # if number_k_one==7:
    #     number_k_one=0
    # else:
    #     number_k_one+=1
    #
    # one_of_rain.image=one_of_rain_k[number_k_one]

    back()



    buttons()






play.start_program()