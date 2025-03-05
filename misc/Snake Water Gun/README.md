# Snake-Water-Gun Game

🔍 **Problem Statement**
Implement a Snake-Water-Gun game where a player competes against the computer in multiple rounds. For a round, the player selects one of three choices (Snake (s), Water (w), or Gun (g)), while the computer randomly selects one. The result is determined based on predefined rules.

📜 **Game Rules**
The available choices are:
- Snake (s)
- Water (w)
- Gun (g)

The winner is determined as follows:
- Snake vs. Water → Snake wins ✅
- Snake vs. Gun → Gun wins ✅
- Water vs. Gun → Water wins ✅
- Same choices result in a draw.

The computer’s choice is randomly generated without knowing the player's choice.

The Round output should display:
- Player’s choice
- Computer’s choice
- Result (Win, Lose, or Draw)

After every round, the player decides if they want to play another round:
- If yes , another round is played.
- If no, the game ends and the final score is displayed:
    1. Number of games played in total
    2. Computer Wins
    3. Player Wins
    4. Draws
    5. Who finally won the entire game?