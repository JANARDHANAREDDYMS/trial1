import random
import statistics
import sys

coin = random.choice(["heads","tails"])
print(coin)

x =  random.randint(1,10)
print(x)

cards = ["jack","king","queen"]
random.shuffle(cards)
for card in cards:
    print(card)

print((statistics.mean([100,90,80])))

if len(sys.argv)<2:
    sys.exit("too few arguments")  #sys.exit exits from the programme
elif len(sys.argv)>2:
    print("too many arguments")
else:
    print("my name is", sys.argv[1])  #if no [1] is given it prints all the argumnets passed icluding the name of the proggramme

for arg in sys.argv[1:]:  #[x:] is called slices, you can also slice from end of argument like [1:-1]
    print("The args are",arg)