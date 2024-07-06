#Juan Carlos Vargas Castro
#¿Qué planeta tiene un diametro de aproximadamente 38% el de la tierra?

dicDiametros_Planetas = {'Sun': 1392000,'Mercury' : 4879, 'Venus' : 12092, 'Earth' : 12756, 'Mars' : 6792,
                    'Jupiter' : 142984 ,'Saturn': 120536, 'Uranus': 50724, 'Neptuno':49244,
                    'Pluto': 2376.6}

for x in sorted(dicDiametros_Planetas):
  print(f'El planeta {x} tiene un diámetro de {dicDiametros_Planetas[x]}.')

vnDiametro_Tierra = dicDiametros_Planetas['Earth']
vnPct_Diametro_Tierra = 0.38

for x in dicDiametros_Planetas:
  vnPct_Diametro_Planetas_Tierra = round(dicDiametros_Planetas[x] / vnDiametro_Tierra,2)
  if vnPct_Diametro_Planetas_Tierra == vnPct_Diametro_Tierra:
    print(f'El planeta {x} tiene un diámetro ({dicDiametros_Planetas[x]}) que es aproximadamente el {vnPct_Diametro_Tierra * 100}% del que tiene la Tierra ({vnDiametro_Tierra}).')

