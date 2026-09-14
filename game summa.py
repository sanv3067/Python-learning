import random

number = random.randint(1, 10)

print("🎮 NUMBER GUESSING GAME 🎮")
print("1 to 10 kulla oru number guess pannunga!")

guess = int(input("Your guess: "))

if guess == number:
    print("🎉 Correct! You Win!")
else:
    print("❌ Wrong!")
    print("Correct number:", number)
