from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():

    scene_width = 800
    scene_height = 500

    canvas = start_drawing("Scene", scene_width, scene_height)

    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_cloud(canvas)
    # draw_grid(canvas, scene_width, scene_height, 50)
    draw_star(canvas)
    draw_cross(canvas,200,175)
    draw_text(canvas, 100, 100, "Hello World!", fill="gold")
    

    finish_drawing(canvas)
    

def draw_sky(canvas, scene_width, scene_height):
    
    draw_rectangle(canvas, 0, scene_height / 9,
        scene_width, scene_height, width=1, fill="midnight Blue")

def draw_ground(canvas, scene_width, scene_height):
    
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=1, fill="grey4")

"""def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)"""




def draw_cloud(canvas):
    
    draw_oval(canvas, 50,350,250,450, width = 1, outline="grey85", fill="grey85")
    draw_oval(canvas, 70,320,300,400, width = 1, outline="grey85", fill="grey85")
    draw_oval(canvas, 330,250,500,300, width = 1, outline="grey85", fill="grey85")
    draw_oval(canvas, 470,270,600,310, width = 1, outline="grey85", fill="grey85")


def draw_star(canvas):
   
   draw_polygon(canvas,670,280,610,468,760,348,580,348,730,468,outline="gold1",fill="gold1"  )


def draw_cross(canvas,center_x,center_y):
    hori_left_x = center_x -85
    hori_left_y = center_y -10
    hori_right_x =center_x +85
    hori_right_y = center_y +25

    ver_left_x = center_x -15
    ver_left_y = center_y -140
    ver_right_x = center_x +15
    ver_right_y = center_y +105

    draw_rectangle(canvas, hori_left_x,hori_left_y,hori_right_x,hori_right_y,outline="saddleBrown",fill='saddleBrown')
    draw_rectangle(canvas, ver_left_x,ver_left_y,ver_right_x,ver_right_y,outline = "grey6",fill='saddleBrown')


    


main()