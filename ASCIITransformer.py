import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SHADING_STYLES = {
    "long": "#$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'.",  # Long default shading
    "normal": "@%#*+=-:. ",  # Default shading
    "custom": "$. "  # Custom shading (editable for experimental testing)
}


class ASCIITransformer:
    def __init__(self, fname="", height=25, shading_style="normal", dark_style=False, font_size=20):
        self.open(fname)
        self.new_height = height
        self.shading_style = SHADING_STYLES[shading_style]
        self.dark_style = dark_style
        if dark_style:
            self.shading_style = self.shading_style[::-1]
        self.font_size = font_size

    def __to_ascii(self, brightness):
        return self.shading_style[round((brightness / 255) * (len(self.shading_style) - 1))]

    def __stringify(self, img=None):
        if img is None:
            img = self.img
        # Calculate ascii image shape
        img_height, img_width = img.shape
        new_width = (2 * self.new_height * img_width) // img_height

        # Scale original image to ascii shape
        scaled_img = cv2.resize(img, dsize=(new_width, self.new_height), interpolation=cv2.INTER_CUBIC)

        # Create an ascii image
        ascii_arr = np.empty((self.new_height, new_width), dtype=str)
        for i in range(self.new_height):
            for j in range(new_width):
                ascii_arr[i, j] = self.__to_ascii(scaled_img[i, j])

        # Save ascii array shape for image sizing later
        self.ascii_arr_shape = ascii_arr.shape

        # Save image to txt file
        lines = '\n'.join([''.join([''.join(char) for char in row]) for row in ascii_arr])
        return lines

    def __imagify(self, img=None):
        # Get ascii string lines
        lines = self.__stringify(img)

        # Setup image
        bg_color, fg_color = ((0, 0), (255, 255)) if self.dark_style is True else ((255, 255), (0, 0))
        img_size = (int(self.ascii_arr_shape[1] * self.font_size * 0.65), int(self.ascii_arr_shape[0] * self.font_size * 1.2))
        img = Image.new('LA', img_size, bg_color)
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("RobotoMono-Bold.ttf", self.font_size)
        d.text((10, 10), lines, fill=fg_color, font=font, spacing=0.5)
        return img

    def open(self, fname):
        if fname != "":
            self.img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

    def transform_to_txt(self, fname="ascii-img.txt"):
        ascii_lines = self.__stringify()
        file = open(fname, "w")
        file.writelines(ascii_lines)

    def transform_to_img(self, fname="ascii-img.png"):
        img = self.__imagify()
        img.save(fname)

    def transform_to_video(self):
        vid = cv2.VideoCapture(0)
        print("HOW TO USE:\n"
              "* Press \'q\' at any time to quit video\n"
              "* Press keys 1-3 to adjust video quality where 1=lowest 3=highest\n"
              "* Toggle dark mode by pressing \"d\"")
        while (True):
            ret, frame = vid.read()
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ascii_img = np.asarray(self.__imagify(grayscale))[:, :, :1]
            cv2.imshow('frame', ascii_img)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord('n'):
                self.shading_style = "normal"
            elif key == ord('l'):
                self.shading_style = "long"
            elif key == ord('c'):
                self.shading_style = "custom"
            elif key == ord('d'):
                self.__reverse_shading()
            elif key == ord('='):
                self.new_height += 1
            elif key == ord('-'):
                self.new_height -= 1
            elif key == ord(']'):
                self.font_size += 1
            elif key == ord('['):
                self.font_size -= 1
            elif key == ord('1'):
                self.new_height = 10
                self.font_size = 45
            elif key == ord('2'):
                self.new_height = 30
                self.font_size = 15
            elif key == ord('3'):
                self.new_height = 50
                self.font_size = 10

        vid.release()
        cv2.destroyAllWindows()

    def __reverse_shading(self):
        self.dark_style = not self.dark_style
        self.shading_style = self.shading_style[::-1]