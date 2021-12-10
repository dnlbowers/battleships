# Ocean battalion - 
This game is a take on the original board game battle ship. Based inside of a mock terminal deployed via Heroku.

As I was a child of the 90's I used the traditional ship naming conventions from the 1990 Milton Bradley game version over the more modern Hasbro rendition. More info on this, the rules and the games history can be found here on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

The scene begins you are in deep waters. Mid sea battle the command comes in over the radio that the war is over, trouble is you still have some ammunition left and there are rounds left in the chamber... it would be irresponsible to leave live rounds in the chamber.... definitely dangerous to do so in fact.... 

To be a good captain and save your own men from accidental onboard detonation you agree to fire "randomly" into the sea. Trouble is the other sides fleet captain had the same idea.....

With both sides racing to release all their rounds (and some extra that "slipped" into the torpedo chamber when the last one was fired :wink:) the obvious winner is the last man standing. The war may be over but this battle has just begun!

Choose a quick start for the your ships to be randomly placed or select your battle arrangement manually. Whatever you decide may the tides of fortune forever be in your favor.

## Game Logic

![Game Logic Flowchart](docs/flowchart.jpeg)

## How to play

* I needed a way to check if a ship had already been place on a tile. I was trying to access the coordinates from the ship obj directly and bu simply using += to add to the list the was no definition between the set of coords (row, column). when I then realized the error saying that fleet[i].coordinates error saying it lack the append attribute I realized I could do  from with in the build fleet function using the predefined list and the coords used to innit the obj. after realising this I was able to use occupied_coordinates.append(tuple(random_start)) to place the row and column coordinate as a tuple set with in the predefined occupied_coordinates list.
  * This changed - go back to review
##issues/testing (rough notes)






* randomize the starting player
  
## Credits:



# To be deleted when finally deployed
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome dnlbowers,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!