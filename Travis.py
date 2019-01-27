#This is a simple little program that checks to see if someone is in
#A list of known users. If you are in the list, kudos! If not, then
#Travis, the security program will ask you if you would like to be
#Added to the list

known_users = ["Andrew", "Billy", "Clarice", "Dumont", "Eugene", "Felix", "Greg", "Harold"]



while True:
    print()
    print("Hi there! My name is Travis.")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Name recognised. Hello there, {}!".format(name))
        remove = input("Would you like to be removed from the system? (y/n)?: ").lower()
        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print()
            print("Here is the updated list")
            print()
            print(known_users)
            
    else:
        print("Name NOT recognised")
        add = input("Would you like to be added to the system? (y/n?: ").lower()
        if add == "y":
            print(known_users)
            known_users.append(name)
            print()
            print("Updating list.......")
            print()
            known_users.sort()
            print(known_users)
            
    
    
      
