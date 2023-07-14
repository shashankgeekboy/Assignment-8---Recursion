def get_min_steps(word1, word2):
  i = j = 0
  count_deletions = 0

  while i < len(word1) and j < len(word2):
    if word1[i] != word2[j]:
      count_deletions += 1
      if word1[i] == word2[j - 1] or word1[i - 1] == word2[j]:
        count_deletions -= 1
      i += 1
      j += 1
    else:
      i += 1
      j += 1

  return count_deletions


def main():
  word1 = "sea"
  word2 = "eat"

  min_steps = get_min_steps(word1, word2)
  print(min_steps)


if __name__ == "__main__":
  main()
