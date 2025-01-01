from functools import reduce

def equilateral(sides):
    equal_sides = all(side == sides[0] for side in sides[1:])
    return lengths_over_zero(sides) and equal_sides


def isosceles(sides):
    two_equal = sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]
    return lengths_over_zero(sides) and naive_triangle_ineq(sides) and two_equal


def scalene(sides):
    return lengths_over_zero(sides) and naive_triangle_ineq(sides) and not equilateral(sides) and not isosceles(sides)


def check_length(side):
    return side > 0


def custom_and(bool1, bool2):
    return bool1 and bool2


def lengths_over_zero(sides):
    return reduce(custom_and, map(check_length, sides))


# another way would be to generate all permutations
# but some of those are unneccessary because a + b is the same as b + a
def naive_triangle_ineq(sides):
    cond1 = sides[0] + sides[1] >= sides[2]
    cond2 = sides[0] + sides[2] >= sides[1]
    cond3 = sides[1] + sides[2] >= sides[0]
    return reduce(custom_and, [cond1, cond2, cond3])


"""
Checking triangle inequality would have been the same as checking if the sum of the sides > 2 * max(sides).
For each triangle type, I could have just checked the number of unique sides in each.

equilateral is len(set(sides)) == 1
isosceles is len(set(sides)) <= 2
scalene is len(set(sides)) == 1
"""
