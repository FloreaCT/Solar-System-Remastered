# Task 17: Import the modules csv, tui and visual
import csv, tui, visual, os, sys, json
from abc import ABC, abstractmethod

# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.
records = []


class Abstract(ABC):
    """
    A abstract class just to demonstrate the concept of OOP.
    """
    @abstractmethod
    def save(self, option):
        pass


class Save(Abstract):
    """
    A class that inherits from Abstract class.
    """
    def save(self, option):
        data_arrangement = planet_and_gravity_categories("planets")
        with open(option + ".json", "w", encoding="utf-8") as f:
            json.dump(data_arrangement, f, ensure_ascii=False, indent=4)


def retrieve_entity(data, entity):
    """
    A function that takes a dictionary and searches the planet within that dictionary.

    :param data: A dictionary containing a data of all entities.
    :param entity: An entity to be searched within the dictionary.
    :return: If an entity is found, return a list with all the data about that entity.
    """

    entity_found = False
    for planet in data:
        if entity == planet[0]:  # Checking if the entity is matching the entity name in the dictionary
            return planet
        else:
            continue
    if not entity_found:
        print(f"Could not find {entity} \n")
        run()


def file_path():
    """
    A function that checks for a .csv file within a file path. If the file exists, all the data from the file will be
    appended to the variable records. Otherwise an error will be printed

    :return: Does not return anything
    """
    path = tui.source_data_path()
    if path:
        if os.path.exists(path):
            with open(path) as csvFile:
                csvdata = csv.reader(csvFile, delimiter=',')
                for row in csvdata:
                    records.append(row)
        else:
            print("Invalid file path or file is missing.")


def entity():
    entities = [planet.capitalize() for planet in
                input("Please enter one or more entities. ex: Earth,Moon,Saturn \n").split(",")]
    indexes = [int(index) for index in input("Please enter the indexes you would like to see. ex: 1,2,3\n").split(',')
               if index.isnumeric()]
    planets = []
    for entity in entities:
        planet = retrieve_entity(records, entity)
        if not planet:
            continue
        else:
            planets.append(planet)

    return planets, indexes

def planet_and_gravity_categories(option):
    """
    A multi function that does 3 things based on the option parameter.

    1. If the parameter "planets" is given, the function will create a dictionary which will consist of 2 key value pairs.
    One for Planets and a list of planets and one for Non Planets and a list of Non Planets

    2. If the parameter "gravity" is given, the function will create a dictionary which will consist of 3 key value pairs.

    3. If any other parameter is given, the function will create a dictionary which will consist of 3 key value pairs.

    :param option: A string
    :return: Returns a dictionary based on the option selected
    """

    if option == "planets":
        planet_dictionary = {"Planets": [], "Non_planets": []}
        for entity in records[1:]:  # Checking if the entity is a planet or not
            if entity[1] == "FALSE":
                planet_dictionary["Non_planets"].append(entity[0])
            else:
                planet_dictionary["Planets"].append(entity[0])

        planet_dictionary["Planets"] = sorted(planet_dictionary["Planets"], key=lambda x: x[0])
        planet_dictionary["Non_planets"] = sorted(planet_dictionary["Non_planets"], key=lambda x: x[0])

        return planet_dictionary

    elif option == "gravity":
        gravities = tui.gravity_range()  # A variable consisting of lower and upper limits
        planet_gravities = {"Lower Limits": [],
                            "Medium Limits": [],
                            "Upper Limits": []}

        for gravity in records[1:]:
            if float(gravity[8]) < gravities[0]:  # Checking if the entity's gravity is lower then the lower limit
                planet_gravities["Lower Limits"].append(gravity[0])
            elif gravities[0] < float(gravity[8]) < gravities[1]:  # Checking if the entity's gravity is between the limits
                planet_gravities["Medium Limits"].append(gravity[0])
            else:
                planet_gravities["Upper Limits"].append(gravity[0])

        return planet_gravities

    else:

        orbits = {}

        for entity in set(option):
            if not entity in [y for x in records for y in x]:  # Using a list comprehension to check if the entity is in records dictionary
                option.remove(entity)
                print(f"\nCould not find {entity}.\n")

        for planet in option:
            for entity in records[1:]:
                if planet != entity[21]:
                    continue
                else:
                    small = []
                    large = []
                    for orbiting in records[1:]:
                        if planet == orbiting[21]:  # Looking for the requested orbited planet
                            if orbiting[21] != "NA":  # Excluding non orbited planets
                                if float(orbiting[10]) < 100:
                                    small.append(orbiting[0])
                                else:
                                    large.append(orbiting[0])

                            else:
                                continue
                    if not small:
                        orbits[planet] = {"large": large}
                    elif not large:
                        orbits[planet] = {"small": small}
                    else:
                        orbits[planet] = {"small": small, "large": large}

    return orbits


