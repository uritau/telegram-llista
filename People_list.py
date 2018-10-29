class People_list:
  
  _name = ""
  _description = ""
  _accepted = []
  
  def __init__(self, name, description):
    self._name = name
    self._description = description
    self._accepted = [""]

  def get_name(self):
    return self._name

  def get_description(self):
    return self._description

  def get_accepted(self):
    return self._accepted

  def set_description(self, description):
        self._description = description
  
  def get_members(self):
        return self._accepted

  def add_member(self,new_accepted):
    self._accepted.append(new_accepted)
    print("add_member")

  def set_name(self, name):
        self._name = name

global lists 
lists = []


def add_list(people_list):
      lists.append(people_list)


#Add user to list
def user_add_list ():
  name = input("""Enter the list name:
     """)
  description = input("Enter the description: ")
  newlist = People_list(name, description)
  add_list(newlist)


#Print all lists
def print_lists():
  print ("There are {} lists".format(len(lists)))


# Print single list 
def show_list(people_list):
  name = people_list.get_name()
  description = people_list.get_description()
  #accepted_list = people_list.get_accepted()
  print ("Name is {} and description {}".format(name,description))


# Select list and print
def choose_list():
    #Check lists not empty 
    lists_names = [list.get_name() for list in lists]
    index = 1
    print ("Available lists: ")
    for name in lists_names:
      print ("[{}]: {}".format(index,name))
      index += 1
    list_id = int(input("Select list: ")) - 1 
    # Check  list_id < len and list_id <= len is valid!
    return (list_id)


# Select list and print
def select_list():
    list_id = choose_list()    # Check  list_id < len is valid!
    print ("Selected id is: {}".format(list_id))
    show_list(lists[list_id])


def show_members():
      list_id = choose_list()
      #show_list(lists[list_id])
      members = lists[list_id].get_members()
      print ("Members: ")
      for member in members:
        print ("{}".format(member))

def add_member():
      list_id = choose_list()
      new_member = input("Enter the new member name: ")
      lists[list_id].add_member(new_member)

def main():
  while True: 
    message = """
What you wanna do? Choose one:
1: add list 
2: show lists
3: Select list
4: add members  
5: show members  

-------------------------
"""
    option = input(message) 
    switch = {
      '1': user_add_list,
      '2': print_lists,
      '3': select_list,
      '4': add_member,
      '5': show_members,
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