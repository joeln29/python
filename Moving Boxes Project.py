"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name: Joel N
Project: Moving Boxes
"""


class MovingBox:
    """
    A class for keeping track of the contents of
    a moving box. Items can be added to, removed from,
    itemized (i.e. listed), and searched from a moving box.
    The number of items in a box can also be queried
    and items can be transferred between two boxes.
    """
    def __init__(self, name):
        """
        Constructor, initializes the newly created object(s)
        :param name: str, the name of the created box
        """
        # Because dictionary self.__goods is not needed in every method, it's
        # not located in the init section. Dictionary contains all the elements
        # in specific location. Self name stores each box's name.
        self.__name = name
        self.__goods = {}

    def box_name(self):
        """
        Specify boxes by giving them a unique name
        :return: the name of the box
        """
        return self.__name

    def add_item(self, name, count):
        """
        Add object and number of how many of them you want to add
        :param name: srt, name of the added object
        :param count: int, how many object(s) you want to add
        :return: doesn't return anything, only adds item(s) in the box
        """
        # If there is an object in the dictionary already, just increase the
        # value by "count"
        if name in self.__goods:
            self.__goods[name] += count
        # If there isn't an object called "name" in the box, create one
        else:
            self.__goods[name] = count

    def list_content(self):
        """
        List all the items in the boxes. (The name and amount of object(s))
        there is.
        :return: doesn't return anything, only lists the elements in the boxes
        """
        # Counts the sum of all the object(s) in the box
        a = self.__goods.values()
        b = sum(a)
        # If there is nothing in the box, print "...contains 0 items."
        if self.__goods == 0:
            print("Box", '"' + self.box_name() + '"', "contains 0 items.")
        # Otherwise print as told in the task example
        else:
            print("Box", '"' + self.box_name() + '"', "contains", b, "items.")
            for i in sorted(self.__goods):
                if self.__goods[i] >= 99:
                    print(self.__goods[i], i)
                elif self.__goods[i] >= 9:
                    print("", self.__goods[i], i)
                else:
                    print(" ", self.__goods[i], i)

    def remove_item(self, name, count):
        """
        Removes object(s) from the specific box
        :param name: str, name of the object wanted to remove
        :param count: int, number of how many object(s) are going to be removed
        :return: return True or the new amount of object(s) to avoid
        error messages, even though the method worked just fine
        """
        # Convert string (count) to integer number
        count = convert_str_to_int(count)
        # If the object is not in dictionary, do nothing
        if name not in self.__goods:
            return
        # If there are for example 7 objects and you want to remove 7, there's
        # nothing left, so the program must delete the object's name from
        # the dictionary
        if self.__goods[name] == count:
            del self.__goods[name]
            return True

        # If the deleting amount is greater than the amount of the objects,
        # return 0 for error message
        elif self.__goods[name] < count:
            return 0

        # If there are more than one object, remove "count" amount
        else:
            self.__goods[name] -= count
            return self.__goods[name]

    def transfer_item(self, target, name, count):
        """
        Transfer object(s) from one box to another
        :param target: str, name of the target location
        :param name: srt, name of the moving object(s)
        :param count: int, the amount of object(s) will be moved
        :return: return True to avoid error message, even though the method
        worked just fine
        """
        # If the object is not in dictionary at all, return false for error
        if name not in self.__goods:
            return False

        # If the amount you want to transfer is greater than amount of the
        # objects in the dictionary, return false for error
        elif self.__goods[name] < count:
            return False

        # Remove the item from the original location
        self.remove_item(name, count)

        # Add the object to target location
        target.add_item(name, count)

        # Return true for successful transfer
        return True

    def search_item(self, item):
        """
        Search specific item(s) from specific box
        :param item: str, name of the object wanted to search
        :return: return the number of how many objects found in the dictionary
        """
        # If the item is not in the dictionary, do nothing (return False)
        if item not in self.__goods:
            return False

        # If there are zero objects in the dictionary, do nothing
        # (return nothing)
        elif self.__goods[item] == 0:
            return

        # Count how many object(s) there is and return the amount
        else:
            return self.__goods[item]

##### DON'T CHANGE ANYTHING AFTER THIS LINE ##########################


def convert_str_to_int(word):
    """
    Converts the parameter string *word* in to an integer value.
    If conversion is successful returns the resulting integer.
    In the case of an error, returns None.

    :param (str) word: a word supposedly representing an integer value.
    :return: int | NoneType
    """
    try:
        result = int(word)
    except ValueError:
        return None

    return result


# NOTE!
# The following functions have a second parameter whose type is always
# a list containing strings, even in those cases when the list is empty.
# The reason for this is that the command interface
# in the main function was kept very simple: different commands
# require a different number of words of user input. The main function
# just stores all the extra words given after the actual command word in
# the user input line in single list without worrying
# if they are correct or not. This list is then passed as
# a parameter to the actual command functions below. It is their
# job to check that the words in the list makes sense in the context
# of the command in question.


def newbox(all_boxes, list_of_additional_info):
    """
    Creates a new moving box named after the first element in
    the parameter *list_of_additional_info*. The new box is stored
    in the dictionary *all_boxes* using the box's name as the key.
    If *all_boxes* already contains a box with the same name,
    it will be removed and replaced with the new box.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing a single element:
           the name of the moving box (str) to be created.
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of initial data: can't create a new box.")
        return

    box_name = list_of_additional_info[0]
    all_boxes[box_name] = MovingBox(box_name)