def run():
    try:
        # Task 19: Call the function welcome of the module tui.
        # This will display our welcome message when the program is executed.
        tui.welcome()

        while True:
            # Task 20: Using the appropriate function in the module tui, display a menu of options
            # for the different operations that can be performed on the data.
            # Assign the selected option to a suitable local variable
            menu = tui.menu()

            # Task 21: Check if the user selected the option for loading data.  If so, then do the following:
            # - Use the appropriate function in the module tui to display a message to indicate that the data loading
            # operation has started.
            # - Load the data (see below).
            # - Use the appropriate function in the module tui to display a message to indicate that the data loading
            # operation has completed.
            #
            # To load the data, it is recommended that you create and call one or more separate functions that do the
            # following:
            # - Use the appropriate function in the module tui to retrieve a file path for the CSV data file.  You
            # should appropriately handle the case where this is None.
            # - Read each line from the CSV file and add it to the list 'records'. You should appropriately handle the case
            # where the file cannot be found
            if menu == 1:
                tui.started("Data loading")
                file_path()
                tui.completed("Data loading")
            # Task 22: Check if the user selected the option for processing data.  If so, then do the following:
            # - Use the appropriate function in the module tui to display a message to indicate that the data processing
            # operation has started.
            # - Process the data (see below).
            # - Use the appropriate function in the module tui to display a message to indicate that the data processing
            # operation has completed.
            #
            # To process the data, it is recommended that you create and call one or more separate functions that do the
            # following:
            # - Use the appropriate function in the module tui to display a menu of options for processing the data.
            # - Check what option has been selected
            #
            #   - If the user selected the option to retrieve an entity then
            #       - Use the appropriate function in the module tui to indicate that the entity retrieval process
            #       has started.
            #       - Use the appropriate function in the module tui to retrieve the entity name
            #       - Find the record for the specified entity in records.  You should appropriately handle the case
            #       where the entity cannot be found.
            #       - Use the appropriate function in the module tui to list the entity
            #       - Use the appropriate function in the module tui to indicate that the entity retrieval process has
            #       completed.
            #
            #   - If the user selected the option to retrieve an entity's details then
            #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
            #       process has started.
            #       - Use the appropriate function in the module tui to retrieve the entity details
            #       - Find the record for the specified entity details in records.  You should appropriately handle the
            #       case where the entity cannot be found.
            #       - Use the appropriate function in the module tui to list the entity
            #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
            #       process has completed.
            #
            #   - If the user selected the option to categorise entities by their type then
            #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
            #       process has started.
            #       - Iterate through each record in records and assemble a dictionary containing a list of planets
            #       and a list of non-planets.
            #       - Use the appropriate function in the module tui to list the categories.
            #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
            #       process has completed.
            #
            #   - If the user selected the option to categorise entities by their gravity then
            #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
            #       process has started.
            #       - Use the appropriate function in the module tui to retrieve a gravity range
            #       - Iterate through each record in records and assemble a dictionary containing lists of entities
            #       grouped into low (below lower limit), medium and high (above upper limit) gravity categories.
            #       - Use the appropriate function in the module tui to list the categories.
            #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
            #       process has completed.
            #
            #   - If the user selected the option to generate an orbit summary then
            #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
            #       started.
            #       - Use the appropriate function in the module tui to retrieve a list of orbited planets.
            #       - Iterate through each record in records and find entities that orbit a planet in the list of
            #       orbited planets.  Assemble the found entities into a nested dictionary such that each entity can be
            #       accessed as follows:
            #           name_of_dict[planet_orbited][category]
            #       where category is "small" if the mean radius of the entity is below 100 and "large" otherwise.
            #       - Use the appropriate function in the module tui to list the categories.
            #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
            #       completed.
            elif menu == 2:
                if not records:
                    print("Error! You must load the data first")
                    continue
                else:
                    tui.started("Data processing operation")
                    process_menu = tui.process_type()

                    if process_menu == 1:
                        tui.started("Entity retrieval process")
                        tui.list_entity(retrieve_entity(records, tui.entity_name()))
                        tui.completed("Entity retrieval process")

                    # elif process_menu == 2:
                    #     tui.started("Entity details retrieval")
                    #     entity = tui.entity_details()
                    #     tui.list_entity(retrieve_entity(records, entity[0]), entity[1])
                    #     tui.completed("Entity details retrieval")

                    elif process_menu == 2:
                        tui.started("Entity details retrieval")
                        entity_det = entity()
                        tui.list_entities(entity_det[0], entity_det[1])
                        tui.completed("Entity details retrieval")

                    elif process_menu == 3:
                        tui.started("Entity type categorisation process")
                        tui.list_categories(planet_and_gravity_categories("planets"))
                        tui.completed("Entity type categorisation process")

                    elif process_menu == 4:
                        tui.started("Categorisation by entity gravity process")
                        tui.list_categories(planet_and_gravity_categories("gravity"))
                        tui.completed("Categorisation by entity gravity process")

                    elif process_menu == 5:
                        tui.started("Orbit summary process")
                        tui.list_categories(planet_and_gravity_categories(tui.orbits()))
                        tui.completed("Orbit summary process")

                    tui.completed("Data processing operation")
            # Task 23: Check if the user selected the option for visualising data.  If so, then do the following:
            # - Use the appropriate function in the module tui to indicate that the data visualisation operation
            # has started.
            # - Visualise the data (see below).
            # - Use the appropriate function in the module tui to display a message to indicate that the data visualisation
            # operation has completed.
            #
            # To visualise the data, it is recommended that you create and call one or more separate functions that do the
            # following:
            # - Use the appropriate function in the module tui to retrieve the type of visualisation to display.
            # - Check what option has been selected
            #
            #   - if the user selected the option to visualise the entity type then
            #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
            #       process has started.
            #       - Use your code from earlier to assemble a dictionary containing a list of planets and a list of
            #       non-planets.
            #       - Use the appropriate function in the module visual to display a pie chart for the number of planets
            #       and non-planets
            #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
            #       process has completed.
            #
            #   - if the user selected the option to visualise the entity gravity then
            #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
            #       process has started.
            #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
            #       low (below lower limit), medium and high (above upper limit) gravity categories.
            #       - Use the appropriate function in the module visual to display a bar chart for the gravities
            #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
            #       process has completed.
            #
            #   - if the user selected the option to visualise the orbit summary then
            #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
            #       process has started.
            #       - Use your code from earlier to assemble a nested dictionary of orbiting planets.
            #       - Use the appropriate function in the module visual to display subplots for the orbits
            #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
            #       process has completed.
            #
            #   - if the user selected the option to animate the planet gravities then
            #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
            #       process has started.
            #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
            #       low (below lower limit), medium and high (above upper limit) gravity categories.
            #       - Use the appropriate function in the module visual to animate the gravity.
            #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
            #       process has completed.

            elif menu == 3:
                tui.started("Data visualisation operation")
                visualise_menu = tui.visualise()
                if visualise_menu == 1:
                    tui.started("Entity type visualisation process")
                    visual.entities_pie(planet_and_gravity_categories("planets"))
                    tui.completed("Entity type visualisation process")

                if visualise_menu == 2:
                    tui.started("Entity by gravity process")
                    visual.entities_bar(planet_and_gravity_categories("gravity"))
                    tui.completed("Entity by gravity process")

                if visualise_menu == 3:
                    tui.started("Orbit summary visualisation process")
                    visual.orbits(planet_and_gravity_categories(planet_and_gravity_categories("planets")["Planets"]))
                    tui.completed("Orbit summary visualisation process")

                if visualise_menu == 4:
                    tui.started("Gravity animation visualisation process")
                    visual.gravity_animation(planet_and_gravity_categories("gravity"))
                    tui.completed("Gravity animation visualisation process")
                if visualise_menu == 5:
                    menu
                tui.completed("Data visualisation operation")


            # Task 28: Check if the user selected the option for saving data.  If so, then do the following:
            # - Use the appropriate function in the module tui to indicate that the save data operation has started.
            # - Save the data (see below)
            # - Use the appropriate function in the module tui to indicate that the save data operation has completed.
            #
            # To save the data, you should demonstrate the application of OOP principles including the concepts of
            # abstraction and inheritance.  You should create an AbstractWriter class with abstract methods and a concrete
            # Writer class that inherits from the AbstractWriter class.  You should then use this to write the records to
            # a JSON file using in the following order: all the planets in alphabetical order followed by non-planets
            # in alphabetical order.
            elif menu == 4:
                tui.started("Save data operation")
                save_menu = tui.save()
                if save_menu == 1:
                    data_saving = Save()
                    data_saving.save(input("Please choose the file name: \n"))
                else:
                    print("Invalid selection")
                tui.completed("Save data operation")

            # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
            # break out of the loop
            elif menu == 5:
                exit("Thank you for using our software")

            # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
            # display an error message
    except ValueError:
        error = str(sys.exc_info()[1]).split()
        tui.error(error[-1])
        run()


if __name__ == "__main__":
    run()
