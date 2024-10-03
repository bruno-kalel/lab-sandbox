def f(num):
  if num == 1 or num == 2:
    return 1
  return f(num - 1) + f(num - 2)


print(f(3))
