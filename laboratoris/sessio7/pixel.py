class Pixel:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
    
    def __str__(self):
        return f"{self.r}, {self.g}, {self.b} {self.a}"
    
    def pixel_promedio(self, otro_pixel):
        r = round((self.r + otro_pixel.r)/2)
        g = round((self.g + otro_pixel.g)/2)
        b = round((self.b + otro_pixel.b)/2)
        a = round((self.a + otro_pixel.a)/2)
        
        return Pixel(r, g, b, a)
