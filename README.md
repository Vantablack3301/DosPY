# DosPY
a flask container for doom basically making it unblock-able from schools

do note that it technically can be run with githb pages, this would only remove the flask security layer and make it possible to block from schools

# Add more games
to add more games to your own branch, you must first upload the zip file for your dos game. i recommend that you
modify it with whatever needed changees you want (controlls, wads, ect). then make a new html file in the templates
file. copy the code from one of the templates and paste it to the new one. then modify the code and point it twords your
zip file and change the built in directory to the corresponding one of the zip file. in short, point it to the zip, and then the exe location within the zip file.

after that it needs to be initialized in the flask container too. this is optional if you dont really care about the flask layer. to do this, add another directory in the main.py script. its okay to copy one of the other existing directorys, just be sure to rename it for it to work. also be sure to point it in the direction of your new page rather than the old page.

# additional info
this project was made with repl.it and therefore works best with that. to run it in repl, create a new project from this repo and set the language to python. also make it run the main.py script in the file.

alternatively you can find the repl project and simply fork it there. although im not too sure about things like the whole github commit feature working.
