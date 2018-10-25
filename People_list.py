class People_list:
  
  _name = ""
  _description = ""
  _accepted = []
  
  def __init__(self, name, description):
    self._name = name
    self._description = description
    self._accepted = []

  def get_name(self):
    return self._name

  def get_description(self):
    return self._description

  def get_accepted(self):
    return self._accepted

  def set_name(self, name):
    self._name = name

  def set_description(self, descriphttps://stackabuse.com/reading-and-writing-json-to-a-file-in-python/n):
    self._description = descriptionhttps://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

  def add_member(self,new_accepted):
    self._accepted.append(new_accepted)
    print("add_member")


global lists 
lists = []


def add_list(people_list):
      lists.append(people_list)


#Add user to list
def user_add_list ():https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
  name = input("""Enter the list https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/name:
   """)https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
  description = input("Enter the https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/list description: ")
  newlist = People_list(name, description)
  add_list(newlist)


#Print all lists
def print_lists():
  print ("There are {} lists".format(len(lists)))
  for list in lists:
      show_list(list)


# Print single list 
def show_list(people_list):
  name = people_list.get_name()
  description = people_list.get_description()
  accepted_list = people_list.get_accepted()
  print ("Name is {} and description {}".format(name,description))


# Select list and print
def select_list():
    #Check lists not empty 
    lists_names = [list.get_name() for list in lists]
    index = 1
    print ("Select which list you wanna read: ")
    for name in lists_names:
      print ("[{}]: {}".format(index,name))
      index += 1
    list_id = int(input("Which list do you wanna read?")) - 1 
    # Check  list_id < len is valid!
    print ("Selected id is: {}".format(list_id))
    show_list(lists[list_id])

def main():

  while True: 
    message = """
What you wanna do? Choose one:
1: add list 
2: show lists
3: Select list  
-------------------------
"""
    option = input(message) 
    switch = {
      '1': user_add_list,
      '2': print_lists,
      '3': select_list,
    }
    switch[option]()


if __name__ == "__main__":
    main()


    # Llistar llistes
# Eliminar llista

# Afegir membre a llista

# Treure membre de llista

# Mostrar llista

#-------------
#Afegir algú 



# Read and write to disk:

# data/channel_id/list_name.json <= https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/