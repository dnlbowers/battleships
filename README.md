# **Batleships**

## **Overview**
This program is a computerized version of the original board game battleships, based inside a mock terminal deployed via Heroku.

As a child of the 90's, I used the traditional ship naming conventions from the 1990 Milton Bradley game version over the more modern Hasbro rendition. One can find more info on the rules and the history of the game here on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)). My only deviation was that I reamed the "Carrier" to "Aircraft carrier" to differentiate it from the Cruiser within the app.  

The app replicates the game's enjoyment by allowing the user to play a single-player version against a computerized player.  
  
[A link to the live site can be found here](https://dnlbowers-battleship.herokuapp.com/)

**AM I RESPONSIVE SCREENSHOT HERE**

## **How to play:**

### ***Firstly select your strategy:***  

Place your fate in the hands of the sea god Neptune. Press "q" or type "quick" to let the currents randomly position your ships before you anchor and fire.   

Or  

Before opening fire, choose to spite the sea god and place your ships by pressing "m" or typing "manual.".

Neptune hand will always guide the computerized fleet only to reveal their location with the flames as you hit one.

### ***Firing round:***  

Once in position, it's time to let a rip. Since the radar equipment was broken "accidentally" in the previous battle, you are firing blind and cannot see the other side's ships, choose your coordinates on the map (row , column) and remember to call "FIRE IN THE HOLD" (safety first after all). The results of your guess are indicated as follows:  

Hit = %  
Miss = X

### ***How to win: ***
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


## **Data Model**
 **TO DO**

## **Libraries**
**TO DO**
Random - rand int and randchoice
OS - Clear screen
getch (pause) - allowed pause for key press

## **Testing**
**TO DO**
since I used the command $ autopep8 --in-place --aggressive --aggressive run.py to format the document no errors were found on pep8

## **Bugs**
**TO DO**

## **Remaining Bugs**
**TO DO**

## **Validator Testing**
**TO DO**

## **Deployment**
**TO DO**

## **Honorable Mentions**
Mark Cutajar
Richard Wells
Sean Murphy

## **Credits**
* Python OOP Tutorial series by Corey Schafer for general reference on working with classes and OOP in general  - [First of six videos in the series](https://youtu.be/ZDa-Z5JzLYM)  
* To get a general idea of the game logic, I used this video on the Devpost Youtube channel - https://youtu.be/zSQIGzmcp2I  
* The idea to decorate the board with numbers above and to the side came from Knowledge Mavens youtube channel - https://youtu.be/alJH_c9t4zw
* Clear console function copied from https://www.delftstack.com/howto/python/python-clear-console/
* How to make a pause for a key to be pressed I referenced from here - https://pretagteam.com/question/python-press-any-key-to-exit
* https://www.lucidchart.com/ - used to create the game flow chart
* Code Institute for providing the template. The template gave me a mock terminal to display my game via a webpage.
* ASCII Art text generator used for into text http://www.network-science.de/ascii/

