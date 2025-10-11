altura = float(input("Introdueix l'alçada del rectangle: "))
amplada = float(input("Introdueix l'amplada del rectangle: "))

if not altura < 0 or not amplada < 0:
	print(f"L'àrea del rectangle és: {round(altura*amplada, 2)} unitats quadrades.")
else:
	print("Les dimensions del rectangle han de ser positives.")

