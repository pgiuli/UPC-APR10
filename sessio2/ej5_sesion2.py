seconds = int(input("Introduzca el número de segundos: "))
hours = seconds // 3600
seconds -= hours * 3600
minutes = seconds // 60
seconds -= minutes * 60
print(f"{hours}h {minutes}m {seconds}s")