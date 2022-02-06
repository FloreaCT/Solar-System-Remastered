import main, os, csv

tui_records = []

def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should consist of the title 'Solar Record Management System' surrounded by dashes.
    The number of dashes before and after the title should be equal to the number of characters in the title 
    i.e. 30 dashes before and after.

    :return: Does not return anything.
    """

    message = "Solar Record Management System"

    print("*" * len(message))
    print(message)
    print("*" * len(message))


def menu():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Load Data', 'Process Data', 'Visualise Data', 'Save Data' and 'Exit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Load Data', 2 for 'Process Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    menu_number = "12345"
    main_menu = input("1. Load Data \n"
                      "2. Process Data \n"
                      "3. Visualise Data \n"
                      "4. Save Data \n"
                      "5. Exit \n")
    if main_menu in menu_number:
        return int(main_menu)
    else:
        error(main_menu)
        return None


def started(operation):
    """
    Task 3: Display a message to indicate that an operation has started.

    The function should display a message in the following format:
    '{operation} has started.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being started
    :return: Does not return anything
    """

    print(operation, "has started. \n")


def completed(operation):
    """
    Task 4: Display a message to indicate that an operation has completed.

    The function should display a message in the following format:
    '{operation} has completed.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being completed
    :return: Does not return anything
    """

    print(operation, "has completed. \n")


def error(error_msg):
    """
    Task 5: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter passed to this function

    :param error_msg: A string containing an error message
    :return: Does not return anything
    """

    print('Error!', error_msg, "is not a valid option.")


def source_data_path():
    """
    Task 6: Retrieve a file path to the source data file.

    The function should prompt the user to enter the file path for a data file (e.g. 'data/sol_data.csv').
    If the file path entered by the user does not end in 'csv' then a suitable error message should be displayed
    and the value None should be returned.
    Otherwise, the file path entered by the user should be returned.

    :return: None if the file path does not end in 'csv' otherwise return the file path entered by the user
    """
    # TODO: Remove the # and the return statement
    # file_path = input("Please enter the file path: \n")
    # if file_path[-4:].lower() != ".csv":
    #     error(file_path)
    #     return None
    # else:
    #     return file_path.lower()
    return "data/sol_data.csv"

def process_type():
    """
    Task 7: Display a menu of options for how the file should be processed. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
        'Categorise entities by gravity', 'Summarise entities by orbit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Retrieve entity', 2 for 'Retrieve entity details' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """

    process_numbers = "123456"
    process_menu = input("1. Retrieve entity \n"
                         "2. Retrieve entity details \n"
                         "3. Categorise entities by type \n"
                         "4. Categorise entities by gravity \n"
                         "5. Summarise entities by orbit \n"
                         "6. Back \n")
    if process_menu in process_numbers:
        return int(process_menu)

    else:
        error(process_menu)
        return None


def entity_name():
    """
    Task 8: Read in the name of an entity and return the name.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should then read in and return the user's response.

    :return: the name of an entity
    """

    return input("Please enter the entity name: \n")


def entity_details():
    """
    Task 9: Read in the name of an entity and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the entity and the list of column
    indexes e.g. ['Earth', [0,1,5,7]]

    :return: A list containing the name of an entity and a list of column indexes
    """

    entity = input("Please enter the name of an entity: \n").capitalize()
    column_indexes = input("Please enter a list of integers for the column indexes (Ex: 0,1,3,6): \n")
    2
    if len(column_indexes) == 0:
        return [entity, []]
    else:
        indexes = [int(index) for index in column_indexes.split(",")]
        return [entity, indexes]


def list_entity(entity, cols=[]):
    """
    Task 10: Display an entity. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the entity will be displayed.

    The entity is a list of values corresponding to particular Solar System space entity
    E.g. ['Earth', TRUE, 9.8].
    The function should only display those values from the entity list that correspond to the column
    indexes provided as part of cols.
    E.g. if cols is [0, 2] then for the entity ['Earth', TRUE, 9.8] the following will be displayed
    ['Earth', 9.8]
    E.g. if cols is an empty list then all the values will be displayed i.e. ['Earth', TRUE, 9.8]

    :param entity: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: does not return anything
    """
    try:
        entity_found = False
        if not cols:
            for planet in tui_records:
                if entity == planet[0]:
                    for number, item in enumerate(tui_records[0]):
                        print('{0:>{1}}'.format(item, len(tui_records[0])), end=" | ")
                        print('{0:<{1}}'.format(planet[number], len(tui_records[0])))
                        entity_found = True
                    break
                else:
                    continue
            if not entity_found:
                print(f"Could not find {entity} \n")
        else:
            for planet in tui_records:
                    if entity == planet[0]:
                        for index in cols:
                            print('{0:>{1}}'.format(tui_records[0][index], len(tui_records[0])), end=" | ")
                            print('{0:<{1}}'.format(planet[index], len(tui_records[0])))
                            entity_found = True
                        break
                    else:
                        continue
            if not entity_found:
                print(f"Could not find {entity} \n")
    except IndexError:
        print(f"Error!!! \nIndex is out of range. The maximum index you can input is {len(tui_records[0])-1}.\n")

def list_entities(entities=[], cols=[]):
    """
    Task 11: Display each entity in entities. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for an entity will be displayed.

    The function should have two parameters as follows:
    entities    which is a list of entities where each entity itself is a list of data values
    cols        this is a list of integer values that represent column indexes.
                the default value for this is an empty list i.e. []

    You will need to add these parameters to the function definition.

    The function should iterate through each entity in entities and display the entity.
    An entity is a list of values e.g. ['Earth', TRUE, 9.8]
    Only the columns whose indexes are included in cols should be displayed for each entity.
    If cols is an empty list then all values for the entity should be displayed.

    :param entities: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here


