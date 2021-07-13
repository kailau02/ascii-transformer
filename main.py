from ASCIITransformer import ASCIITransformer

'''
ASCIITransformer Class:

    Constructor parameters:
    1. fname=(str) string for  image you will convert (if using webcam, you can leave this blank)
    2. height=(int) number of rows of ascii characters, width will be proportionally calculated
    3. shading_style=(str) "normal", "long", or "custom"
    4. dark_style=(bool) create ascii image with dark theme or light theme
    5. font_size=(int) adjust font size

    Methods:
    .open(fname={input file name}) # To open an image for conversion
    .transform_to_txt(fname={output file name}) # Transform opened image to ascii in .txt document
    .transform_to_img(fname={output file name}}) # Transform opened image to ascii in .png document
    .transfrom_to_video() # Realtime video transform

    # Video example:
    transformer = ASCIITransformer(height=40, font_size=12, dark_style=True)
    transformer.transform_to_video()
    
    # Photo example:
    img_transformer = ASCIITransformer(fname="images/tree.jpeg", height=70, font_size=10)
    img_transformer.transform_to_img(fname="images/tree-ascii.png")
    
    # Text example:
    transformer = ASCIITransformer(fname="images/dog.jpg")
    transformer.transform_to_txt(fname="images/ascii-dog.txt")
    
'''
transformer = ASCIITransformer(height=40, font_size=12, dark_style=True)
transformer.transform_to_video()