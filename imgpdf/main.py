from PIL import Image

def process_images():
    images = []
    for i in range(1, 279):
        fname = f"gray/{i:03}.jpg"
        print(fname)
        # Load and process the image
        im = Image.open(fname)
        # Pillow can't save RGBA images to pdf,
        # make sure the image is RGB
        
        # # im = im.convert("RGB")
        # if i > 1 and i < 278:
        #     im = im.convert("L")
        # else:
        #     if im.mode == "RGBA":
        #         im = im.convert("RGB")
        
        # Add the (optionally) processed image to the images list
        images.append(im)

    # Convert the images list to pdf
    images[0].save("saber_bw.pdf", save_all = True, quality=65, append_images = images[1:])

if __name__ == "__main__":
    # Let the user pass parameters to the code, all parameters are optional have some default values
    # ...
    # Make sure the output file ends with *.pdf*
    # ...
    process_images()