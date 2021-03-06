from collections import namedtuple


tape = []

Rule = namedtuple("Rule", ["q0", "s", "t_n", "q1"])
rule1 = Rule(0, 1, "R", 0)
rule2 = Rule(0, 0, 1, 1)
rule3 = Rule(1, 1, "R", 1)
rule4 = Rule(1, 0, "L", 2)
rule5 = Rule(2, 1, 0, 3)

rules = [rule1, rule2, rule3, rule4, rule5]


def add(x,y, max=10):
  tape = [1 for _ in range(x)] + [0] + [1 for _ in range(y)] + [0 for _ in range(max)]
  print(tape)
  state = 0
  pointer = 0
  halted = False
  while True:
    s = tape[pointer]

    halted = True
    for i, rule in enumerate(rules):
      if rule.q0 == state and rule.s == s:
        halted = False
        print(f"rule : {i+1}, q0 : {state}, s : {s}, t_n : {rule.t_n}, q1 : {rule.q1}, pointer : {pointer}")
        if rule.t_n == "R":
          pointer += 1
        elif rule.t_n == "L":
          pointer -= 1
        else:
          tape[pointer] = rule.t_n

        state = rule.q1
        break

    if halted == True:
      print(tape)
      break


add(5, 11, max=20)


