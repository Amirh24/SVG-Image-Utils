from svgimageutils import SVGImgUtils as svga
# import scour as sc


def run():
    # Create SVG Appender for SVG images
    base_template = svga.fromfile('images/monkey.svg')
    base_template.monkeycolorchange("gray", "pink")

    pants = svga.fromfile('images/pants.svg')
    shoes = svga.fromfile('images/shoes.svg')
    tail = svga.fromfile('images/tail.svg')
    mouth = svga.fromfile('images/mouth.svg')
    # glasses = svga.fromfile('images/accessories/glasses/basic/output2.svg')
    hat = svga.fromfile('images/hat.svg')
    hippie_hat = svga.fromfile('images/accessories/hat/rare/JESTER.svg')


    misc = svga.fromfile('images/misc.svg')

    # Append SVG images into base template
    base_template.append(pants)
    base_template.append(shoes)
    base_template.append(tail, new_color='orange')
    base_template.append(mouth)
    # base_template.append(glasses)
    # base_template.append(hat)
    base_template.append(hippie_hat)


    base_template.append(misc)

    # Save new SVG Image
    base_template.save('Images/merged.svg')

    print((23,56,43,255)[:3])


if __name__ == '__main__':
    run()
