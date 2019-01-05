# Create a set of randomly generated unique elements and from
# this set create a valid subset with equal (fair) probability that
# any element of the set 's' will be added to a subset '(r)eservoir'

import random
import sys

def reservoir_sample(constraint=random.randint(1, 10) , s=[i for i in range(random.randint(10,20))]):
  if (len(s) > constraint):
    reservoir = s[:constraint]
    setTail = s[len(reservoir):]
    for i in range(len(setTail)):
      fairChoice = random.randint(0, len(reservoir) + i)
      if fairChoice < len(reservoir):
        reservoir[fairChoice] = setTail[i]
    return reservoir
  else:
    print("The length of the provided set must be greater than the contraint")
    print("Constraint: %s" % constraint)
    print("Set: %s" % s)

s = [i for i in range(0, 10)]
c = 4
print("Set: {0}".format(s))
rs = reservoir_sample(c, s)
print(rs)
