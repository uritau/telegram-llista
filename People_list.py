class People_list:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.accepted_list = []
    self.rejected_list = []

  def add_member(self, member_name, list):
     
    # Check if member_name is_in_list
    # If not:      ## Add the passed element to accepted_list array
    # Check if is in the other list and delete from there
    # Return if added
    print("add_member")

  def del_member(self, member_name):
    # Check if member_name is_in_list (Accepted or rejected)
    # If is delete from list
    # Return if_deleted
    print("del_member")


