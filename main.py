# Task 17: Import the modules csv, tui and visual
import csv, tui, visual, os

# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.
records = []


def retrieve_entity(data, entity):
    entity_found = False
    for planet in data:
        if entity == planet[0]:
            return planet
        else:
            continue
    if not entity_found:
        print(f"Could not find {entity} \n")
        run()


def file_path():
    path = tui.source_data_path()
    if path:
        if os.path.exists(path):
            with open(path) as csvFile:
                csvdata = csv.reader(csvFile, delimiter=',')
                for row in csvdata:
                    records.append(row)
                csvFile.close()
        else:
            print("Invalid file path or file is missing.")


def planet_and_gravity_categories(option):
    if option == "planets":
        planet_dictionary = {"Planets": [], "Non_planets": []}
        for entity in records[1:]:
            if entity[1] == "FALSE":
                planet_dictionary["Non_planets"].append(entity[0])
            else:
                planet_dictionary["Planets"].append(entity[0])
        planet_dictionary["Planets"] = sorted(planet_dictionary["Planets"], key=lambda x: x[0])
        planet_dictionary["Non_planets"] = sorted(planet_dictionary["Non_planets"], key=lambda x: x[0])
        return planet_dictionary

    elif option == "gravity":
        gravities = tui.gravity_range()
        planet_gravities = {"Lower Limits": [],
                            "Medium Limits": [],
                            "Upper Limits": []}

        for gravity in records[1:]:
            if float(gravity[8]) < gravities[0]:
                planet_gravities["Lower Limits"].append(gravity[0])
            elif gravities[0] < float(gravity[8]) < gravities[1]:
                planet_gravities["Medium Limits"].append(gravity[0])
            else:
                planet_gravities["Upper Limits"].append(gravity[0])

        return planet_gravities

    else:

        orbits = {}

        for entity in set(option):
            if not entity in [y for x in records for y in x]:
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
                        if planet == orbiting[21]:
                            if orbiting[21] != "NA":
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

                elif process_menu == 2:
                    tui.started("Entity details retrieval")
                    entity = tui.entity_details()
                    tui.list_entity(retrieve_entity(records, entity[0]), entity[1])
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
        # TODO: Your code here

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
        # TODO: Your code here

        # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
        # break out of the loop
        elif menu == 5:
            exit("Thank you for using our software")

        # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
        # display an error message


if __name__ == "__main__":
    run()
