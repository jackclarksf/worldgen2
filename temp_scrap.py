from PIL import Image, ImageDraw


print("Dog")

def pil_image():
    size = (100, 100)
    im = Image.new("RGB", size)
    draw = ImageDraw.Draw(im)
    red = (255,210,10)
    position = (0, 0)
    draw.rectangle((position, (10, 20)), fill=red)


    print(im)
    im.save("C:/Users/iamja_000/Documents/GitHub/worldgen2/lemons.jpeg")

pil_image()