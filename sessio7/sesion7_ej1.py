from pixel import Pixel
vals = input("Introduzca primer pixel (R,G,B,A): ").split(' ')
pix1 = Pixel(int(vals[0]), int(vals[1]), int(vals[2]), int(vals[3]))
vals = input("Introduzca segundo pixel (R,G,B,A): ").split(' ')
pix2 = Pixel(int(vals[0]), int(vals[1]), int(vals[2]), int(vals[3]))


print(f"Pixel promedio: {pix1.pixel_promedio(pix2).__str__()}")