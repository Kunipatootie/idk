import yaml 

def foo(file_path):
    stream = open(file_path, 'r')                 #opens yaml file so that we can read from it
    dictionary = yaml.load(stream)                          #read from the file

    for key, value in dictionary.items():
        print(key + " : " + str(value))
    
    return dictionary


if __name__ == '__main__':                          #

    data = foo("data/example.yaml")