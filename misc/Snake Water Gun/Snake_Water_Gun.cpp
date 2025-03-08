#include <bits/stdc++.h>
#include <random>
using namespace std;

class Snake_Water_Gun
{
public:
    int playerWin;   // number of times the player won
    int computerWin; // number of times the computer won
    int gamesPlayed; // total number of games played

    // default constructor - initialising values before any games are played
    Snake_Water_Gun()
    {
        playerWin = 0;
        computerWin = 0;
        gamesPlayed = 0;
    }

    // Function to get the computer's choice randomly generated
    char get_computerchoice()
    {
        random_device rd;                       // obtain a random number
        mt19937 gen(rd());                      // seed the generator
        uniform_int_distribution<> distr(0, 2); // define the range as there are 3 options

        int randomChoice = distr(gen);
        switch (randomChoice)
        {
        case 0:
            return 's'; // snake
        case 1:
            return 'w'; // water
        case 2:
            return 'g'; // gun
        }

        return 's'; // default
    }

    // function to get the player's choice
    char get_playerChoice()
    {
        char playerChoice;
        cout << "Enter your choice('s' for snake/'w' for water/'g' for gun):";
        cin >> playerChoice;
        playerChoice = tolower(playerChoice); // making sure upper case input is treated correctly

        return playerChoice;
    }

    // start a game with multiple rounds
    void play()
    {
        do
        {
            gamesPlayed++;
            char computerChoice = get_computerchoice();
            char playerChoice = get_playerChoice();
            winner(computerChoice, playerChoice); // compute the winner and display
            cout << "do you want to play another game?('y' for yes/'n' for no):";
            char choice;
            cin >> choice;
            choice = tolower(choice);

            if (choice == 'n') // if choice is no
            {
                cout << "Game over!" << endl;
                cout << "The number of games played:" << gamesPlayed << endl;                    // total games played
                cout << "Comptuter wins:" << computerWin << endl;                                // total compter wins
                cout << "Player wins:" << playerWin << endl;                                     // total player wins
                cout << "The number of draws:" << gamesPlayed - computerWin - playerWin << endl; // number of draws
                if (computerWin > playerWin)
                {
                    cout << "Oops!Computer won.";
                }
                else if (computerWin == playerWin)
                {
                    cout << "Draw";
                }
                else
                {
                    cout << "Congratulations!! Player won.";
                }
                break;
            }
        } while (true);
    }

    void winner(char computerChoice, char playerChoice)
    {
        cout << "The computer's choice:" << computerChoice;
        cout << endl;
        cout << "The player's choice:" << playerChoice;
        cout << endl;

        if (playerChoice != 's' && playerChoice != 'w' && playerChoice != 'g') // for invalid entry by player,computer wins
        {
            cout << "Invalid choice by player. Computer wins by default.";
            computerWin++;
        }
        // defining the rules of winning
        else if (
            ((playerChoice == 's' && computerChoice == 'g') ||
             (playerChoice == 'w' && computerChoice == 's') ||
             (playerChoice == 'g' && computerChoice == 'w')))
        {
            computerWin++;
            cout << "Computer won this round.";
        }

        // condition for draw
        else if (playerChoice == computerChoice)
        {
            cout << "It's a draw!\n";
        }

        // player naturally wins for any other condition
        else
        {
            playerWin++;
            cout << "Player won this round.";
        }
        cout << endl;
    }
};

int main()
{

    Snake_Water_Gun game;
    game.play();

    return 0;
}