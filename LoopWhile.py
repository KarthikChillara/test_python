counter = 1
while counter <= 100:
    print(counter)
    counter += 2
    if counter > 50:
        break
print("Next line after while loop")
while counter >= 0:
    counter -= 1
    if counter % 2 == 1:
        continue
    print(counter)
else:
    print("Counter is no longer greater than zero")
print("After second while loop")

