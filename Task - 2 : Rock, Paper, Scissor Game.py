# 🎮 Rock, Paper, Scissors Game

from random import randint

print("=" * 40)
print("🎲 Welcome to Rock, Paper, Scissors 🎲")
print("=" * 40)

t = ["Rock", "Paper", "Scissors"]

computer_win = 0
player_win = 0

while True:
    print("\n🤔 Choose your move:")
    player_choice = input("👉 Rock, Paper, Scissors or type 'exit' to quit: ")

    if player_choice == "exit":
        print("\n🏁 Final Score:")
        print("🖥️  Computer wins:", computer_win)
        print("🧑 Player wins   :", player_win)
        print("🙏 Thanks for playing!")
        break

    comp_choice = t[randint(0, 2)]

    if player_choice == comp_choice:
        print("🤝 It's a Tie!")
    elif player_choice == "Rock":
        if comp_choice == "Paper":
            print("❌ You lose!")
            print("🖥️  Computer chose:", comp_choice)
            print("🧑 You chose     :", player_choice)
            computer_win += 1
        else:
            print("✅ You win!")
            print("🧑 You chose     :", player_choice)
            print("🖥️  Computer chose:", comp_choice)
            player_win += 1
    elif player_choice == "Paper":
        if comp_choice == "Scissors":
            print("❌ You lose!")
            print("🖥️  Computer chose:", comp_choice)
            print("🧑 You chose     :", player_choice)
            computer_win += 1
        else:
            print("✅ You win!")
            print("🧑 You chose     :", player_choice)
            print("🖥️  Computer      :",comp_choice)
