# **Testing**
## **Table of Contents:**
* [**Testing**](#testing)
  * [**Table of Contents:**](#table-of-contents)
  * [**Manual Testing:**](#manual-testing)
    * [***PEP8 Linter:***](#pep8-linter)
    * [***Inputs:***](#inputs)
    * [***Game Play:***](#game-play)
  * [**Bugs and Fixes**](#bugs-and-fixes)
    * [**Remaining Bugs**](#remaining-bugs)
  * [**Post Development Testing**](#post-development-testing)
    * [**Validators**](#validators)
      * [***HTML*** - https://validator.w3.org/nu/](#html---httpsvalidatorw3orgnu)
      * [***CSS*** - https://jigsaw.w3.org/css-validator/](#css---httpsjigsaww3orgcss-validator)
      * [***Python:*** - http://pep8online.com/](#python---httppep8onlinecom)

## **Manual Testing:** 
I performed manual testing throughout this project in the following ways:
### ***PEP8 Linter:***
To begin with, I was using Pylint to lint my code. The reason for this was that I was developing on my local machine using Vscode and a virtual environment meaning flake8 was not working for me. After some research, I discovered the error with flake8 was in the Code Institute settings Json where CI had set the file path for the linter according to the Gitpod virtual environment. After deleting the file path and installing flake8 with the pip install command, I continued developing with the course-recommended linter.

During the above investigation, I also noticed the below line in the settings Json of the code institute template. I began to wonder what it was: -   
 
 "python.formatting.autopep8Path"

A quick google search revealed the following console command "$ autopep8 --in-place --aggressive --aggressive run.py", and after executing this command, the function formatted my code perfectly in line with PEP8 coding conventions.

### ***Inputs:***
I have tested all inputs with strings where expecting integers, integers where expecting strings and adding spaces to the input value.  

Lastly, I challenged the slack community to break the app in any way possible which by the deployment of final product was not possible.   

### ***Game Play:***
Throughout development, I was testing the game in the terminal of VScode as well as several playing multiple rounds in the Code Institute terminal template for each deployment to Heroku.

The end result is a robust game which stays playing continuously without error.

## **Bugs and Fixes**
1. **Intended Outcome:** - Well-defined classes containing related methods.
    * ***Issue Found:***
        * At first, I attempted to make everything a sub-class of Player. However, after much research, I found this improper use of OOP. 
    * ***Causes:*** 
        * By making Player a superclass I was telling the computer that the board and ship were a type of Player, which is not the case. Player, Board, and Ship are all three distinct object types.
    * ***Solution Found:***  
        * Instead of using inheritance, to allow for cross-functionality I opted for giving all objects a relationship with each other through belonging/possession, this was achieved by:   
            * Creating the board object as part of the Player init method. This meant that the Player possessed the board object.   
            * The Ship objects are created in the build_fleet method of the board, making a list of ships belonging to a particular player's board.
     
1. **Intended Outcome:** - Placing every ship on an original set of tiles with no overlap.
    * ***Issue Found:***
        * I initially tried to append the start tile directly to the ship coordinates, which led to no definition between a set of coordinates.
    * ***Causes:*** 
        * At this stage of development, I had yet to convert the start position input into a tuple. Not having a tuple of two numbers meant that when a player entered two numbers, the code added them to the list as individual numbers.  
    *  ***Solution Found:***  
        *  At the start of the function, I created an empty list of occupied tiles, enabling me to use occupied_coordinates.append(tuple(random_start)). This line of code later turned into occupied_coordinates.append(ship_instance.coordinates), which updated the list with the full coordinates of each ship so they could never start from a duplicate tile. The occupied_coordinate list was then later fed back into the build ship function to ensure that tiles could not be reused when placing a ship.

1. **Intended Outcome:** - A auto place option offered to the user allowing for a quick start game feature.
    * ***Issue Found:***
        * When it came to the computer player's turn, it offered me the choice to place the ship on the board manually.
    * ***Causes:***
        * The interpreter could not distinguish a difference between the intended AI player and the intended human player.  
    * ***Solution Found:*** 
        * By adding an if statement in the Player init method, I could set the call of the board class to start with the auto set up as default when the string "computer" was added into the objects constructor call. 
        * The downside to this was that the app could be broken easily by the player entering their name as "computer."
            * This was then resolved within the Game class method "name_input." I added a conditional statement that printed a tongue-in-cheek reason why the human player could not also be called "computer". It did occur to me that I could have also added a variable into the init called human_player as a boolean; however, I preferred my final solution to add an element of personality to a classical game.

1. **Intended Outcome:** - Recognizing the non-human player and skipping the manual ship placement.
    * ***Issue Found:***
        * When initializing the computer player, the app was still offering the choice to place the computer's ships manually. 
    * ***Causes:*** 
        * Originally, I used an *args parameter to pass in the list of occupied coordinates. The auto-placement was passed in after the *args parameter and added to the list passed with the *args parameter. 
        * I later discovered this was an incorrect use of *args, and despite the first fix below working, the real issue was that the function was reading the first parameter as "self".
    * ***Solution Found***
        * The first solution was to move the *args to the last passed parameter, which worked but was an improper use of *args.
        * I later realized that the interrupter read the first parameter as "self". Removing the *args and adding "self " as the first parameter worked as the final resolution for the method function.
         
1. **Intended Outcome** - Search through a list of occupied tiles when placing a ship and return a boolean value to indicate whether or not the passed guess has been used before. 
   * ***Issue Found:***
        * My statements to read the lists containing the already occupied tiles were failing to work correctly.
    * ***Causes:*** 
        * I only checked the outer list with my conditional statements and not the lists within the lists.
    * ***Solution Found:***
        * By creating a nested for loop to check each item of each nested list and returning a boolean value when it found a match or not. I assigned the static method containing the for loop to a variable and successfully used it as a conditional. 

1. **Intended Outcome** - Until the user gives a valid input, the code will loop around and provide feedback to the user.
    * ***Issue Found:***
        * Many infinite loops in the process of trying to set this up.
    * ***Causes:***
        * There was an instance where I neglected to define the escape variable before the loop.
        * I ran the code with a conditional statement that couldn't trigger within the while loop.
    *  ***Solution Found:***
        * A combination of return statements, break, and booleans assigned to variables.

1. **Intended Outcome** - A dictionary with occupied tiles as the key and ship symbol as the value. The app would then check the guess and find the correct ship to update the damaged tiles on.
    * ***Issue Found:***
        * Trying to zip() the list of coordinates together with the ship symbol returned an error.
    * ***Causes:***
        * Due to the list lengths being different sizes, the zip() method could not join all the ship's coordinates with a single defined symbol of the ship instance.
    *  ***Solution Found:***
        * When defining the ship symbol in the subclasses of the ship class, I multiplied the symbol by the ship's length, creating two lists of equal size to be zipped together into a dictionary.

1. **Intended Outcome** - All ships placed on the board after all tile coordinates in a ship instance were deemed original.
    * ***Issue Found:***
        * Although the console showed no error, the ship failed to show up on the board after the placement phase.
    * ***Causes:***
        * I used the append method to append the ship symbol to the board 2d array.
    *  ***Solution Found:***
        * By changing append to the assignment operator (=) I resolved the issue.

1. **Intended Outcome** - When a player made a guess, the opponent's board could be accessed and updated accordingly.
    * ***Issue Found:***
        * without using the global scope allowing instance of an object to manipulate the data of another object.
    * ***Causes:***
        * This was caused mostly by my inexperience in working with OOP and classes.
    *  ***Solution Found:***
        * Originally, I passed the opponent board into a class method that existed before I created the object, so it was not necessarily a correct way to use OOP.
        * In the end, I created a new Game class for the game loop and created the Player objects within it. From there, I was able to access the methods of both objects with constructors and parameters.

1. **Intended Outcome** - A continuous loop of guess and guess results until someone sank all five of the other player's ships.
    * ***Issue Found:***
        * After a player had sunk three ships, every guess returned a symbol for a miss even though I could see it was hitting a ship.
    * ***Causes:***
        * I was using the function "self.fleet_coords_map()" and not the init variable "self.map_of_fleet" in the code, causing the dictionary to rebuild every time a player took a turn. Since there were fewer ships in the object once a player sank one, The for loop creating the dictionary would loop fewer times, thus omitting some of the later created ships.. 
    *  ***Solution Found:***
        * Began calling this dictionary with "self.map_of_fleet" thereby accessing the dictionary generated during the setup phase and not a new dictionary formed by looping less because fewer ships in the board object instance.

1. **Intended Outcome** - The user's guess results accurately reflect hit or miss on their guess board.
    * ***Issue Found:***
        * When testing he deployed game hits were showing in random positions that didn't make sense when taking into account ship length.
    * ***Causes:***
        * I included the constructor for the computer player inside the firing round while loop, which generated a new computer player board/fleet every time the while loop repeated itself.
    *  ***Solution Found:***
        * Moving the computer player constructor outside of the while loop resolved. The solution meant the player object "computer" was created only once.

1. **Intended Outcome** - Ascii art text for the intro screen displayed as legible words.
    * ***Issue Found:***
        * The text printed partially formed, and the console appeared to push several characters to the right-hand side of the text instead of being printed within it.
    * ***Causes:***
        * The backslashes in the Ascii art were being read as escape characters and not being printed in place. The lines containing the backslash had moved from their intended position in the text.
    *  ***Solution Found:***
        * The first solution was to add a single space after each line which converted the backslash into a string. This solution, however, returned errors with the linter and pep8 online.
        * I eventually realized that adding a second backslash next to every backslash would turn the escape character into a single backslash and print correctly in the terminal.

1. **Intended Outcome** - Favicon displayed in the browser tab.
    * ***Issue Found:***
        * When adding the image to the directory and linking it in the template HTML, nothing showed up on the deployed site.
    * ***Causes:***
        * There are some limitations with the CI template that prevents adding favicons in the way used in my previous projects
    *  ***Solution Found:***
        * By switching to using the URL of a web-hosted image, the favicon is displayed correctly.

### **Remaining Bugs**
At the time of submission no bugs remained in the app.

## **Post Development Testing**
### **Validators**

#### ***HTML*** - https://validator.w3.org/nu/

* ***Issue Found:***
    * The SVG file contained attributes written in non English language and hence the validator returned the below error: 
![HTML Validator Error](docs/screenshots/html-validator-error.jpg)

* ***Solution Used:***
    * Placing the attribute, 'lang="ca"' in the div containing the background image fixed this.

#### ***CSS*** - https://jigsaw.w3.org/css-validator/

* The page was tested by passing the URL to the validator, with no issues found.  
![CSS Validator Badge](https://jigsaw.w3.org/css-validator/images/vcss)  

#### ***Python:*** - http://pep8online.com/
* Due to the use of linters and the autopep8 terminal command referenced above, [PEP8online.com](http://pep8online.com/) returned no errors.

[return to README.md](README.md)