# 🌍 Capital Master

A fun and interactive geography quiz game built with **Python** and **CustomTkinter**.

Test your knowledge of world countries, states, and capitals through an engaging quiz interface with animations, scoring, and celebration effects.

---

## 🎮 Features

### 🌎 Multiple Game Modes

### International Mode
- Quiz questions covering countries around the world.
- Example:
  > What is the capital of France?

### Country Mode
- Select a country and answer questions about its states and capitals.
- Example:
  > What is the capital of Maharashtra?

---

## ✨ Game Features

- Interactive GUI built with CustomTkinter
- Random question generation
- Multiple choice answers
- Score tracking
- Correct answer validation
- Instant feedback
- Confetti celebration animation 🎉
- Return to main menu anytime
- Restart games without restarting the application
- Custom sound effects support
- JSON-based database system

---

# 🛠️ Technologies Used

## Programming Language

- Python 3.x

## GUI Framework

- CustomTkinter
- Tkinter Canvas animations

## Data Storage

- JSON

---

# 📂 Project Structure
capitals_game/
│
├── main.py
├── database.json
├── README.md
│
├── sounds/
│ ├── correct.wav
│ └── wrong.wav
│
└── assets/
└── images/

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/capital-master.git

▶️ Running the Game

Start the application:

python main.py

The game window will open with the main menu.

🎯 How to Play:
----------------
Launch the game.
Choose a mode:
🌍 International
🏳 Country
Select a country if using Country Mode.
Press Start Game.
Select the correct capital from the options.
Earn points for correct answers.
Enjoy the confetti celebration when you answer correctly! 🎉
🏆 Scoring
Correct Answer:
Score increases
Wrong Answer:
No points awarded

Future versions may include:

Difficulty levels
Timers
Achievements
Leaderboards


📚 Database

The game uses a JSON database structure.

Example:

{
    "countries": {
        "India": {
            "capital": "New Delhi",
            "states": {
                "Tamil Nadu": {
                    "capital": "Chennai"
                },
                "Maharashtra": {
                    "capital": "Mumbai"
                }
            }
        }
    }
}

The database can be expanded easily with additional countries and states.

🎉 Confetti Animation

The game includes a custom celebration animation:

Features:

Burst from both sides of the screen
Multiple colors
Multiple shapes
Gravity-based falling
Random movement
Automatic cleanup
🔮 Future Improvements

Planned enhancements:

 Complete world country database
 Complete state/province database
 Question history tracking
 Difficulty modes
 Timed challenges
 Player statistics
 High-score saving
 More animations
 Multiple languages
🤝 Contributing

Contributions are welcome!

Steps:

Fork the repository.
Create a new branch.
git checkout -b feature-name
Make your changes.
Commit your work.
git commit -m "Added new feature"
Push and create a pull request.
📄 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Created as a Python learning project exploring:

GUI development
Game logic
JSON databases
Animation systems
Application architecture
