import json
import math
import time

start_time = time.time()

with open('CTBC.json') as page:
    page = json.load(page)
print("--- %s seconds ---" % (time.time() - start_time))

Voc = []
for i in range(0, len(page)):
    answer = page[i]["answer"]
    for j in range(0, len(answer)-1):
        if i == 0 and j == 0:
            Voc.append(answer[j:j+2])
        else:
            for k in range(0, len(Voc)):
                if answer[j:j+2] != '  ':
                    if Voc[k] == answer[j:j+2]:
                        break
                    elif k + 1 == len(Voc):
                        Voc.append(answer[j:j+2])
#print ('All Vocabulary')
#print (Voc)
print("--- %s seconds ---" % (time.time() - start_time))

Bag = []
for i in range(0, len(page)):
    answer = page[i]["answer"]
    Bag.append([])
    for j in range(0, len(answer)-1):
        if j == 0:
            Bag[i].append(answer[j:j+2])
        else:
            for k in range(0, len(Bag[i])):
                if answer[j:j+2] != ' ':
                    if Bag[i][k] == answer[j:j+2]:
                        break
                    elif k + 1 == len(Bag[i]):
                        Bag[i].append(answer[j:j+2])
#print ('Bag-of-Words')
#print (Bag)
print("--- %s seconds ---" % (time.time() - start_time))

TF = []

for i in range(0, len(page)):
    answer = page[i]["answer"]
    sentence = answer
    TF.append([])
    for j in range(0, len(sentence)-1):
          existInPages = 0
          if j == 0:
              TF[i].append([sentence[j:j+2],1])
          else:
              for k in range(0, len(TF[i])):
                  if sentence[j:j+2] != '  ':
                      if TF[i][k][0] == sentence[j:j+2]:
                          TF[i][k][1] += 1
                          break
                      elif k + 1 == len(TF[i]):
                          TF[i].append([sentence[j:j+2],1])
          if j == len(sentence)-2:
              for k in range(0, len(TF[i])):
                  TF[i][k][1] = TF[i][k][1]/(len(sentence)-1)
#print ('Bi-Gram TF')
#print (TF)
print("--- %s seconds ---" % (time.time() - start_time))

realTF = []
for i in range(len(TF)):
    realTF.append([])
    for j in range(len(Voc)):
        for k in range(len(TF[i])):
            if TF[i][k][0] == Voc[j]:
                realTF[i].append([TF[i][k][0],TF[i][k][1]])
                break
            elif k + 1 == len(TF[i]):
                realTF[i].append([Voc[j],0])
#print ('Real TF data matrix')
#print (realTF)
print("--- %s seconds ---" % (time.time() - start_time))

Q = input('Please input data you want to search :\n')

QVoc = []

for i in range(0, len(Q)-1):
    if i==0:
        QVoc.append(Q[i:i+2])
    else:
        for k in range(0, len(QVoc)):
            if Q[i:i+2] != '  ':
                if QVoc[k] == Q[i:i+2]:
                    break
                elif k + 1 == len(QVoc):
                    QVoc.append(Q[i:i+2])
#print ('All Question Vocabulary')
#print (QVoc)

Rank = []
for i in range(len(realTF)):
    Rank.append(0)
    for j in range(len(QVoc)):
        for k in range(len(realTF[i])):
            if QVoc[j] == realTF[i][k][0]:
                Rank[i] += realTF[i][k][1]

#print (Rank)

value = -1
index = -1
for i in range(len(Rank)):
    if Rank[i] > value:
        value = Rank[i]
        index = i
#print ('Index : ' + str(index))
#print ('Value : ' + str(value))

indexes = []

for i in range(len(Rank)):
    if Rank[i] == value:
        indexes.append(i)

#print ('Possible indexes : ')
#print (indexes)

print('These datas might be what you are looking for : ')
for i in range(len(indexes)):
    print (i)
    print ('Q : ' + page[indexes[i]]["answer"])
    print ('A : ' + page[indexes[i]]["answer"] + '\n')
