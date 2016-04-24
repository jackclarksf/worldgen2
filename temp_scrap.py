from PIL import Image, ImageDraw


print("Dog")

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
    draw.rectangle((position, (10, 20)), fill="red")


    print(im)
    im.save("C:/Users/iamja_000/Documents/GitHub/worldgen2/lemonsyyy.jpeg")

pil_image()