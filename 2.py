zi=['Luni','Marti','Miercuri','Joi','Simbata','Duminica']
v=[2345,556,878,4567,2000,1500,970]
print('Venitul saptamanal',sum(v))
print('Media venitului saptamanal',round(sum(v)//7,2))
print('Ziua cu cel mai mare venit',zi[v.index(max(v))])
print('Ziua cu cel mai mic venit',zi[v.count(min(v))])