def add_to_box(all_boxes, list_of_additional_info):
    """
    Adds a new item into a box stored in the dictionary *all_boxes*.
    If there is no box named by the first element of the list
    *list_of_additional_info*, then an error message is shown.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 3 elements:
           the name of the box (str),
           the name of the item (str), and
           the number of items to be added (str).
    :return: None
    """

    if len(list_of_additional_info) != 3:
        print("Error: wrong number of elements: can't add into a box.")
        return

    box_name, item_name, item_count = list_of_additional_info
    item_count = convert_str_to_int(item_count)

    if item_count is None:
        print("Error: not a number: can't add to a box.")
        return

    if box_name not in all_boxes:
        print("Error: box does not exist: can't add to a box.")
        return

    all_boxes[box_name].add_item(item_name, item_count)


def remove_from_box(all_boxes, list_of_additional_info):
    """
    Removes a given amount of named items from a box stored
    in the dictionary *all_boxes*.
    If there is no box named by the first element of the list
    *list_of_additional_info*, then an error message is displayed.
    If the box exits but doesn't contain the named item,
    then an error message is also displayed.
    If the parameter giving the number of items to be removed
    is larger than what's available in the box, then again
    an error message is displayed.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 3 elements:
           the name of the box (str),
           the name of the item (str), and
           the number of items to be removed (str).
    :return: None
    """

    if len(list_of_additional_info) != 3:
        print("Error: wrong number of elements: can't remove from a box.")
        return

    box_name, item_name, item_count = list_of_additional_info
    item_count = convert_str_to_int(item_count)

    if item_count is None:
        print("Error: not a number: can't remove from a box.")
        return

    if box_name not in all_boxes:
        print("Error: box does not exist: can't remove from a box.")
        return

    if not all_boxes[box_name].remove_item(item_name, item_count):
        print("Error: removing an item from a box failed.")


def transfer_from_box_to_another_box(all_boxes, list_of_additional_info):
    """
    Transfers some amount of named items from one moving box to into another.

    :param all_boxes: all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 4 elements:
           the name of the source box (str),
           the name of the target box (str),
           the name of the item to move (str), and
           the number of items to move (str)
    :return: None
    """

    if len(list_of_additional_info) != 4:
        print("Error: wrong number of elements: can't transfer items.")
        return

    source_name, target_name, item_name, item_count = list_of_additional_info
    item_count = convert_str_to_int(item_count)

    if item_count is None:
        print("Error: not a number: can't transfer items.")
        return

    if source_name not in all_boxes or target_name not in all_boxes:
        print("Error: unknown box name: can't transfer items.")

    if not all_boxes[source_name].transfer_item(all_boxes[target_name], item_name, item_count):
        print("Error: item transfer failed for some reason.")


def list_box_content(all_boxes, list_of_additional_info):
    """
    Displays the contents of a single box in *all_boxes*
    dictionary. If there is no box named by the first element of the list
    *list_of_additional_info*, then an error message is displayed.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 1 element:
           the name of the box (str)
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of elements: can't list contents.")
        return

    box_name = list_of_additional_info[0]

    if box_name not in all_boxes:
        print("Error: box does not exist: can't list content.")
        return

    all_boxes[box_name].list_content()


def list_all_boxes(all_boxes, list_of_additional_info):
    """
    Prints the contents of all boxes on the screen.
    The boxes are printed in an alphabetical order.
    The content of each individual box is printed
    in the same format as it is done in the function
    *list_box_content* above.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: An empty list since this function
           does not require any other data than *all_boxes*.
    :return: None
    """

    if len(list_of_additional_info) != 0:
        print("Error: wrong number of elements: boxes not listed.")
        return

    for box_name in sorted(all_boxes):
        list_box_content(all_boxes, [box_name])


def search_all_boxes(all_boxes, list_of_additional_info):
    """
    Searches a particular item in all of the boxes and
    and prints which boxes contained the item and how
    many of it there was. The boxes in *all_boxes* are
    checked in an alphabetical order. If no items are found,
    the function prints nothing.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing one element (str)
           which is the name of the item the function should search for.
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of elements: can't search boxes.")
        return

    item_name = list_of_additional_info[0]

    for box_name in sorted(all_boxes):
        item_count = all_boxes[box_name].search_item(item_name)

        if item_count > 0:
            print(f"Box {box_name}: {item_count}")


def count_specific_items(all_boxes, list_of_additional_info):
    """
    Counts and prints the number of a particular items
    inside all of the boxes contained in *all_boxes*.
    Zero is printed if there are none.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing one element (str)
           which is the name of the item the function should count.
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of elements: can't count items.")
        return

    item_name = list_of_additional_info[0]

    item_count = 0
    for box in all_boxes.values():
        item_count += box.search_item(item_name)

    print(f"There are total {item_count} {item_name}(s) in the boxes.")


def main():
    """
    In this project *main* function contains the top level
    part of the program's user interface.

    **Do not modify the main function in any way: the automated
    tests rely it to behave in a pre-defined way.**
    """
    boxes = {}

    while True:
        command_line = input("next command> ").strip()
        if command_line == "":
            break

        command_words = command_line.split()
        first_word = command_words[0]
        list_of_other_words = command_words[1:]

        if first_word == "quit":
            break

        elif first_word == "newbox":
            newbox(boxes, list_of_other_words)

        elif first_word == "add":
            add_to_box(boxes, list_of_other_words)

        elif first_word == "remove":
            remove_from_box(boxes, list_of_other_words)

        elif first_word == "transfer":
            transfer_from_box_to_another_box(boxes, list_of_other_words)

        elif first_word == "list":
            list_box_content(boxes, list_of_other_words)

        elif first_word == "list_all":
            list_all_boxes(boxes, list_of_other_words)

        elif first_word == "search":
            search_all_boxes(boxes, list_of_other_words)

        elif first_word == "count":
            count_specific_items(boxes, list_of_other_words)

        else:
            print(f"Error: \"{first_word}\" is not a recognized command!")


if __name__ == "__main__":
    main()
