from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def get_color(event):
    x, y = event.x, event.y
    pixel_color = img.getpixel((x, y))
    if len(pixel_color) > 3:
        pixel_color = pixel_color[:3]
    color_box.config(bg='#%02x%02x%02x' % pixel_color)
    color_label.config(text=f"R: {pixel_color[0]}, G: {pixel_color[1]}, B: {pixel_color[2]}")
    color_label2.config(text='#%02x%02x%02x' % pixel_color)

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global img
        img = Image.open(file_path)
        img = img.resize((400, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo

root = Tk()

image_label = Label(root)
image_label.pack()

button = Button(root, text="Open Image", command=open_image)
button.pack()

color_box = Label(root, width=10, height=5, bg='white')
color_box.pack()

color_label = Label(root, text="")
color_label.pack()
color_label2 = Label(root, text="")
color_label2.pack()

image_label.bind('<Button-1>', get_color)

root.mainloop()
