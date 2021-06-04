print("Basic: ")
for x in range(151):
    print(x)

print("Multiples of 5: ")
for x in range(5, 1001, 5):
    print(x)

print("Counting, the Dojo Way: ")
for x in range(1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")

print("Whoa. That Sucker's Huge")
sum = 0
for x in range(500001):
    if(x % 2 == 1):
        sum += x
print(sum)

print("Countdown by Fours: ")
for x in range(2018, 0, -4):
    print(x)

print("Flexible Counter: ")
lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)