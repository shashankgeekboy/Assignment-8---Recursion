def is_valid(s):
  count_left = 0
  count_right = 0

  for c in s:
    if c == '(':
      count_left += 1
    elif c == ')':
      count_right += 1
    elif c == '*':
      if count_right > count_left:
        return False
      else:
        count_right = max(0, count_right - 1)

  return count_left == count_right


def main():
  s = "()"

  is_valid = is_valid(s)
  print(is_valid)


if __name__ == "__main__":
  main()
