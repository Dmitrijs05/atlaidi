def aprAtlaidi(summa):
  rez=""
  if summa<100:
    rez="Atlaide nav piešķirta, janomaksa vel"+ str(summa)
  elif summa>=100 and summa <200:
    rez="Atlaide 5%, janomaksā vēl"+ str(summa*0,95)
  else:
    rez="Atlaide 10%, janomaksā vēl"+ str(summa*0,9)
  return rez

summa=float(input("Ievadiet summu:"))
print(aprAtlaidi(summa))