def list_categories():
    """
    Task 12: Display the contents of the dictionary categories.

    The function should take a single parameter categories which is a dictionary containing category names
    and a list of entities that belong to the category.

    You will need to add the parameter categories to the function definition.

    :param categories: A dictionary containing category names and a list of entities that are part of that category
    :return: Does not return anything
    """
    # TODO: Your code here


def gravity_range():
    """
    Task 13: Ask the user for the lower and upper limits for gravity and return a tuple containing the limits.

    The function should prompt the user to enter the lower and upper limit for a range of values related to gravity.
    The values will be floats e.g. 5.1 for lower limit and 9.8 for upper limit.
    The function should return a tuple containing the lower and upper limits

    :return: a tuple with the lower and upper limits
    """
    # TODO: Your code here


def orbits():
    """
    Task 14: Ask the user for a list of entity names and return the list.

    The function should prompt the user to enter a list of entity names e.g. Jupiter,Earth,Mars
    The list represents the entities that should be orbited.
    The user may enter as many entity names as they desire.
    The function should return a list of the entity names entered by the user.

    :return: a list of entity names
    """
    # TODO: Your code here


def visualise():
    """
    Task 15: Display a menu of options for how the data should be visualised. Return the user's response.

    A menu should be displayed that contains the following options:
        'Entities by type', 'Entities by gravity', 'Summary of orbits', 'Animate gravities'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Entities by type', 2 for 'Entities by gravity' and so on.

    If the user enters an invalid option, then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here


def save():
    """
    Task 16: Display a menu of options for how the data should be saved. Return the user's response.

    A menu should be displayed that contains the following option:
         'Export as JSON'

    The user's response should be read in and returned as an integer corresponding to the selected option.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here


def file_path():
    path = source_data_path()
    if path:
        if os.path.exists(path):
            with open(path) as csvFile:
                csvdata = csv.reader(csvFile, delimiter=',')
                for row in csvdata:
                    main.records.append(row)
                    tui_records.append(row)
                csvFile.close()
        else:
            print("Invalid file path or file is missing.")




def entity_retrieval():

    entity_found = False
    if not entity_details[1]:
        for entity in main.records:
            if entity[0] == entity_name:
                max_length = max(len(i) for i in main.records[0])
                for number, item in enumerate(main.records[0]):
                    print('{0:>{1}}'.format(item, max_length), end=" | ")
                    print('{0:<{1}}'.format(entity[number], max_length))
                    entity_found = True
                break
            else:
                continue
    if not entity_found:
        print(f"Could not find {entity_name} \n")
