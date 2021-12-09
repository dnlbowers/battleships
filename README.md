# **Batleships**

## **Overview**
This program is a computerized version of the original board game battleships, based inside a mock terminal deployed via Heroku.

As a child of the 90's, I used the traditional ship naming conventions from the 1990 Milton Bradley game version over the more modern Hasbro rendition. One can find more info on the rules and the history of the game here on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)). My only deviation was that I reamed the "Carrier" to "Aircraft carrier" to differentiate it from the Cruiser on the board within the app.  

The app replicates the game's enjoyment by allowing the user to play a single-player version against a computerized player.  
  
[Click here to be taken to the final deployment of the project.](https://dnlbowers-battleship.herokuapp.com/)

**AM I RESPONSIVE SCREENSHOT HERE**

## **How to play:**

### ***Firstly select your strategy (setup phase):***  

Place your fate in the hands of the sea god Neptune. Press "q" or type "quick" to let the currents randomly position your ships before you anchor and fire.   

Or  

Before opening fire, choose to spite the sea god and place your ships by pressing "m" or typing "manual.".

Neptune hand will always guide the computerized fleet only to reveal their location with the flames as you hit one.

### ***Firing round:***  

Once in position, it's time to let a rip. Since the radar equipment was broken "accidentally" in the previous battle, you are firing blind and cannot see the other side's ships, choose your coordinates on the map (row , column) and remember to call "FIRE IN THE HOLD" (safety first after all).  

The results of your guess are indicated as follows:  

Hit = :boom:   
Miss = :ocean:  

### ***How to win:***
The last side with a ship still afloat wins. 

## **Planning Phase:**
### ***User stories:***
As a user, I want to be able to:
* See clearly from the offset what the game is.
* Have a straightforward way to read the game instructions from within.
* To access a fun story setting the scene of the game.
* Play an enjoyable game of the classic game battleships by myself.

### ***Site aims:***
The site aim to:
1. Make it clear what the game is without the need for further explanation from external sources.
1. Communicate a clear and appropriate response to all user inputs.
1. Continue in a loop without ever crashing due to an error caused by the user's input.
1. Allow the user to have an enjoyable experience playing battleships by themselves.
  
### ***How will this be achieved:***
To achieve the above, the site will:
1. Provide a welcome screen with the game name in ascii art.
    * Offer the user a chance to read the rules and back story before starting the game.
1. Ensure that all user input provides an appropriate response.
1. Any time the user input is not as expected by the game, the app will show a message to inform the user that their entry was invalid and guide them on how to input as expected.
1. Executing all of the above in a way that successfully replicates the original board game of battleships.

### ***Game Flow Chart:***
To understand the steps required in order to program the game, I created the below flowchart using[lucid charts](https://www.lucidchart.com/).  

![Game Logic Flowchart](docs/flowchart.jpeg) 

<<<<<<<Grammarly done til here>>>>>>>
## **Features**
 
**TO BE DONE WHEN COMPLETE**

## **Future-enhancements**
**TO DO**

## **Data Model**
 **TO DO**

## **Testing Phase**
I have included details of testing both during development and post development in a separate document called [TESTING.md](TESTING.md).

## **Libraries**
For this project to work, I required three imported libraries: -
### ***random***
  * randint used to generate a random number between 0 and 9 for the automated placement and computer guessing
### ***os***
  * system used in conjunction with the clear/cls command to clear the console so the user would not get overwhelmed in reams of outdated data from previous rounds
### ***getch***
  * pause imported from getch to pause the gameplay and give the user more control between turns. This function will also later allow two human players to use the same screen to play against each other. A blank screen could implement this between player turns and a pause until the new player is in play and the previous player has looked away.

## **Deployment**
**TO DO**

## **Honorable Mentions**
* [Mark Cutajar](https://github.com/markcutajar) - Truly, if Data science were a superpower, Mark would be the equivalent of superman. He was with me at several points throughout the development process and was always on call when I needed him to cross-reference my ideas.  
* [Richard Wells](https://github.com/D0nni387) - Taught me what it means to have a mentor. Richard has always been perfect for me as a mentor on this learning journey; however, I understood how to use him to his full potential during this project. Our relationship feels like it has blossomed into junior and senior developers on the same team.
[Sean Murphy](https://github.com/nazarja) - Provided me the pseudo-code I required to print two boards side by side. Not only did he give me exactly what I needed, but he spent the necessary time to break it down and explain it step by step so that I understood the code and was able to adapt it to my project without issue.

* And the biggest thanks goes to my wife and child, who have had to deal with me face to face through it all. Oliver has been my reason for the change and Analise my inspiration. 

## **Credits**
* Python OOP Tutorial series by Corey Schafer for general reference on working with classes and OOP in general  - [First of six videos in the series](https://youtu.be/ZDa-Z5JzLYM)  
* To get a general idea of the game logic, I used this video on the [Devpost Youtube channel](https://youtu.be/zSQIGzmcp2I)  
* The idea to decorate the board with numbers above and to the side came from [Knowledge Mavens youtube channel](https://youtu.be/alJH_c9t4zw)
* Clear console function copied from [delftstack.com](https://www.delftstack.com/howto/python/python-clear-console/)
* How to make a pause for a key to be pressed I referenced from [pretagteam.com](https://pretagteam.com/question/python-press-any-key-to-exit)
* [lucid chart.com](https://www.lucidchart.com/) was used to create the game flow chart
* [Code Institute](https://codeinstitute.net/) for providing the template. The [template](https://github.com/Code-Institute-Org/python-essentials-template) gave me a mock terminal to display my game via a webpage.
* [ASCII Art text generator](http://www.network-science.de/ascii/) used for the welcome screen text.

