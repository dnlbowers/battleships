## **Testing**
I performed manual testing throughout this project in the following ways:
### ***PEP8 linter:***
To begin with, I was using Pylint to lint my code. The reason for this was that I was developing on my local machine using Vscode and a virtual environment meaning flake8 was not working for me. After some research, I discovered the error with flake8 was in the Code institute settings Json where CI had set the file path for the linter according to the Gitpod virtual environment. After deleting the file path and installing flake8 with the pip install command, I continued developing the course-recommended linter.

During the above investigation, I also noticed the below line in the settings Json of the code institute template. I began to wonder what it was: -   
 
 "python.formatting.autopep8Path"

A quick google search revealed the following console command "$ autopep8 --in-place --aggressive --aggressive run.py", and after executing this command, the function formatted my code perfectly in line with PEP8 coding conventions.

### ***Inputs**
I have tested all inputs with strings where expecting integers, integers where expecting strings and adding spaces to the input value.  

Lastly, I challenged the slack community to break the app in any way possible which by the deployment of final product was not possible.   

### ***Game play:***
Throughout development, I was testing the game in the terminal of VScode as well as several playing several rounds in the Code Institute terminal template for each deployment to Heroku.

The end result is a robust game stays playing continuously without error.

## **Bugs and Fixes**
1. **Intended outcome:** - Well-defined classes containing related methods.
    * ***Issue Found:**:*
        * At first, I attempted to make everything a sub-class of Player. however, after much research, I found this improper use of OOP. 
    * ***Causes:*** 
        * By making Player a superclass I was telling the computer that the board and ship were a type of Player, which is not the case. Player, Board, and Ship are all three distinct Object types.
    * ***Solution Found:***  
        * Instead of using inheritance, to allow for cross-functionality I opted for giving all objects a relationship with each other through belonging/possession by:   
            * Calling the board function in the Player Innit method, meaning that the Player possessed the board object.   
            * The Ship objects are created in the build_fleet method of the board, making a list of ships belonging to a particular player's board.
     
1. **Intended outcome:** - Placing every ship on an original set of tiles with no overlap.
    * ***Issue Found:***
        * I initially tried to append the start tile directly to the ship coordinates, which led to no definition between a set of coordinates.
    * ***Causes:** 
        * At this stage of development, I had yet to convert the start position input into a tuple. Not having a tuple of two numbers meant that when a player entered two numbers, the code added them to the list as individual numbers.  
    *  ***Solution Found:***  
        *  At the start of the function, I created an empty list of occupied tiles, enabling me to use occupied_coordinates.append(tuple(random_start)). This line of code later turned into occupied_coordinates.append(ship_instance.coordinates), which updated the list with the full coordinates of each ship so they could never start from a duplicate tile. The occupied_coordinate list was then later fed back into the build ship function to ensure that tiles could not be reused when placing a ship.

1. **Intended Outcome:** - A auto place option offered to the user allowing for a quick start game feature.
    * ***Issue Found:***
        * When it came to the computer player's turn, it offered me the choice to place the ship on the board manually.
    * ***Causes:***
        * The interrupter could not distinguish a difference between the intended AI player and the intended human player.  
    * ***Solution Found:*** 
        * By adding an if statement in the Player innit method, I could set the call of the board class to start with the auto set up as default when the name "computer" was added as in string into the objects constructor call. 
        * The downside to this was that the app could be broken easily by the player entering their name as "computer."
            * This was then resolved within the Game class method "name_input." I added a conditional statement that printed a tongue-in-cheek reason why the human player could not also be called "computer". It did occur to me that I could have also added a variable into the innit called human_player as a boolean; however, I preferred my final solution to add an element of personality to a classical game.



## **Remaining Bugs**
At the time of submission no bugs remained in the app.

## **Validator Testing**
### ***PEP8:***
* Due to the use of linters and the autopep8 command line function referenced above, [PEP8online.com](http://pep8online.com/) returned no errors.