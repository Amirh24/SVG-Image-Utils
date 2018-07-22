from pkg.SVGAppender import SVGAppender as svga


def run():
    # Create SVG Appender for SVG images
    base_template = svga.fromfile('Images/monkey.svg')
    pants = svga.fromfile('Images/pants.svg')
    shoes = svga.fromfile('Images/shoes.svg')
    tail = svga.fromfile('Images/tail.svg')
    mouth = svga.fromfile('Images/mouth.svg')
    glasses = svga.fromfile('Images/glasses.svg')
    hat = svga.fromfile('Images/hat.svg')
    misc = svga.fromfile('Images/misc.svg')

    # Append SVG images into base template
    base_template.append(pants)
    base_template.append(shoes)
    base_template.append(tail)
    base_template.append(mouth)
    base_template.append(glasses)
    base_template.append(hat)
    base_template.append(misc)

    # Save new SVG Image
    base_template.save('Images/merged.svg')

if __name__ == '__main__':
    run()

# print(rule.style.getCssText())
# print(rule.style.getPropertyCSSValue('fill'))
