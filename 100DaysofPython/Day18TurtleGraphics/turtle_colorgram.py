import colorgram

colors = colorgram.extract('TurtleGraphics/hirst_painting.jpg', 30)
rgb_colors = []

for colour in colors:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    color_tuple = (r, g, b)
    rgb_colors.append(color_tuple)
print(rgb_colors)
