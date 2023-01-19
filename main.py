""" Created by: Leo Martinez III in Spring 2022 """

from positional_list import PositionalList
from array_stack import ArrayStack

L = PositionalList()
S = ArrayStack()
Helper = ArrayStack() # Used to dump duplicates into

#L = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27] created in line 17
S.push(28)
S.push(24)
S.push(20)
S.push(16)
S.push(12)
S.push(8)
S.push(4)

for i in range(10):
  L.add_last(3*i)

checker = L.first()

for a in range(len(S)):
  newe = S.pop()
  while(checker.element()<newe and checker != L.last()):
    checker = L.after(checker)
  if checker.element()>newe:
    L.add_before(checker, newe)
  elif checker.element()<newe:
    L.add_after(checker, newe)

for e in L: # Display the newly numerically organized list
  print(e)

"""Running time of the program: O(n), the function is linear."""
