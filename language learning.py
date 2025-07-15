# Language Learning App (CLI)

import random

# Word dictionary: English to Spanish (you can change this)
word_list = {
    "apple": "manzana",
    "book": "libro",
    "dog": "perro",
    "water": "agua",
    "hello": "hola",
    "school": "escuela",
    "house": "casa",
    "car": "coche",
    "sun": "sol",
    "tree": "árbol"
}

def start_quiz():
    print("\n🌍 Welcome to the Language Learning App (Spanish Vocabulary) 🌍")
    print("Translate the following English words into Spanish.\n")

    words = list(word_list.items())
    random.shuffle(words)

    score = 0
    for i, (english, spanish) in enumerate(words[:5], 1):
        user_input = input(f"{i}. Translate '{english}': ").strip().lower()
        if user_input == spanish:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong. Correct answer: {spanish}\n")

    print(f"🎯 You got {score} out of 5 correct.")
    if score == 5:
        print("🏆 Excellent! You're doing great!")
    elif score >= 3:
        print("👍 Good job! Keep practicing.")
    else:
        print("📘 Keep learning. Practice makes perfect!")

def main():
    while True:
        print("\n=== Language Learning App Menu ===")
        print("1. Start Vocabulary Quiz")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ").strip()

        if choice == '1':
            start_quiz()
        elif choice == '2':
            print("👋 Goodbye! Keep learning new languages!")
            break
        else:
            print("❌ Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
