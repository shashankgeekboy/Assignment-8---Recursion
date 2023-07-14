def find_anagrams(s, p):
  anagrams = []
  window = {}
  for i in range(len(s)):
    char = s[i]
    if char in window:
      window[char] -= 1
    else:
      window[char] = 0

    if len(window) == len(p):
      anagrams.append(i - len(p) + 1)

    char = p[i - len(p) + 1]
    if char in window:
      window[char] += 1
    else:
      window[char] = 0

  return anagrams


def main():
  s = "cbaebabacd"
  p = "abc"

  anagrams = find_anagrams(s, p)
  print(anagrams)


if __name__ == "__main__":
  main()
