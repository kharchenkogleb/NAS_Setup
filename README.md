# championship_games
SortChampionshipGamesProject

O projeto consiste em script (Programa) do qual fazemos previsões das finais de um campeonato, ao estilo melhor de 5, sendo obrigatório jogar as 5 partidas.

Utilizamos a biblioteca numpy para criarmos os arrays, dos quais são incluídos os dados que serão treinados pelo no IA. 

A biblioteca sklearn foi utilizada para fazer estes treinamentos, previsões, estimativas dos dados existentes nos arrays.

O array ‘’X’’, contendo os valores ‘’0 (time da casa)’’ e  ‘’ 1 (time visitante) ’’ e o array “Y” contendo os valores “ 0 (vitória do time da casa)” e “ 1 (vitória time visitante)” são informadas para a IA através da função “ train_test_split ” a partir do retorno é criado o modelo de estimativa através da função: “ RandomForestClassifier “ e através de uma estrutura de repetição, é previsto qual time será vencedor de cada partida.

Executando novamente o script, são previstos outros resultados dos jogos.
