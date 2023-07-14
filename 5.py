def compress_chars(chars):
  i = 0
  count = 1
  for j in range(1, len(chars)):
    if chars[j] == chars[i]:
      count += 1
    else:
      if count == 1:
        chars[i] = chars[j]
      else:
        chars[i] = chars[j]
        chars[i + 1] = str(count)
        i += 2
      count = 1

  if count == 1:
    chars[i] = chars[-1]
  else:
    chars[i] = chars[-1]
    chars[i + 1] = str(count)
    i += 2

  return i


def main():
  chars = ["a", "a", "b", "b", "c", "c", "c"]

  new_len = compress_chars(chars)
  print(chars[:new_len])


if __name__ == "__main__":
  main()
