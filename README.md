# spritesheet2gif

Convert spritesheet image to a animated gif file

This project use python 3.7.1

You need have Pillow installed to run this project (lul)

> pip install Pillow

How to convert a spritesheet to gif

Step 1 : put an spritesheet into inputs folder (sprite animation should place in order from left to right, top to bottom)

Step 2 : cd to source code folder, type

> python main.py file_name_in_inputs_folder row col frameLength

frameLength is number of frames in spritesheet you want to capture.

Step 3 : Open outputs folder and see your gif

# Example

Put a image named haha.png to inputs folder

![Image of Input](examples/input.png)

Open terminal, cd to project's directory then type

> python main.py haha.png 4 5 18

check outputs folder and we will see this

![Image of Output](examples/output.gif)
