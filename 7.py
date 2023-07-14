def decode_string(s):
  stack = []
  decoded_string = ""

  for c in s:
    if c == "]":
      current_string = ""
      while stack and stack[-1] != "[":
        current_string += stack.pop()
      stack.pop()
      decoded_string += current_string * int(stack.pop())
    else:
      stack.append(c)

  while stack:
    decoded_string += stack.pop()

  return decoded_string


def main():
  s = "3[a]2[bc]"

  decoded_string = decode_string(s)
  print(decoded_string)


if __name__ == "__main__":
  main()
