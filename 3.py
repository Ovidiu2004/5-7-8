ora=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
t=[0,-1,-2,-3,-4,-5,1,2,3,4,5,9,12,13,14,15,16,17,18,7,16,2,14,10,8]
print('Temperatura medie',round(sum(t)/24,1))
print('Maximul temperaturii',max(t))
print('Minimul temperaturii',min(t))
print('ora(orele) la care s-a inregistrat temperatura maxima',ora[t.index(max(t))])
print('ora(orele) la care s-a inregistrat temperatura minima',ora[t.index(min(t))])