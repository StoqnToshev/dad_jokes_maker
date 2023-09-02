import json
from PIL import Image, ImageDraw, ImageFont
import random
import textwrap

with open("jokes.json") as file:
    dad_jokes = json.load(file)
image = Image.open("bg1.jpg")
draw = ImageDraw.Draw(image)

#Chooses random joke
joke = random.choice(dad_jokes["jokes"])
text = joke["joke"]

text_color = (225, 225, 225)

W, H = image.size
font = ImageFont.truetype(font="Rubik-Bold.ttf", size=32)

# Wraps the text so it fits within the image width
lines = textwrap.wrap(text, width=40)

y_text = H // 2  # Starting Y-coordinate where the text will be placed

#If the text is too big, it makes the text go to a new line
for line in lines:
    _, _, w, h = draw.textbbox((0, 0), line, font=font)
    text_position = ((W-w)//2, y_text)
    draw.text(text_position, text=line, fill=text_color, align="center", font=font)
    y_text += h  # Adding the height of the line to the Y-coordinate for the next line

#Saves the image as dj("dad joke").png
image.save(f"dj.png")
