# your code goes here

def solve(s):
  i = 0
  j = len(s) -1

  res = ""
  append = ""
  while i < j:
    if s[i] != s[j]:
      append = s[i] + append
      res += s[i]
      i += 1
    else:
      append = s[i] + append
      res += s[i]
      i += 1
      j -= 1

  if len(s) % 2 == 0:
    res += append
  else:
    res += s[i] + append
  return res

def main():
  s = input()
  res = solve(s)
  print(res)

if __name__ == "__main__":
  main()
