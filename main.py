import os
import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

class Solution:
  def __init__(self, filename):
    self.filename = filename
    lines = open(filename, 'r').readlines()

    self.D, self.I, self.S, self.V, self.F = [int(tmp) for tmp in lines[0].strip().split()]

    self.streets = []

    for i in range(1, 1+self.S):
      street = {}
      B, E = [int(tmp) for tmp in lines[i].strip().split()[:2]]
      name = lines[i].split()[2]
      L = int(lines[i].strip().split()[-1])
      street['B'] = B
      street['E'] = E
      street['name'] = name
      street['L'] = L
      self.streets.append(street)
    
    self.cars = []
    for i in range(self.S+1, self.S+self.V+1):
      car = {}
      paths = lines[i].strip().split()[1:]
      car['paths'] = paths

      self.cars.append(car)

    self.intersections = []
    for i in range(self.I):
      self.intersections.append({})

  def baseline(self):
    for street in self.streets:
      if 'incoming' not in self.intersections[street['E']]:
        self.intersections[street['E']]['incoming'] = []

      self.intersections[street['E']]['incoming'].append(street['name'])

    # print(self.intersections)
    f = open(self.filename.replace('.txt', '_out.txt'), 'w+')

    f.write(f'{self.I}\n')
    for index, i in enumerate(self.intersections):
      f.write(f'{index}\n')
      f.write(f'{len(i["incoming"])}\n')
      for strt in i['incoming']:
        f.write(f'{strt} 1\n')

    f.close()

  def d_solution(self):
    """
    stre format:
    a -> b
    b -> a
    all streets have 2 dir, same length
    """
    pass

  def e_sol(self):
    """
    street format:
    i -> i + 1
    i + 1 -> 499
    i+1 -> i+2
    499 -> i+2
    """

    for street in self.streets:
      if 'incoming' not in self.intersections[street['E']]:
        self.intersections[street['E']]['incoming'] = []

      self.intersections[street['E']]['incoming'].append(street['name'])

    # print(self.intersections)
    f = open(self.filename.replace('.txt', '_out.txt'), 'w+')

    f.write(f'{self.I}\n')
    for index, i in enumerate(self.intersections):
      if index == 499:
        break
      f.write(f'{index}\n')
      f.write(f'{len(i["incoming"])}\n')
      for strt in i['incoming']:
        if 'ejj' in strt:
          f.write(f'{strt} 1\n')
        else:
          f.write(f'{strt} 10\n')
    
    count_path = {}
    scheduled = []
    for car in self.cars:
      for index, path in enumerate(car['paths']):
        if path.endswith('ejj'):
          if path not in count_path:
            count_path[path] = 0
          count_path[path] += 1

    scheduled_count = 0
    print(len(count_path))
    f.write('499\n')
    f.write(f'{len(count_path)}\n')

    count = [(k, v) for k, v in count_path.items()]
    count = sorted(count, key=lambda x:-x[-1])
    for k, v in count:
      print(k,v)
      f.write(f"{k} {1}\n")

    f.close()

  def e_sol2(self):
    """
    street format:
    i -> i + 1
    i + 1 -> 499
    i+1 -> i+2
    499 -> i+2
    """

    for street in self.streets:
      if 'incoming' not in self.intersections[street['E']]:
        self.intersections[street['E']]['incoming'] = []

      self.intersections[street['E']]['incoming'].append(street['name'])

    # print(self.intersections)
    f = open(self.filename.replace('.txt', '_out.txt'), 'w+')

    f.write(f'{self.I}\n')
    for index, i in enumerate(self.intersections):
      if index == 499:
        break
      f.write(f'{index}\n')
      f.write(f'{len(i["incoming"])}\n')
      for strt in i['incoming']:
        f.write(f'{strt} 1\n')
    
    count_path = []
    for car in self.cars:
      count = {}
      for index, path in enumerate(car['paths']):
        if path.endswith['ejj']:
          if path not in count:
            count_path = []
    pass


    f.close()


    # for street in self.streets:
    #   if 'incoming' not in self.intersections[street['E']]:
    #     self.intersections[street['E']]['incoming'] = []

    #   self.intersections[street['E']]['incoming'].append(street['name'])

    # # print(self.intersections)
    # f = open(self.filename.replace('.txt', '_out.txt'), 'w+')

    # f.write(f'{self.I}\n')
    # for index, i in enumerate(self.intersections):
    #   f.write(f'{index}\n')
    #   f.write(f'{len(i["incoming"])}\n')
    #   for strt in i['incoming']:
    #     f.write(f'{strt} 1\n')

    # f.close()
    
  def hoangalgo(self):
    for street in self.streets:
      if 'incoming' not in self.intersections[street['E']]:
        self.intersections[street['E']]['incoming'] = []

      self.intersections[street['E']]['incoming'].append(street['name'])

    self.schedules = []
    # print(self.intersections)
    f = open(self.filename.replace('.txt', '_out.txt'), 'w+')

    f.write(f'{self.I}\n')
    for index, i in enumerate(self.intersections):
      f.write(f'{index}\n')
      f.write(f'{len(i["incoming"])}\n')
      for strt in i['incoming']:
        f.write(f'{strt} i['']\n')

    f.close
    pass
    
  def to_submission(self):
    pass
  
if __name__ == "__main__":
  # from tqdm import tqdm
  # for fn in ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']:
  #   if fn.endswith('.txt'):
  #     sol = Solution(fn)
  #     sol.baseline()
  sol = Solution('e.txt')
  sol.e_sol()
  
  