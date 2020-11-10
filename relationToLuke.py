def relation_to_luke():
    ##prompting user for their name
    person = input("What is your name? : ")
    ##printing first part of sentance out note would be better to include
    ##the contents of the print statement in each if statement as the print()
    ##function ends the line automatically
    print("Luke I am your ")
    ##test cases for each name.
    if(person == "Darth Vader"):
        print("father")
    elif(person == "Leia"):
        print("sister")
    elif(person == "Han"):
        print("brother in law")
    elif(person == "R2D2"):
        print("droid")
    else:
        print("nothing")

    """RESEARCH: Are there switch statements in Python?
    ANSWER: Yes! there are. format is as follows:
    def switch_demo(argument):
        switcher = {
            1: "Darth Vader"
            and so on for however many cases
        switcher.get(argument, "Invalid name")
    Note that this actually wouldn't be a valid choice here because in order to 
    access "Darth Vader" we would have to type the number 1 when calling the 
    switch statement. A way around this is to use Dictionary mapping, which I
    don't understand at this point but will research more later on.
    
    """
