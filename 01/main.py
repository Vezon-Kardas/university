from tkinter import *

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def getorigin(eventorigin):
    global x, title
    x = eventorigin.x
    if x<=255:
        root.title("0, 0, " + str(x))
    elif x>=256 and x<=511:
        root.title("0, "+str(-256+x)+", 255")
    elif x >= 512 and x <= 767:
        root.title("0, 255, "+str(767-x))
    elif x>=768 and x<=1023:
        root.title(str(-768+x) + ", 255, 0")
    elif x>=1024 and x<=1279:
        root.title("255, "+str(1279-x)+", 0")

root = Tk()
root.bind("<Button 1>",getorigin)

canvas = Canvas(root, width=1276, height=50, bg='white')

for i in range(1276):
    if i<=255:
        canvas.create_line(i, 10, i, 40, fill=_from_rgb((0, 0, i)))
    elif i>=256 and i<=511:
        canvas.create_line(i, 10, i, 40, fill=_from_rgb((0, -256+i, 255)))
    elif i >= 512 and i <= 767:
        canvas.create_line(i, 10, i, 40, fill=_from_rgb((0, 255, 767-i)))
    elif i >= 768 and i <= 1023:
        canvas.create_line(i, 10, i, 40, fill=_from_rgb((-768+i, 255, 0)))
    elif i >= 1024 and i <= 1279:
        canvas.create_line(i, 10, i, 40, fill=_from_rgb((255, 1279-i, 0)))

canvas.pack()
root.mainloop()