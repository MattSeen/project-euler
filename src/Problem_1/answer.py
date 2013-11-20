answer = 0

for currentNumber in range(1000):

    if currentNumber % 5 == 0 or currentNumber % 3 == 0:
        answer += currentNumber

print "ans all", answer