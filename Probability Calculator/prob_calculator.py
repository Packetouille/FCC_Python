import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
    # Constructor: accepts a set of color:number pairs. The loops within
    # append a str(color) to the instance variable list self.contents
        self.contents = []
        for color,number in kwargs.items():     # Traversing through kwargs
            while number > 0:                   # Appends each color to contents
                self.contents.append(color)
                number -= 1

    def draw(self, draw_num):
    # Method returns list of items randomly drawn from self.contents based on a
    # passed number. As items are drawn they are popped from the list before
    # drawing again. length of list is adjusted as balls are popped.
        if draw_num > len(self.contents):
            return self.contents

        draw_list = []
        while draw_num > 0:                     # Builds a random draw_list of balls
            selection = random.randint(0, len(self.contents) - 1)
            draw_list.append(self.contents[selection])
            self.contents.pop(selection)
            draw_num -= 1

        return draw_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
# This function runs an experiment to calculate the probability of drawing a specified
# combo from a specified number of balls. The function receives an object, the expected
# combination, a number of balls to draw, and the total number of experiments to perform
# The object.draw() method is called to handle the drawing of the balls.

    occurrences = 0                                 # Var tracks # of times expected_balls is met
    exp_count = num_experiments                     # num_experiments will be needed at the end
    while exp_count > 0:                            # Loop through num_experiments times
        new_hat = copy.deepcopy(hat)                # Copy hat at sart of each exp_count
        draw_list = new_hat.draw(num_balls_drawn)   # Draw specified number of balls
        check = 0                                   # Flag variable
        for color, num in expected_balls.items():   # Traversing and comparing expected_balls dict
            matches_found = draw_list.count(color)  # Track the times the current ball exists
            if matches_found >= num:                # If exists >= expected times: flag var + 1
                check += 1
        if check == len(expected_balls):            # If all expected_balls were found: occurrences + 1
            occurrences += 1
        exp_count -= 1                              # decrement counter

    return occurrences/num_experiments              # Calculate and return probability
