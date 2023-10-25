print("Practicing Python Basics")

def space(function):
    print("\n{}".format("-" * 10))
    print("{}".format(function))
    print("{}\n".format("-" * 10))
    #can also do like this:
    #print("\n{my_text}\n".format(my_text = "-" * 3))

def main():
    #im gonna selectively run my functions here
    print("Main")
    '''
    test_title = "Title"
    space(test_title)
    '''
    classes()

def classes():
    title = "Classes" 
    space(title)

    class PersonName:
        def __init__(self,first_name,last_name):
            self.first_name = first_name
            self.last_name = last_name

    #using the class we just set
    my_person = PersonName(input("First Name: "),input("Last Name: "))
    print("Hi, my name is {fn} {ln}".format(fn = my_person.first_name, ln = my_person.last_name))



main()