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
    def __init__(self, our_list, our_name):
        self.image_list_iterator(our_list, our_name)

    def image_list_iterator(self, input_list, pic_name):
        size = (len(input_list[0])*10, len(input_list[0]*10))
        im = Image.new("RGB", size)
        draw = ImageDraw.Draw(im)
        count = 0

        def position_fiddler(pos):
            pos = list(pos)
            pos[0] += 10
            pos = tuple(pos)
            return pos

        for i in input_list:
            print(i, input_list.index(i))
            print(count)
            our_index = input_list.index(i)
            position = (0, count*10)
            position2 = (10, (count*10) + 10)
            for j in i:
                if j == "W":
                    draw.rectangle((position, position2), fill="blue")
                    position = position_fiddler(position)
                    position2 = position_fiddler(position2)
                elif j == "S":
                    draw.rectangle((position, position2), fill="red")
                    position = position_fiddler(position)
                    position2 = position_fiddler(position2)
                elif j == "C":
                    draw.rectangle((position, position2), fill="green")
                    position = position_fiddler(position)
                    position2 = position_fiddler(position2)
                elif j == "R":
                    draw.rectangle((position, position2), fill="purple")
                    position = position_fiddler(position)
                    position2 = position_fiddler(position2)
                elif j == "X":
                    draw.rectangle((position, position2), fill="orange")
                    position = position_fiddler(position)
                    position2 = position_fiddler(position2)
                else:
                    draw.rectangle((position, position2), fill="yellow")
                    position = position_fiddler(position)
                    position2 = position_fiddler(position2)
            count += 1
        im.save("C:/Users/iamja_000/Documents/GitHub/worldgen2/images/lemons_experiment_" + str(pic_name) + ".jpg")


#image_list_iterator(visual_map, 20)

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

#print(visual_map)
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


#pil_image_iterative()
