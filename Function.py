import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

pd.set_option("display.max_columns", None)
documentA = ' кроме новый и двухгнездовый многоузловой сервер twin компания supermicro также представить линейка сервер новый поколение под общий название wio и сервер с поддержка восемь гп удвоенный ширина.'
documentB = ' на вопрос один из пользователь сервис микроблог о примерный дата выпуск смартфон на рынок адресованный испанский аккаунт поддержка sony последний сообщить что новый xperia ii должный появиться на полок уже в конец этот месяц.'
documentC ='авторитетный инсайдер мукула шарм поделиться качественный фото новый флагманский устройство oneplus pro в различный расцветка судить по один фотография в вода смартфон точно не быть бояться вода.'
documentD = 'сегодня xiaomi официально представить новый наушник под название redmi airdots внешне наушник ничто не отличаться от оригинальный модель.'
documentE = 'процессор core обладать ядро и поток и согласно тест он базовый тактовый частота составлять ггц тогда как максимальный достигать ггц.'
bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')
bagOfWordsC = documentC.split(' ')
bagOfWordsD = documentD.split(' ')
bagOfWordsE = documentE.split(' ')


uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB), set(bagOfWordsC), set(bagOfWordsD), set(bagOfWordsE))


numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1

numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1

numOfWordsC = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsC:
    numOfWordsC[word] += 1

numOfWordsD = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsD:
    numOfWordsD[word] += 1

numOfWordsE = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsE:
    numOfWordsE[word] += 1




def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

tfA = computeTF(numOfWordsA ,bagOfWordsA)
tfB = computeTF(numOfWordsB, bagOfWordsB)
tfC = computeTF(numOfWordsC, bagOfWordsC)
tfD = computeTF(numOfWordsD, bagOfWordsD)
tfE = computeTF(numOfWordsE, bagOfWordsE)


def computeIDF(documents):
    import math
    N = len(documents)

    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

idfs = computeIDF([numOfWordsA, numOfWordsB, numOfWordsC, numOfWordsD, numOfWordsE])

def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)
tfidfC = computeTFIDF(tfC, idfs)
tfidfD = computeTFIDF(tfD, idfs)
tfidfE = computeTFIDF(tfE, idfs)

df = pd.DataFrame([tfidfA, tfidfB, tfidfC, tfidfD, tfidfE, ])

print(df)
'''vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([documentA, documentB, documentC, documentD, documentE])
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)'''
