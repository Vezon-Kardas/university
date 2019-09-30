from tkinter import *

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def depth(x):
    percent = 100*x/1276
    depth = int(percent)/100
    number_depth = 16383*depth
    number_depth = int(number_depth)
    total = bin(number_depth)
    label = Label(text=total[2:], bg="white", font="Arial 12", justify="center", pady=10, padx=10)
    label.place(x=275, y=53)


def getorigin(eventorigin):
    global x, y, location
    x = eventorigin.x
    y = eventorigin.y

    if x<=255 and y<=50:
        location = "0, 0, {0}".format(x)
    elif x>=256 and x<=511 and y<=50:
        location = "0, {0}, 255".format(-256+x)
    elif x >= 512 and x <= 767 and y<=50:
        location = "0, 255, {0}".format(767-x)
    elif x>=768 and x<=1023 and y<=50:
        location = "{0}, 255, 0".format(-768+x)
    elif x>=1024 and x<=1279 and y<=50:
        location = "255, {0}, 0".format(1279-x)
    if y<=50:
        label = Label(text=location, bg="white", font="Arial 12", justify="center", pady=10, padx=10)
        label.place(x=90, y=53)
        depth(x)


root = Tk()
root.title("Зондирование земли")
root.geometry('1276x750')
root.bind("<Motion>",getorigin)

canvas = Canvas(root, width=1279, height=95, bg='white')
for i in range(1279):
    if i<=255:
        canvas.create_line(i, 10, i, 50, fill=_from_rgb((0, 0, i)))
    elif i>=256 and i<=511:
        canvas.create_line(i, 10, i, 50, fill=_from_rgb((0, -256+i, 255)))
    elif i >= 512 and i <= 767:
        canvas.create_line(i, 10, i, 50, fill=_from_rgb((0, 255, 767-i)))
    elif i >= 768 and i <= 1023:
        canvas.create_line(i, 10, i, 50, fill=_from_rgb((-768+i, 255, 0)))
    elif i >= 1024 and i <= 1279:
        canvas.create_line(i, 10, i, 50, fill=_from_rgb((255, 1279-i, 0)))

Label(text="RGB-код: ", bg="white", font="Arial 12", justify="center", pady=10, padx=10).place(x=5, y=53)
Label(text="Глубина: ", bg="white", font="Arial 12", justify="center", pady=10, padx=10).place(x=200, y=53)

canvas.grid()
root.mainloop()
