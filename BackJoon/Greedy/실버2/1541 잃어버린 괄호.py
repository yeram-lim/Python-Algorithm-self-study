content = input()

content_list = []
num = ''
for letter in content:
  if letter.isdigit():
    num += letter
  else:
    content_list.append(int(num))
    content_list.append(letter)
    num = ''
content_list.append(int(num))
#[55, '-', 50, '+', 40]

sum = content_list[0]
temp = 0
for index, content in enumerate(content_list):
  if content == '-' or content == '+':
    continue
  
  if content_list[index - 1] == '-':
    if temp > 0:
      sum -= temp
      temp = content
    else:
      temp += content
  elif content_list[index - 1] == '+':
    if temp > 0:
      temp += content
    else:
      sum += content

print(sum - temp)