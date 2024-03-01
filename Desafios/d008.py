medida_m = float(input('Qual a medida em metros? '))
medida_km = medida_m/1000
medida_hm = medida_m/100
medida_dam = medida_m/10
medida_dm = medida_m*10
medida_cm = medida_m*100
medida_mm = medida_m*1000
print('A medida de {}m corresponde a: \nKilometros: {}km \nHectômetros: {}hm \nDecâmetros {}dam \nDecímetros: {}dm \nCentímetros: {}cm \nMilímetros: {}mm'.format(medida_m, medida_km, medida_hm, medida_dam, medida_dm, medida_cm, medida_mm))