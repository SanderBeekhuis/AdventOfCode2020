import functools

class LoopException(Exception): 
  pass

def run(file: str='input.txt'):
  lines = open(file, 'r').readlines()
  lines = map(lambda l: l.strip(), lines)
  lines = list(lines)

  try:
    run_program(lines)
  except LoopException as e: 
    print("Part 1", e)

  for index in range(len(lines)):
    # copy program and edit line at `index`
    program_copy = list(lines)
    cmd = program_copy[index][:3]
    if cmd == 'jmp':
      program_copy[index] = 'nop' + program_copy[index][3:]
    elif cmd == 'nop':
      program_copy[index] = 'jmp' + program_copy[index][3:]
    else:
      continue

    try: 
      result = run_program(program_copy)
      print('Part 2', result)
      break
    except LoopException:
      continue


def run_program(lines):
  visited = set()
  index = 0
  accumaltor = 0

  while index != len(lines):
    if index in visited:
      raise LoopException(accumaltor)
    visited.add(index)

    cmd, arg = lines[index].split(' ')
    if cmd == 'acc':
      accumaltor += int(arg)
      index += 1
    elif cmd == 'jmp': 
      index += int(arg)
    elif cmd == 'nop':
      index += 1
    else:
      assert False, "Unexpected command"

  return accumaltor

if __name__ == "__main__":
  run()