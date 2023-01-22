# Ursina is an open source Python Game Engine!!!
# It is built on top of the Panda 3d Engine.
# Panda 3d uses Python, C, & C++
# Ursina GitHub Below
# https://github.com/pokepetter/ursina
# https://www.ursinaengine.org/api_reference.html
from ursina import *

# The Python import random module in Python defines a series of functions 
# for generating or manipulating random integers.
# The uniform() method returns a random floating number between the two 
# specified numbers (both included).
from random import uniform

from ursina import curve

# Import first person controller from ursina!
# Enables ability to controll from the first person movement in a 3d space
# and at the same time give us a 1st person perspective.
from ursina.prefabs.first_person_controller import FirstPersonController

def input(key):
    if key == "left mouse down":
        Audio("sounds/shot.wav")
        Animation("assets/spark", parent=camera.ui, fps=5, scale=.1, position=(.1, -.05), loop = False)

        for wasp in wasps:
            if wasp.hovered:
                destroy(wasp)

        for spider in spiders:
            if spider.hovered:
                destroy(spider)

# Asset credit
# https://free3d.com/3d-model/base-mesh-ready-to-be-rigged-15483.html
class Wasp(Button):
    def __init__(self, x, y, z):
        super().__init__ (
            parent=scene,
            model="assets/man.obj",
            scale=.1,
            position=(x, y, z),
            rotation=(0, 90, 0),
            collider="box"
        )

# Asset credit
# https://free3d.com/3d-model/skull-v3--785914.html
class Spider(Button):
    def __init__(self, x, y, z):
        super().__init__ (
            parent=scene,
            model="assets/skull.obj",
            scale=.1,
            position=(x, y, z),
            rotation=(0, 90, 0),
            collider="box"
        )

app=Ursina()

# We need a sky, or if the player looks up, it will be plain white,
# or a void of nothing. 
Sky()

# Player is the playable character. A player 1.
# Not yet sure what y and y origin are yet. 
# This is the reccomended setting. Need to check, 
# once models are running. Mess with it and see
# what happens.
player=FirstPersonController(y=2, origin_y=.5)

# We need a ground. Even though this is a FPS game,
# users can still look down at the ground. You also need a base 
# for your level design and coordinates.
# 100 on the X axis, 1 on the y there is no need to have a thicker
# y axis unless we want to add hills or mountains. 
# 100 on the z axis to get a nice square to work with in this level.
# Picking green as a color, to represent a grass like enviorment.
# Not sure what "white cube texture is"
# Not sure what texture scale is. 
# Texture Scale set to 100 on the y and 100 on the x axis
# Not sure whar a collider is 
ground=Entity(model='plane', scale=(100, 1, 100), color=color.green, texture="white_cube", 
    texture_scale=(100, 100), collider='box')

wall_1=Entity(model="cube", collider="box", posistion=(-8, 0, 0), scale=(8, 5, 1), rotation=(0, 0, 0),
    texture="brick", texture_scale=(5,5), color=color.rgb(255, 128, 0))

wall_2 = duplicate(wall_1, z=5)
wall_3 = duplicate(wall_1, z=10)

wall_4=Entity(model="cube", collider='box', posistion=(-15, 0, 10), scale=(1, 5, 20), rotation=(0, 0, 0),
    texture="brick", texture_scale=(5,5), color=color.rgb(225, 128, 0))

class HookBlock(Button):
    def __init__(self, position):
        super().__init__(
            parent = scene,
            model="cube",
            color=color.brown,
            position=position
        )
        self.on_click = Func(player.animate_position, self.position, duration=.5, curve=curve.linear)

hookblock_1 = HookBlock(position=(3, 3, 3))

# Gun Model Credits 
# https://quaternius.itch.io/50-lowpoly-guns
gun=Entity(model="OBJ/AssaultRifle_1.obj", parent=camera.ui, scale= .5, color=color.gray, position=(.6, -.5), 
    rotation=(0, 70, 5))

num=6
wasps=[None]*num
spiders=[None]*num
for i in range(num):
    wx=uniform(-12, -7)
    wy=uniform(.1, 1.8)
    wz=uniform(.8, 3.8)
    wasps[i]=Wasp(wx, wy, wz)
    wasps[i].animate_x(wx+.5, duration=.2, loop=True)
    sx=uniform(-12, -7)
    sy=uniform(.1, 1.8)
    sz=uniform(5.8, 8.8)
    spiders[i]=Spider(sx, sy, sz)
    spiders[i].animate_x(sx+.5, duration=.2, loop=True)

app.run()