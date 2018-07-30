from svgimgutils import SVGImgUtils


def run():

    # Create SVG Image Utils for each SVG image
    base_template = SVGImgUtils.fromfile('Images/monkey.svg')
    pants = SVGImgUtils.fromfile('Images/pants.svg')
    shoes = SVGImgUtils.fromfile('Images/shoes.svg')
    tail = SVGImgUtils.fromfile('Images/tail.svg')
    mouth = SVGImgUtils.fromfile('Images/mouth.svg')
    glasses = SVGImgUtils.fromfile('Images/glasses.svg')
    hat = SVGImgUtils.fromfile('Images/hat.svg')
    misc = SVGImgUtils.fromfile('Images/misc.svg')

    # Append SVG images onto base template
    base_template.append(pants)
    base_template.append(shoes)
    base_template.append(tail)
    base_template.append(mouth)
    base_template.append(glasses)
    base_template.append(hat)
    base_template.append(misc)

    # Save new merged SVG image
    base_template.save('Images/merged.svg')


if __name__ == '__main__':
    run()
