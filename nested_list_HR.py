recordAll=[]
scoreAll=[]
secondSmallestNames=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student=[name,score]
        scoreAll.append(score)
        recordAll.append(student)
scoreAll.sort()
secondSmallestScore=0
for score1 in scoreAll:
    if (scoreAll[0]<score1):
        secondSmallestScore=score1
        break
count=scoreAll.count(secondSmallestScore)
print(count)
for list in recordAll:
    if (list[1]==secondSmallestScore):
        secondSmallestNames.append(list[0])
secondSmallestNames.sort()
for name in secondSmallestNames:
    print(name)
