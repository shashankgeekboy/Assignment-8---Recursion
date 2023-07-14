def build_tree(s):
  stack = []
  for c in s:
    if c == '(':
      stack.append([])
    elif c == ')':
      left = stack.pop()
      right = stack.pop()
      node = [int(c), left, right]
      stack.append(node)
    else:
      node = [int(c)]
      stack.append(node)

  return stack[0]


def main():
  s = "4(2(3)(1))(6(5))"

  root = build_tree(s)
  print(root)


if __name__ == "__main__":
  main()
