# ascii-transformer

## Installation

### Installation using Conda:
1. Open terminal and locate folder to copy to
2. `git clone https://github.com/kailau02/ascii-transformer.git`
3. `conda create --name ./env --file requirements.txt`

### Global python3 installation:
1. Open terminal and locate folder to copy to
2. `git clone https://github.com/kailau02/ascii-transformer.git`
3. `pip3 install opencv-python numpy pillow`

## How to Use
In `main.py`, you must instantiate the `ASCIITransformer` class-object and then you can call methods to transform images and videos to ASCII representations

### Webcam mode

#### Basic setup
* The webcam mode loads by default from `main.py` by writing in terminal `python3 main.py`
* Make sure to allow the program access to your webcam to run
* The script may need to be ran twice before working properly
* While the program is running, you can set the ascii density/quality by clicking `1` `2` and `3` on your keyboard

#### Usage
Call the video capture method using `obj.transform_to_video()`

### Image mode
* Open an existing image on object instantiation like: `obj = ASCIITransformer(fname="image.jpeg")`
* Or, open an image directly from the object like: `obj.open(fname="image.jpeg")`
* Convert the image to an ASCII image like: `obj.transform_to_img(fname="resulting-image.png")`

### Text mode
* Open an existing image on object instantiation like: `obj = ASCIITransformer(fname="image.jpeg")`
* Or, open an image directly from the object like: `obj.open(fname="image.jpeg")`
* Convert the image to an ASCII text file like: `obj.transform_to_txt(fname="resulting-text.txt")`

## Video Example
[![Dolly Zoom Video Example](https://img.youtube.com/vi/Ad_T9uC9uCg/0.jpg)](https://www.youtube.com/watch?v=Ad_T9uC9uCg)
