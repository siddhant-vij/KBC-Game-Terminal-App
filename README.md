# KBC Game Terminal App

KBC (Kaun Banega Crorepati) is a popular Indian television game show in which a player answers multiple-choice questions to increase their winnings, with the possibility to use various "lifelines" for assistance. The game has several "lifelines" to aid contestants when they are unsure of an answer. Some of the most common lifelines include "50:50" (where two incorrect options are removed), "Phone a Friend" (the contestant can make a call to a friend for help), and "Ask the Audience" (the audience votes on the answer, and the results are shown to the contestant).

<br>

Despite being on-air for over two decades, KBC continues to garner high viewer ratings and remains one of the most successful and influential programs on Indian television. Here are the user stories for a terminal-based game inspired by Kaun Banega Crorepati:

1. **Starting the Game**: As a player, I want to be able to start the game so that I can try to win the quiz.

2. **Instructions**: As a player, I want to see instructions on how to play the game, so that I understand the rules and controls.

3. **Questions**: As a player, I want to be asked multiple choice questions, one at a time, so that I can attempt to answer them.

4. **Answers**: As a player, I want to be able to choose my answer from the given options, so I can try to answer the question correctly.

5. **Feedback**: As a player, I want to be informed immediately whether my answer is correct, so I can understand if I'm moving forward in the game.

6. **Score**: As a player, I want to see my current score and how many questions I've answered correctly, so I can track my progress.

7. **Lifelines**: As a player, I want to have lifelines that can assist me when I'm not sure about the answer, so I have a better chance of progressing in the game. These could include Asking the audience,50/50 (where two incorrect options are removed) and Phone a friend (the game suggests a likely answer)

8. **Difficulty Progression**: As a player, I want the questions to get progressively harder as I advance, so that the game remains challenging and engaging.

9. **Quitting the Game**: As a player, I want to be able to quit the game at any point, so I can stop playing when I choose.

10. **High Score**: As a player, I want to see a list of high scores when the game ends, so I can compare my performance to previous games and aim to improve.

11. **Basic Error Handling**: As a user, I want to be informed about what went wrong if I type something incorrectly, so I can correct my mistakes and continue with the game.

12. **Quit**: As a user, I want to be able to quit the game at any point, so I can stop playing when I choose.

13. **Monetary Structure**: As a user, I want to be able to see the monetary structure of the game, so I can track my progress and get a btter idea of how much I'm winning.

14. **Handle Milestones**: As a user, I want to see the winnings as per my last milestone earned, so I can track how much I'm winning.

<br>

**Note**: This is a simple starting point. This implementation covers all the user stories provided above, but it's very basic. It uses a procedural approach, which is fine for a small program like this, but for larger projects, you would want to consider using an object-oriented approach. This would make the code easier to manage and extend. Note that this could be further enhanced with more advanced features, better organization, and better error handling. Here are a certain additions that cam be implemented:
- Introducing a time limit for each answer
- DB or external file for question & answers
- Improved lifeline func. and gameplay
- GUI Implementation
- User profiles & web app functionality
- Backend development
- Better & bigger categories of questions
- More lifelines?
- Unit tests for the functionalities