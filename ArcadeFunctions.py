import arcade

def create_shapes(win_width, win_height):
    shape_list = []
    win_width = win_width/4
    rectangle = arcade.create_rectangle_filled(win_width, 350, 100, 200, arcade.color.DEEP_RUBY)
    circle = arcade.create_ellipse_filled(win_width*3, 350, 50, 50, arcade.color.ELECTRIC_YELLOW)
    line = arcade.create_line(win_width, 650, 650, 75, arcade.color.DEEP_SKY_BLUE)
    shape_list.append(rectangle)
    shape_list.append(circle)
    shape_list.append(line)
    return shape_list

def create_more_shapes(current_shapes, win_height):
    poly_points = [(400, win_height-50), (350, win_height-100), (450, win_height-100)]
    triangle = arcade.create_polygon(poly_points, arcade.color.INTERNATIONAL_ORANGE)
    current_shapes.append(triangle)

def main():
    WINDOW_WIDTH = 700
    WINDOW_HEIGHT = 700
    arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, "demo with functions")
    # when we use all caps in programming it means that the value should not be changed
    shapes_to_draw = create_shapes(WINDOW_WIDTH, WINDOW_HEIGHT)
    # shapes_to_draw = create_shapes()
    create_more_shapes(shapes_to_draw, WINDOW_HEIGHT)


    arcade.start_render()
    for shape in shapes_to_draw:
        shape.draw()

    arcade.finish_render()
    arcade.run()

main()