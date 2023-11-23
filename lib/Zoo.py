class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animal_names(self):
        animal_names = []
        
        for animal in self.animals:
            name = animal.get_name()
            animal_names.append(name)
            
        return animal_names