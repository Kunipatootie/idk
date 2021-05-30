import yaml 

if __name__ == '__main__':                          #

    stream = open("data/example.yaml", 'r')                 #opens yaml file so that we can read from it
    dictionary = yaml.load(stream)                          #read from the file
    print(dictionary.items)
    #for key, value in dictionary.items():                   
    #    print (key + " : " + str(value))

        