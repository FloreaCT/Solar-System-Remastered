import matplotlib.pyplot as plt
import matplotlib.animation as animation


def entities_pie(categories):
    """
    Task 24: Display a single subplot that shows a pie chart for categories.

    The function should display a pie chart with the number of planets and the number of non-planets from categories.

    :param categories: A dictionary with planets and non-planets
    :return: Does not return anything
    """

    labels = [label for label in categories.keys()]
    sizes = [len(size) for size in categories.values()]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')
    plt.title("Number of planets and non planets")

    plt.show()


def entities_bar(categories):
    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """

    labels = [label for label in categories.keys()]
    sizes = [len(size) for size in categories.values()]

    plt.barh(labels, sizes)
    plt.xlabel("Number of entities")
    plt.title("Entities categorised by gravity")

    for index, value in enumerate(sizes):
        plt.text(value, index, str(value))

    plt.gcf().set_size_inches(10, 10)
    plt.show()


def orbits(summary):
    """
    Task 26: Display subplots where each subplot shows the "small" and "large" entities that orbit the planet.

    Summary is a nested dictionary of the form:
    summary = {
        "orbited planet": {
            "small": [entity, entity, entity],
            "large": [entity, entity]
        }
    }

    The function should display for each orbited planet in summary. Each subplot should show a bar chart with the
    number of "small" and "large" orbiting entities.

    :param summary: A dictionary containing the "small" and "large" entities for each orbited planet.
    :return: Does not return anything
    """
    labels = [label for label in summary.keys()]
    small = []
    large = []

    for key, value in summary.items():
        if 'large' in value:
            small.append(len(summary[key]['small']))
            large.append(len(summary[key]['large']))
        else:
            small.append(len(summary[key]['small']))
            large.append(0)

    fig, axs = plt.subplots(1, len(labels))
    fig.suptitle('The number and size of entities orbiting each planet: ')

    # Using the number of the planets as a range
    for i in range(len(labels)):
        x1 = 2
        y1 = small[i]
        x2 = 4
        y2 = large[i]
        plt.subplot(int(len(labels)/2), int(len(labels)/3), i + 1)  # At first iteration i will be 0 and creating a subplot 2,3,0 is not valid.
        plt.bar(x1, y1, color='orange')
        plt.bar(x2, y2, color='blue')
        plt.title(labels[i])  # Setting the name of the planet for each subplot
        plt.legend(['Small', 'Large'])

        # Checking if we have 0 planets orbiting, in order to not display 0
        if y1 == 0:
            plt.text(x1, y1, str(y1), color='white', ha='center')  # Setting white so 0 wont be visible
            plt.text(x2, y2 + 0.5, str(y2), color='black', ha='center')
        elif y2 == 0:
            plt.text(x1, y1 / 2, str(y1), color='black', ha='center')
            plt.text(x2, y2 + 0.5, str(y2), color='white', va='center')  # Setting white so 0 wont be visible
        else:
            plt.text(x1, y1 / 2, str(y1), color='black', ha='center')
            plt.text(x2, y2 + 0.5, str(y2), color='black', ha='center')

    plt.tight_layout()
    mng = plt.get_current_fig_manager()  # This is the figure manager
    mng.window.state('zoomed')  # and we use this to open the figure in full screen
    plt.show()



def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """


    fig = plt.figure()
    max_height = max(len(categories["Lower Limits"]),len(categories["Medium Limits"]), len(categories["Upper Limits"]))

    ax = plt.axes(xlim=(-1, 3), ylim=(0, max_height))

    rectangles = plt.bar(["Lower Limits \n" + str(len(categories["Lower Limits"])),"Medium Limits \n" + str(len(categories["Medium Limits"])),"Upper Limits \n" + str(len(categories["Upper Limits"]))],[len(categories["Lower Limits"]),len(categories["Medium Limits"]), len(categories["Upper Limits"])],width=0.1) #rectangles to animate

    patches = list(rectangles) #things to animate

    def init():
        #init rectangles
        for rectangle in rectangles:
            rectangle.set_height(0)

        return patches #return everything that must be updated

    def animate(i):
        #animate rectangles
        for j,rectangle in enumerate(rectangles):
            rectangle.set_height(i/(j+1))

        return patches #return everything that must be updated

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=max_height, interval=10, blit=True)

    plt.show()
