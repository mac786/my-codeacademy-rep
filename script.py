#from trie import Trie
from data import *
#from welcome import *
#from hashmap import HashMap
from linkedlist import LinkedList, Node

class StackInput:
  def __init__(self,name):
    self.size =0
    self.top_item = None
    self.limit = 100
    self.name = []
    #self.array = name[]

  def push(self,value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size +=1
    else:
      print("No more room on stack")

  def pop(self):
    if self.size >0:
      item_to_remove = self.top_item
      self.top_item =item_to_remove.get_next_node()
      self_size =-1
      return self.top_item.get_value()
    else:
      print("This stack is totally empty")

  def peek(self):
    if self.size  >0:
      return self.top_item.get_value()
    print("Nothing to see here")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size ==0

  def get_size(self):
    return self_size

  def return_reversed(self):
    pointer = self.top_item
    reversed_list = []
    while (pointer):
      reversed_list.append(pointer.get_value())
      pointer = pointer.get_next_node()

    reversed_list.reverse()
    return reversed_list

#Printing the Welcome Message
#print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py
# to test include extra item with g ie guernsey

# Working code
#food_types = list(types)
#reversed_food_types = food_types[::-1]
#print(reversed_food_types)
# test: print(food_types[1]) => [0] gives 'german' and [1] gives 'japanese'
#food_input_stack = StackInput(reversed_food_types)
#for i, types in enumerate(food_types):
    #food_input_stack.push(types)
    #first_letter =
    #print("types: {0} and {1}".format(types,food_input_stack.peek()))

#food_types.insert(1,'guernsey')
#print(food_types)
#print(hashmap_food_type[0])

#class data_convert:
  #def __init__(self,list):
    #self.list = list
    #self.hash_map = HashMap(len(list))

  #def list_to_stack(self,size_list):
    #self.array = size_list


#Write code to insert restaurant data into a data structure here. The data is in data.py


#Write code for user interaction here
# OUTER WHILE LOOP
while True:
    printable_list = []
    #user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
    user_input = 'ger'
    response = list(user_input.split())

    reversed_input_list = response[::-1]
    reversed_stack = StackInput(reversed_input_list)
    print(reversed_stack)

#return False
    #for i, char in enumerated(user_input_list):
      #reversed_stack.push(char)




    #final_selected_food_type = len(user_input)
    #choice_more_than_one_do_again = 'y'

    # INNER WHILE LOOP
    #While choice_more_than_one_do_again == 'y':
      # Keep requesting for more letters until food_type identified
      #user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
      # parse this user_input into a single letter list
      # reverse this list
      # store it in a stack

      # compare the first letter at top of stack to HashMap key
      # if found copy list HashMap[1] to printable_list
      # print to screen the ['available , options'] by printing input() below.
      # if len(printable_list) == 1
        # Then we can search for this in restaurents data
        #After finding food type write code for retrieving restaurant data here
        # Search printable_list = food_type_selected find restaurents in data store in list store in retrieved_list
        #print("With those beginning letters your choices are {0}".format(retrieved_list))
      # else len(printable_list) > 1
        # choice_more_than_one_do_again =input("The {0} restaurents in SoHo are {1} \n Do you want to find other restaurents?\n Enter 'y' for yes and 'n' for no".format(user_input,printable_list)
        # if  choice_more_than_one_do_again = 'y' reloop to request user_input once again "inner while loop"
        # if  choice_more_than_one_do_again = 'n' end program by looping outer
      # return False

    #else:


    #Search for user_input in food types data structure here
    # make a list of individual characters
    #user_input_list = []
    #for i, character in enumerate(user_input):
      # check if the first character key is in hash map - for that key call up linkedlist which contains values for that key.
      #results_from_first_character = []
      #user_input_list += character
      #print(user_input_list[i])

    #print(user_input_list)

    #for char in user_input:
      #print(user_input_list[0])

    # Not neccesary to convert string to a list
    # user_input_list = [user_input]
    # print(user_input_list[0])
    #-------------------------------------------

    #for character in range(len(user_input)) :
        #if user_input[character] == types[0:1]:
          #print(types[0])
        #else:
          #print("Not working?")
# Test programs
