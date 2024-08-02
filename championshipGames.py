import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = np.array([[0, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0], [0, 0, 0, 1]])
y = np.array([0, 1, 1, 0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier(n_estimators=100)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

championship_games = np.array([[0, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 1], [1, 1, 0, 0], [1, 0, 0, 1]])
predictions = model.predict(championship_games)

print('Numa melhor de 5, teriamos os seguintes resultados possíveis: ')

for i in range(len(championship_games)):
    if predictions[i] == 0:
        print("O time da casa vence o jogo {}.".format(i+1))
    else:
        print("O time visitante vence o jogo {}.".format(i+1))