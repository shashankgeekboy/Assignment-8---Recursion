def get_min_ascii_sum(s1, s2):
  i = j = 0
  sum = 0

  while i < len(s1) and j < len(s2):
    if s1[i] != s2[j]:
      sum += ord(s1[i])
      i += 1
    else:
      i += 1
      j += 1

  while i < len(s1):
    sum += ord(s1[i])
    i += 1

  while j < len(s2):
    sum += ord(s2[j])
    j += 1

  return sum


def main():
  s1 = "sea"
  s2 = "eat"

  min_ascii_sum = get_min_ascii_sum(s1, s2)
  print(min_ascii_sum)


if __name__ == "__main__":
  main()
