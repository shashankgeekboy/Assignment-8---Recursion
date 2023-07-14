def can_swap(s, goal):
  char_counts = {}
  for c in s:
    if c in char_counts:
      char_counts[c] += 1
    else:
      char_counts[c] = 1

  for c in goal:
    if c not in char_counts or char_counts[c] == 0:
      return False
    char_counts[c] -= 1

  return True


def main():
  s = "ab"
  goal = "ba"

  can_swap = can_swap(s, goal)
  print(can_swap)


if __name__ == "__main__":
  main()
