name = str(input("What is your name? : "))
print(f"Hello {name}, Welcome to FLAMES GAME!")
print("This game does not accurately predict whether or not an individual is right for you")
print("It's just for fun!")

name1 = input("Enter the name of the 1st person: ").upper()
name2 = input("Enter the name of the 2nd person: ").upper()


name1 = name1.replace(" ", "")
name2 = name2.replace(" ", "")

list1 = list(name1)
list2 = list(name2)

def remove_common_letters(list1, list2):
    """
    Removes common letters from two lists.
    """
    for letter in list1[:]:
        if letter in list2:
            list1.remove(letter)
            list2.remove(letter)


if __name__ == "__main__":
    remove_common_letters(list1, list2)

count = len(list1 + list2)  

if count > 0:
    flame_list = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"] 
    while len(flame_list) > 1:
        index = count % len(flame_list) - 1
        if index >= 0:

            flame_list = flame_list[index+1:] + flame_list[:index]
        else:

            flame_list = flame_list[:len(flame_list)-1]
    
    print("Relationship result based on FLAMES:", flame_list[0])
else:
    print("Please enter valid names.")  

        
     


    

