# Create a set of randomly generated unique elements and from
# this set create a valid subset with equal (fair) probability that
# any element of the set 's' will be added to a subset '(r)eservoir'

import random
from argparse import ArgumentParser

def reservoir_sample(constraint=random.randint(1, 9) , s=[i for i in range(random.randint(10,20))]):
  if (len(s) > constraint):
    reservoir = s[:constraint]
    reservoir_length = len(reservoir)
    set_tail = s[reservoir_length:]
    set_tail_length = len(set_tail)
    
    for i in range(set_tail_length):
      fair_choice = random.randint(0, reservoir_length + i)
      if fair_choice < reservoir_length:
        reservoir[fair_choice] = set_tail[i]
    
    print("Set: {0}".format(s))
    return reservoir
  else:
    print("The length of the provided set must be greater than the contraint")
    print("Constraint: %s" % constraint)
    print("Set: %s" % s)

def parse_args():
  parser = ArgumentParser()
  parser.add_argument("-c", "--constraint", dest="constraint")
  parser.add_argument("-s", "--set", dest="sample_set")
  args = parser.parse_args()

  if args.constraint:
    try:
      args.constraint = int(args.constraint)
    except:
      print("Constraint must be an integer")
  if args.sample_set:
    args.sample_set = [i for i in set(args.sample_set.split(","))]
  
  return args

args = parse_args()

if args.constraint and args.sample_set:
  print(reservoir_sample(args.constraint, args.sample_set))

elif args.constraint and not args.sample_set:
  print(reservoir_sample(constraint=args.constraint))

elif not args.constraint and args.sample_set:
  print(reservoir_sample(s=args.sample_set))

else:
  print(reservoir_sample())
