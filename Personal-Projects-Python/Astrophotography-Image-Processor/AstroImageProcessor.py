# An application to process and enhance astrophotography images
# @author Addie Domanico
# @version 8/3/2024

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageEnhance, ImageTk
import tkinter.font as tkFont
import Platform


class AstroImageProcessor:
    def __init__(self, root):
        # Initialize main application window
        self.root = root
        self.root.title("Astrophotography Image Processor")

        # Set initial window size
        self.root.geometry("800x600")

        # Load custom font
        self.custom_font = tkFont.Font(family="ClashGrotesk-Regular", size=16)

        # Create grid layout
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=0)

        # Create frame to hold image
        self.image_frame = tk.Frame(root)
        self.image_frame.grid(row=0, column=0, sticky="nsew")

        # Create smaller frames within the main frame
        self.right_frame = tk.LabelFrame(self.image_frame, text='Adjustments', font=self.custom_font, width=200,
                                         height=500)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        # Create label to display image
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack(padx=10, pady=10, expand=True)

        # Create a frame for sliders
        self.slider_frame = tk.Frame(root, height=100)
        self.slider_frame.grid(row=1, column=0, sticky="ew")

        # Create brightness slider
        self.brightness_scale = tk.Scale(self.right_frame, from_=-1.0, to=10.0, resolution=0.01, orient=tk.HORIZONTAL,
                                         label="Brightness")
        self.brightness_scale.grid(row=0, column=0, padx=5, pady=5)
        self.brightness_scale.bind("<Motion>", self.adjust_image)

        # Create contrast slider
        self.contrast_scale = tk.Scale(self.right_frame, from_=-1.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL,
                                       label="Contrast")
        self.contrast_scale.grid(row=1, column=0, padx=5, pady=5)
        self.contrast_scale.bind("<Motion>", self.adjust_image)

        # Create saturation slider
        self.saturation_scale = tk.Scale(self.right_frame, from_=-1.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL,
                                         label="Saturation")
        self.saturation_scale.grid(row=2, column=0, padx=5, pady=5)
        self.saturation_scale.bind("<Motion>", self.adjust_image)

        # Create resize slider
        self.resize_scale = tk.Scale(self.right_frame, from_=1.0, to=2.0, resolution=0.01, orient=tk.HORIZONTAL,
                                     label="Resize Factor")
        self.resize_scale.grid(row=3, column=0, padx=5, pady=5)
        self.resize_scale.set(1.0)

        # Set up menu bar with 'Open' and 'Save' options
        menu_bar = tk.Menu(root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Add 'Edit' menu with shortcuts
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        if self.is_mac:
            edit_menu.add_command(label="Undo      ⌘Z", command=self.undo_action, accelerator="Cmd+Z")
            edit_menu.add_command(label="Redo     ⌘⇧Z", command=self.redo_action, accelerator="Cmd+Shift+Z")
        else:
            edit_menu.add_command(label="Undo     Ctrl+Z", command=self.undo_action, accelerator="Ctrl+Z")
            edit_menu.add_command(label="Redo     Ctrl+Y", command=self.redo_action, accelerator="Ctrl+Y")
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        root.config(menu=menu_bar)

        # Bind shortcuts to commands
        

        # Initialize variables to hold original and processed images
        self.original_image = None
        self.processed_image = None
        self.zoom_factor = 1.0

        self.root.bind("<MouseWheel>", self.zoom_image)

        # Force update to ensure widgets are drawn
        self.root.update_idletasks()

    def open_image(self):
        # Open a file dialog to select image file
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg")])
        print(f"Selected file path: {file_path}")  # Debugging line
        if file_path:
            try:
                self.original_image = Image.open(file_path)
                self.processed_image = self.original_image
                self.resize_and_display_image(self.original_image)
            except Exception as e:
                print(f"Error: {e}")  # Debugging line
                messagebox.showerror("Error", f"Failed to open image: {e}")
            
    def save_image(self):
        # Save processed image to file
        if self.processed_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPG files", "*.jpg")])
            if file_path:
                self.processed_image.save(file_path)
        else:
            messagebox.showerror("Error", "No image to save")

    def adjust_image(self, event):
        # Adjust image based on all sliders
        if self.original_image:
            # Retrieve slider values
            brightness = self.brightness_scale.get()
            resize_factor = self.resize_scale.get()
            contrast = self.contrast_scale.get()
            saturation = self.saturation_scale.get()

            # Copy original image to avoid permanent changes
            image = self.original_image.copy()

            # Adjust brightness
            if brightness != 0:
                enhancer = ImageEnhance.Brightness(image)
                image = enhancer.enhance(1 + brightness)

            # Adjust contrast
            if contrast != 0:
                enhancer = ImageEnhance.Contrast(image)
                image = enhancer.enhance(1 + contrast)

            # Adjust color saturation
            if saturation != 0:
                enhancer = ImageEnhance.Color(image)
                image = enhancer.enhance(1 + saturation)

            # Resize image
            width, height = image.size
            new_size = (int(width * resize_factor), int(height * resize_factor))
            image = image.resize(new_size, Image.LANCZOS)

            self.processed_image = image
            self.resize_and_display_image(self.processed_image)

    def resize_and_display_image(self, image):
        # Resize image to fit within the window
        max_width = self.root.winfo_width() - 20
        max_height = self.root.winfo_height() - 100

        # Resize image while maintaining aspect ratio
        image.thumbnail((max_width, max_height), Image.LANCZOS)
        
        # Display given image
        image_tk = ImageTk.PhotoImage(image)
        self.image_label.config(image=image_tk)
        self.image_label.image = image_tk
        self.image_label.config(width=image_tk.width(), height=image_tk.height())

    def zoom_image(self, event):
        # Adjust zoom based on mouse wheel movement
        if event.delta > 0:
            self.zoom_factor *= 1.1
        elif event.delta < 0:
            self.zoom_factor /= 1.1

        self.zoom_factor = max(0.1, min(self.zoom_factor, 10.0))

        self.adjust_image(None)

    @staticmethod
    def undo_action():
        print("Undo completed")

    @staticmethod
    def redo_action():
        print("Redo completed")

if __name__ == "__main__":
    root = tk.Tk()
    app = AstroImageProcessor(root)
    root.mainloop()
    
    
                                                                                      
