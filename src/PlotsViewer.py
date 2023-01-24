import tkinter
import customtkinter
import os,glob
import ntpath
from PIL import Image

class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    # self.geometry("1240x780")
    self.title("CustomTkinter simple_example.py")

    customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    self.frame_1 = customtkinter.CTkFrame(self)
    self.frame_1.pack()

    rootDir = os.path.dirname(os.path.abspath(__file__))
    self.outputFilesPath = os.path.join(rootDir,"..","OutputFiles")
    self.listOfImagePaths = glob.glob(os.path.join(self.outputFilesPath,'*.png'))
    listOfImages = [ntpath.basename(name).split('.')[0] for name in self.listOfImagePaths]
    self.optionmenu_1 = customtkinter.CTkOptionMenu(self.frame_1, values=listOfImages,command=self.showImage)
    self.optionmenu_1.grid(row=0,column=0,pady=10, padx=10)
    self.optionmenu_1.set(listOfImages[0])
    
    self.optionmenu_2 = customtkinter.CTkOptionMenu(self.frame_1, values=listOfImages,command=self.showImage)
    self.optionmenu_2.grid(row=0,column=1,pady=10, padx=10)
    self.optionmenu_2.set(listOfImages[1])

    self.frame_2 = customtkinter.CTkFrame(self)
    # self.frame_2.grid(row=1,column=0)
    self.frame_2.pack()
    self.large_test_image = customtkinter.CTkImage(Image.open(self.listOfImagePaths[0]), size=(600, 500))
    self.label_1 = customtkinter.CTkLabel(master=self.frame_2, justify=tkinter.CENTER,image=self.large_test_image,text="")
    self.label_1.grid(row=0,column=0,pady=10, padx=10)
    self.large_test_image = customtkinter.CTkImage(Image.open(self.listOfImagePaths[1]), size=(600, 500))
    self.label_2 = customtkinter.CTkLabel(master=self.frame_2, justify=tkinter.CENTER,image=self.large_test_image,text="")
    self.label_2.grid(row=0,column=1,pady=10, padx=10)
    # self.large_test_image = customtkinter.CTkImage(Image.open(listOfImagePaths[0]), size=(600, 500))
    # label_1 = customtkinter.CTkLabel(master=self.frame_1, justify=tkinter.CENTER,image=self.large_test_image)
    # label_1.pack(pady=10, padx=10)

    # tabview_1 = customtkinter.CTkTabview(master=self.frame_1, width=400, height=270)
    # tabview_1.pack(pady=10, padx=10)
    # tabview_1.add("CTkTabview")
    # tabview_1.add("Tab 2")
    
    
  def showImage(self,event):
    # print(os.path.join(self.outputFilesPath,self.optionmenu_1.get()+".png"))
    # self.frame_2.grid_forget()
    self.frame_2.pack_forget()
    selectedImage1 = glob.glob(os.path.join(self.outputFilesPath,self.optionmenu_1.get()+".png"))[0]
    self.large_test_image1 = customtkinter.CTkImage(Image.open(selectedImage1), size=(600, 500))
    selectedImage2 = glob.glob(os.path.join(self.outputFilesPath,self.optionmenu_2.get()+".png"))[0]
    self.large_test_image2 = customtkinter.CTkImage(Image.open(selectedImage2), size=(600, 500))
    
    self.frame_2 = customtkinter.CTkFrame(self)
    self.frame_2.pack()
    self.label_1 = customtkinter.CTkLabel(master=self.frame_2, justify=tkinter.CENTER,image=self.large_test_image1,text="")
    self.label_1.grid(row=0,column=0,pady=10, padx=10)
    self.label_2 = customtkinter.CTkLabel(master=self.frame_2, justify=tkinter.CENTER,image=self.large_test_image2,text="")
    self.label_2.grid(row=0,column=1,pady=10, padx=10)
    # label_1.grid(row=1,column=0)


if __name__ == "__main__":
  app = App()
  app.mainloop()
