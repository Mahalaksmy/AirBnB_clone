class FileStorage():
    """ Class FileStorage"""

    __file_path = './file.json'
    __objects =  {}

    def all(self):
        """ Returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        
    def save(self):
        """serializes __objects to the JSON file (path: __file_path) """

        with open('self.___file_path', "w") as write_file:
            json.dump(self.__objects, write_file, indent=4, sort_keys=True)
        
    def reload(self):
        """ eserializes the JSON file to __objects"""
        
        if os.path.exists(self.__file_path):
            with open('self.___file_path', "r") as write_file:
                json.load(self.__objects, write_file, indent=4,sort_keys=True )
