# AirBnB clone - The console

## General Objectives 

- Create a Python package
- Create a command interpreter in Python using the cmd module
- Usage Unit testing and how to implement it in a large project
- Serialize and deserialize a Class
- Write and read a JSON file
- Use of manage datetime
- Use of UUID
- Use of  * args and how to use it
- Use of * kwargs and how to use it
- To handle named arguments in a function.

# Requirements 
- Python Scripts 
- Python Unit Tests 

# The command interpreter 

In order to manage the objects of our program, we create an environment where we can use and execute specific commands that will allow us to manage our program in a more efficient way,

## Interactive mode:
    ➜  AirBnB_clone git:(main) ✗ ./console.py 
    (hbnb)help
    
    Documented commands (type help <topic>):
    ========================================
    EOF  User  all  create  destroy  help  quit  show
    
    (hbnb)
    (hbnb)
    (hbnb)
    (hbnb)quit
    ➜  AirBnB_clone git:(main) ✗ 

##In non-interactive mode:

    ➜  AirBnB_clone git:(main) ✗ echo "help" | ./console.py
    (hbnb)
    Documented commands (type help <topic>):
    ========================================
    EOF  User  all  create  destroy  help  quit  show
    
    (hbnb)%                                                                     
    ➜  AirBnB_clone git:(main) ✗ 

## Usage of commands

Syntax : quit
------------
Command to exit the program

    ➜  AirBnB_clone git:(main) ✗ ./console.py 
    (hbnb)
    (hbnb)quit
    ➜  AirBnB_clone git:(main) ✗ 

Syntax : EOF
------------
Command to exit the program

    ➜  AirBnB_clone git:(main) ✗ ./console.py
    (hbnb)
    (hbnb)EOF
    ➜  AirBnB_clone git:(main) ✗ 
    

Syntax : create
------------
Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.

    ➜  AirBnB_clone git:(main) ✗ ./console.py
    (hbnb)
    (hbnb)create
    ** class name missing **
    (hbnb)create MyModel
    ** class does not exist **
    (hbnb)create BaseModel
    .9fbd3cc9-3e0b-411b-ac1b-5a8e01b64a1d
    (hbnb)
    (hbnb)

Syntax : show
------------
Prints the string representation of an instance based on the class name and id.

    ➜  AirBnB_clone git:(main) ✗ ./console.py
    (hbnb)
    (hbnb)show
    ** class name missing **
    (hbnb)show MyModel
    ** class doesnt exist **
    (hbnb)show BaseModel
    ** instance id missing **
    (hbnb)show BaseModel 121212
    ** no instance found **
    (hbnb)
    (hbnb)show 9fbd3cc9-3e0b-411b-ac1b-5a8e01b64a1d
    ** class doesnt exist **
    (hbnb)show BaseModel 9fbd3cc9-3e0b-411b-ac1b-5a8e01b64a1d
    [BaseModel] (9fbd3cc9-3e0b-411b-ac1b-5a8e01b64a1d) {'created_at': datetime.datetime(2021, 11, 13, 23, 5, 18, 456036), 'id': '9fbd3cc9-3e0b-411b-ac1b-5a8e01b64a1d', 'updated_at': datetime.datetime(2021, 11, 13, 23, 5, 18, 456053)}
    (hbnb)
	

Syntax : destroy
------------
Deletes an instance based on the class name and id (save the change into the JSON file).

    ➜  AirBnB_clone git:(main) ✗ ./console.py
    (hbnb)
    (hbnb)destroy
    ** class name missing **
    (hbnb)destroy MyModel
    ** class doesnt exist **
    (hbnb)destroy BaseModel
    ** instance id missing **
    (hbnb)destroy BaseModel 121212
    ** no instance found **
    (hbnb)destroy BaseModel 9fbd3cc9-3e0b-411b-ac1b-5a8e01b64a1d
    (hbnb)


Syntax : all
------------
Prints all string representation of all instances based or not on the class name.

    ➜  AirBnB_clone git:(main) ✗ ./console.py
    (hbnb)
    (hbnb)all BaseModel
    [BaseModel] (d4f94723-c724-4803-a92c-342a69dee1d7) {'created_at': datetime.datetime(2021, 11, 12, 20, 21, 40, 173122), 'id': 'd4f94723-c724-4803-a92c-342a69dee1d7', 'my_number': 89, 'name': 'My_First_Model', 'updated_at': datetime.datetime(2021, 11, 12, 20, 21, 40, 173128)}
    [BaseModel] (d7b39e6f-3694-4380-b892-6c79faae9361) {'created_at': datetime.datetime(2021, 11, 12, 20, 21, 42, 356737), 'id': 'd7b39e6f-3694-4380-b892-6c79faae9361', 'my_number': 89, 'name': 'My_First_Model', 'updated_at': datetime.datetime(2021, 11, 12, 20, 21, 42, 356743)}
    [BaseModel] (f50daab2-e7b7-4ae9-98fc-5681c59a2fbb) {'created_at': datetime.datetime(2021, 11, 12, 20, 21, 25, 303542), 'id': 'f50daab2-e7b7-4ae9-98fc-5681c59a2fbb', 'my_number': 89, 'name': 'My_First_Model', 'updated_at': datetime.datetime(2021, 11, 12, 20, 21, 25, 303566)}



Syntax : Update
------------
Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).



```flow
st=>start: Console
op=>operation: create
cond=>condition: Successful Yes or No?
e=>end: quit

st->op->cond
cond(yes)->e
cond(no)->op
```

[AUTHORS](http://https://github.com/Mahalaksmy/AirBnB_clone/blob/main/AUTHORS "AUTHORS")

Carolina Lopera Correa 
Dairo Julian Carlosama 
Maha Laksmy Amariles 
