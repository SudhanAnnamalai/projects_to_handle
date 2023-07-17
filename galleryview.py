from tkinter import *
import glob
from PIL import ImageTk, Image

#Customized Frame for Gallery View
class GalleryViewer(Frame):
    #@Override the constructor of Frame
    def __init__(self, master, image_path):
        super().__init__(master)
        self.master = master
        self.image_paths = image_path
        self.cindex = 0
        self.master.title("Image Gallery")
        self.grid()
        self.create_widget()
        self.strack = 0

    def create_widget(self):
        #----------------------Navigation Buttons------------------------------------#
        #//////Previous//////////
        self.previous_button = Button(self, text="Previous", command=self.show_previous)
        self.previous_button.grid(row=0, column=0, padx=5, pady=5)
        #///////Next/////////
        self.next_button = Button(self, text = "Next",command=self.show_next)
        self.next_button.grid(row=0, column=1, padx=5, pady=5)

        #-----------------Display Area----------------------------------#
        self.image_label = Label(self, width=400, height=400)
        self.image_label.grid(row=1, column=0, columnspan=2)#Columnspan-Take two columns
        self.image_label.bind("<Button-1>", self.increase_label)

        #-----------------Current-Index Label-----------------------------#
        self.index_label = Label(self, text="Index label")#Edit it later
        self.index_label.grid(row=2,column=0, columnspan=2, padx=5)

        #-------------------------Status bar --------------------------------#
        self.status = Label(self, text="Click on Image to view")
        self.status.grid(row=3,column=0, columnspan=2, padx=5)

    

        #----------Display image-------------#
        self.show_image(0)
    #---------------------Function to Show Image------------------#
    def show_image(self, index):
        image_path = self.image_paths[index]
        image = Image.open(image_path)
        image = image.resize((self.image_label['width'],self.image_label['width']))
        photo = ImageTk.PhotoImage(image)

        self.image_label.configure(image=photo)
        self.image_label.image = photo
         
        self.index_label.configure(text = f"Image {index} of {len(self.image_paths)-1}")

    #---Function to increase image size-------------------
    def increase_label(self,event):
            if self.strack==0:
                new_width, new_height = self.image_label['width']+200, self.image_label['height']+200
                self.strack+=1
            else:
                new_width, new_height = self.image_label['width']-200, self.image_label['height']-200
                self.strack-=1
            self.image_label.config(width=new_width, height=new_height)
            self.show_image(self.cindex)
           


    #----------Now we can use show image to show previous and next images---------------#
    #Function for previous image
    def show_previous(self):
        if self.cindex>0:
            self.cindex-=1
            self.show_image(self.cindex)
        else:
            self.status.configure(text="This is first image")
    
    #---------Function for Next image----------------#
    def show_next(self):
        if self.cindex < len(self.image_paths)-1:
            self.cindex+=1
            self.show_image(self.cindex)
        else:
            self.status.configure(text="This is the last image")

image_paths = glob.glob("*.jpg")
root = Tk()
app = GalleryViewer(root, image_paths)
app.mainloop()




    