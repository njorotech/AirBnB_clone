# 0x00. AirBnB clone - The console
This project is a clone of the AirBnB website.
In this particular project, we create a parent class called BaseModel. The BaseModel class takes care of the initialization, serialization and deserialization of the future instances.

We also created other classes which include User, State, City, Place, Review, and amenity. All these classes inherit from the BaseModel class.

We also created an abstracted storage engine where all the instances of the classes are stored. Our storage is a json file

We also created unittests to validate all our classes and the storage engine.

## Command Interpreter
To access our project and also manipulate data, we created a command Interpreter console.py. 

### How to Start Command Interpreter
1. Clone the repository to your local machine
2. Open your terminal and navigate to the project directory
3. Launch the command interpreter with the command **./console.py**

### How to Use the Command Interpreter
1. After launching the interpreter, you will see a prompt **(hbnb)**
2. Type **help** and enter to see available commands
3. Enter the command of your choice with the required arguments

### Here are some example of commands you can use:
- To create a new object:
  **create object_name key1=value1 key2=value2 ...**
- To update an object:
  **update object_name object_id key=new_value**
- To delete an object:
  **destroy object_name object_id**
- To exit the interpreter:
  **quit**

