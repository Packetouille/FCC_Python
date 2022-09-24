import prob_calculator
import copy

hat = prob_calculator.Hat(red=5,blue=2)
print(f"hat.contents before: = {hat.contents}")
actual = hat.draw(2)
print(f"hat.contents after: = {hat.contents}")
expected = ['blue', 'red']
print(f"\nactual = {actual}, expected = {expected}")

print()

'''
hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"yellow": 2,
                    "blue":3,
                    "test":1
                    },
    num_balls_drawn=20,
    num_experiments=100)
print("Probability:", probability)

print(hat.contents)


hat = prob_calculator.Hat(blue=3,red=2,green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue":2,
                    "green":1
                    },
    num_balls_drawn=4,
    num_experiments=1000)
print("Probability:", probability)
'''
