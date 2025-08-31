from PIL import Image, ImageDraw, ImageFont

font_files = ["Roboto-Regular.ttf"]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

img_size = (28, 28)

for i in font_files:
    for letter in letters:
        
        img = Image.new("L", img_size, 0)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("fonts/" + i, 24)
        w, h = draw.textsize(letter, font=font)

        draw.text(((img_size[0]-w)//2, (img_size[1]-h)//2), letter, fill=255, font=font)

        img.save("datasets/text_images/{letter}_{i}.png")