from lib.Zoo import * 
from lib.Animal import *
from unittest.mock import Mock


#When the list_animal_names function gets called, 
#it creates a list of the anmail names
def test_integration_test_list_animal_names(): 
    red_panda = Animal("red panda")
    squirrel = Animal("squirrel")
    turtle = Animal("turtle")
    zoo = Zoo("Chester Zoo")
    zoo.add_animal(red_panda)
    zoo.add_animal(squirrel)
    zoo.add_animal(turtle)
    assert zoo.list_animal_names() ==  ["red panda", "squirrel", "turtle"]


# Unit test - list_animal_names
def test_unit_list_animal_names(): 
    mock_animal = Mock()
    # mock_animal.name = "mock animal name"
    mock_animal.get_name.return_value = "mock animal name"

    #  {
    #     name: "mock animal name "
    #     get_name : function return "mock animal name"
    #  }

    zoo = Zoo("Chester Zoo")
    zoo.add_animal(mock_animal)
    assert zoo.list_animal_names() == ["mock animal name"]

