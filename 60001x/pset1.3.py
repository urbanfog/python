s = 'azcbobobegghakl'

iter = 0
char = s[iter]
longest = char

while iter <= int(len(s))-2:
  if s[iter] <= s[iter+1]:
    char += s[iter+1]
    if int(len(char)) > int(len(longest)):
      longest = char
  else:
    char = s[iter + 1]
  iter += 1

""" 
for pos, ltr in eitererate(s, start=0):
    if pos <= (len(s) - 2):
      if s[pos] < s[pos + 1]:
        output = output + s[pos]
    all()

   """
print('Longest substring in alphabetical order is:' + str(longest))