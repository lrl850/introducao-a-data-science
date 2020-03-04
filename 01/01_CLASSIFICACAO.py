

print ('lima')

porco01 =   [1,1,0]
porco02 =   [1,1,0]
porco03 =   [1,1,0]

cachorro01 = [1,1,1]
cachorro02 = [0,1,1]
cachorro03 = [0,1,1]


dados = [porco01, porco02, porco03, cachorro01, cachorro02,cachorro03]

marcacoes = [1 ,1 ,1,-1,-1,-1]

misterioso01 = [1,1,1]
misterioso02 = [1,0,0]
teste = [misterioso01,misterioso02]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

print(modelo.predict(misterioso01))
print(modelo.predict(teste))
