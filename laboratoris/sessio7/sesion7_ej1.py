from pixel import Pixel
vals = " ".split(input("Introduzca primer pixel (R,G,B,A): "))
print(vals)
pix1 = Pixel(vals[0], vals[1], vals[2], vals[3])
vals = " ".split(input("Introduzca segundo pixel (R,G,B,A): "))
pix2 = Pixel(vals[0], vals[1], vals[2], vals[3])


print(pix1.__str__, pix2.__str__)