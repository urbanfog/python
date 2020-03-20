s = 'azcbobobegghakl'
bob_count = 0
x = 0

for ltr in s:
  sub_str = s[x:x+3]
  if 'bob' in sub_str:
    bob_count += 1
  x += 1
print(bob_count)
