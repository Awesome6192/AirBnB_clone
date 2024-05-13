Project Description:

This is the first part of the AirBnB clone project. This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data.
Data (python objects) generated are stored in a json file and can be accessed with the help of the json module in python.

Description of the command interpreter:

The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website. This command line interpreter serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.
And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:
* create - Creates an instance based on given class
* destroy - Destroys an object based on class and UUID
* show - Shows an object based on class and UUID
* all - Shows all objects the program has access to, or all objects of a given class
* update - Updates existing attributes an object based on class name and UUID
* quit - Exits the program (EOF will as well)

How to start it:
First you will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.
After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.

How to use it:
Once the repository is cloned, locate the "console.py" file and run it as follows:
/AirBnB_clone$ ./console.py
When this command is run the following prompt should appear:
(hbnb)
This prompt designates you are in the "HBnB" console.

Format of Command Input:
In order to give commands to the console, these will need to be piped through an echo in case of Non-interactive mode.

In Interactive Mode the commands will need to be written with a keyboard when the prompt appears and will be recognized when an enter key is pressed (new line). As soon as this happens, the console will attempt to execute the command through several means or will show an error message if the command didn't run successfully. In this mode, the console can be exited using the CTRL + D combination, CTRL + C, or the command quit or EOF.

Examples:

Primary Command Syntax:
user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu:~/AirBnB$ ./console.py

Alternative Syntax:
Example: Show all User objects
Usage: <class_name>.all()
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
