from PIL import Image

thresh = 200
fn = lambda x : 255 if x > thresh else 0

def process_images():
    images = []
    for i in range(2, 278):
        fname = f"low/{i:03}.jpg"
        print(fname)
        # Load and process the image
        im = Image.open(fname)

        if i > 1 and i < 278:
            im = im.convert("L").point(fn, mode='1')
        
        # save
        im.save(f"bw/{i:03}.jpg")

if __name__ == "__main__":
    # Let the user pass parameters to the code, all parameters are optional have some default values
    # ...
    # Make sure the output file ends with *.pdf*
    # ...
    process_images()