from PIL import Image, ImageDraw
import random

print("Dog")

visual_map = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
['W', ' ', 'W', 'W', ' ', 'W', 'W', 'S', 'W', 'W'],
['W', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', 'W'],
['W', ' ', ' ', ' ', ' ', ' ', 'R', 'C', ' ', 'W'],
['W', ' ', ' ', 'C', 'R', 'R', 'R', ' ', ' ', 'W'],
['W', ' ', 'C', 'C', 'R', 'R', 'R', ' ', ' ', 'W'],
['W', 'S', 'R', 'R', 'R', 'C', 'C', ' ', ' ', 'W'],
['W', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', 'W'],
['W', 'W', ' ', ' ', ' ', 'W', ' ', 'W', 'W', 'W'],
['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]

class Image_Maker:
    def __init__(self, size, our_list):
        red = (255,210,10)
        img_size = (size*10, size*10)
        im = Image.new("RGB", img_size)
        draw = ImageDraw.Draw(im)
        for i in our_list:
            j = 0
            while j < len(i):
                pos_y = 0
                if i[j] == "W":
                    draw.rectangle(((0, pos_y), (10, 10)), fill=red)
                    pos_y += 10
        im.save("C:/Users/iamja_000/Documents/GitHub/worldgen2/lemonsx.jpeg")



def pil_image():
    size = (100, 100)
    im = Image.new("RGB", size)
    draw = ImageDraw.Draw(im)
    #red = (255,210,10)
    position = (0, 0)
    position2 = (10, 10)
    draw.rectangle((position, position2), fill="red")
    position = (10, 0)
    position2 = (20, 10)
    draw.rectangle((position, position2), fill="blue")
    position = (20, 0)
    position2 = (30, 10)
    draw.rectangle((position, position2), fill="yellow")
    print(im)
    im.save("C:/Users/iamja_000/Documents/GitHub/worldgen2/lemonsyyy.jpeg")

print(visual_map)
#pil_image()

def pil_image_iterative():
    size = (100, 100)
    im = Image.new("RGB", size)
    draw = ImageDraw.Draw(im)
    position = (0, 0)
    position2 = (10, 10)
    colors = ["red", "blue", "yellow"]
    print("Iterating")
    while position2[0] <= 100:
        color_choice = random.choice(colors)
        draw.rectangle((position, position2), fill=color_choice)
        position = list(position)
        position[0] += 10
        position = tuple(position)
        position2 = list(position2)
        position2[0] += 10
        position2 = tuple(position2)
        print("Position1 {} position2 {}".format(position, position2))
    im.save("C:/Users/iamja_000/Documents/GitHub/worldgen2/lemonsxx.jpeg")


pil_image_iterative()