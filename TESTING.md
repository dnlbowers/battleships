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

## **Bugs**
**TO DO**

## **Remaining Bugs**
At the time of submission no bugs remained in the app.

## **Validator Testing**
### ***PEP8:***
* Due to the use of linters and the autopep8 command line function referenced above, [PEP8online.com](http://pep8online.com/) returned no errors.