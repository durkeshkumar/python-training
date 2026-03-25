# Mini Project 8: Voting System

# Store candidates and votes
votes = {
    "vijay": 0,
    "dk": 0,
    "kumar": 0
}

# 1. Add Vote
def add_vote():
    print("\nCandidates:", ", ".join(votes.keys()))
    choice = input("Enter candidate name to vote: ")

    if choice in votes:
        votes[choice] += 1
        print(f"Vote given to {choice}!")
    else:
        print("Invalid candidate!")

# 2. Display Results
def display_results():
    print("\n--- Voting Results ---")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")

# 3. Display Winner
def show_winner():
    winner = max(votes, key=votes.get)
    print(f"\n🏆 Winner is {winner} with {votes[winner]} votes!")

# Menu system
def menu():
    while True:
        print("\n--- Voting Menu ---")
        print("1. Add Vote")
        print("2. Show Results")
        print("3. Show Winner")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_vote()
        elif choice == '2':
            display_results()
        elif choice == '3':
            show_winner()
        elif choice == '4':
            print("Thank you for voting!")
            break
        else:
            print("Invalid choice! Try again.")

# Run program
menu()