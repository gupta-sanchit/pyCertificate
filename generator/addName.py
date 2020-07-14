from PIL import ImageFont, ImageDraw, Image

fontColour = (70, 121, 189)
fontSize = 120

font = ImageFont.truetype("../generator/fonts/roman.ttf", fontSize)


def certificate(name, certificateID, gender):
    xCoordinate = 1926
    yCoordinate = 1161

    if gender == 'm':
        template = '../templates/templateMale.png'

    elif gender == 'f':
        template = '../templates/templateFemale.png'
    else:
        template = '../templates/templateO.png'
        xCoordinate = 2125

    img = Image.open(template)
    draw = ImageDraw.Draw(img)

    draw.text((xCoordinate, yCoordinate), name, font=font, fill=fontColour)

    img = img.convert('RGB')
    img.save(f"../certificates/{certificateID}.pdf")
