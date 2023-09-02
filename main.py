import json
from PIL import Image, ImageDraw, ImageFont
import random
import textwrap

file = open("jokes.json")
image = Image.open("bg1.jpg")

draw = ImageDraw.Draw(image)

dad_jokes = json.load(file)
joke = random.choice(dad_jokes["jokes"])
text = joke["joke"]

text_color = (225, 225, 225)

W, H = image.size
font = ImageFont.truetype(font="Rubik-Bold.ttf", size=32)

# Wrap the text so it fits within the image width
lines = textwrap.wrap(text, width=40)

y_text = H // 2  # Starting Y-coordinate where the text will be placed

for line in lines:
    _, _, w, h = draw.textbbox((0, 0), line, font=font)
    text_position = ((W-w)//2, y_text)
    draw.text(text_position, text=line, fill=text_color, align="center", font=font)
    y_text += h  # Add the height of the line to the Y-coordinate for the next line

image.save(f"dj.png")
