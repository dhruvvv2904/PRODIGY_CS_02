from PIL import Image

key = int(input("Enter secret key (number): "))

img = Image.open("encrypted.png")
pixels = img.load()

width, height = img.size

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        pixels[x, y] = ((r - key) % 256,
                         (g - key) % 256,
                         (b - key) % 256)

img.save("decrypted.png")
print("Image decrypted and saved as decrypted.png")
