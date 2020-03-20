s = 'azcbobobegghakl'
vowels = 0

for ltr in s:
  if ltr == 'a' or ltr == 'e' or ltr =='i' or ltr == 'o' or ltr == 'u':
    vowels += 1

print('Number of vowels: ' +str(vowels))