N = int(input())
options = []
shortcuts = []
for i in range(N):
  option = input()
  # 단축키 후보
  temp_shortcut = ''
  # 출력할 옵션(대괄호가 추가된 옵션 string)
  new_option = ''

  # 먼저 띄어쓰기 단위로 단어를 나눠서 첫 글자를 단축키로 지정할 수 있는지 확인
  for letter in option.split(' '):
    # 아직까지 나온 단축키 후보가 없고 이미 선정된 단축키 리스트에 단어의 첫 글자가 없을 때
    if temp_shortcut == '' and letter[0].lower() not in shortcuts:
      # 단축키 후보에 저장, 대소문자 구별하지 않으므로 소문자로 통일해서 저장
      temp_shortcut = letter[0].lower()
      # 단축키로 지정할 문자에 대괄호를 지정해서 저장
      # (이 때 단어단위로 저장하므로 띄어쓰기도 같이 넣어줌)
      new_option += '[' + letter[0] + ']' + letter[1:] + ' '
    else:
      # 단축키가 안 되는 단어들은 괄호 없이 그냥 출력할 옵션에 추가
      # (이 때 단어단위로 저장하므로 띄어쓰기도 같이 넣어줌)
      new_option += letter + ' '
  
  # 단어 단위로 검사했을 때 단축키 후보가 안 나왔다면
  if temp_shortcut == '':
    # 단축키 후보가 없어도 아까 for loop 돌면서 option 단어들이 저장되어 있음
    # 새로 검사하면서 단어를 새로 저장해야하므로 초기화
    new_option = ''
    # 한 글자씩 검사
    for i in range(len(option)): 
      # 글자가 띄어쓰기가 아니고 선정된 단축키 리스트에 글자가 없다면
      if option[i] != ' ' and option[i].lower() not in shortcuts:
        # 단축키 후보에 저장, 출력할 옵션 문자열에 대괄호 추가
        temp_shortcut = option[i].lower()
        new_option += option[0 : i] + '[' + option[i] + ']' + option[i + 1:]
        break
  # 단어 단위로 검사했을 때 단축키 후보가 나왔다면
  else:
    # 마지막에 추가된 띄어쓰기 제거
    new_option = new_option[0:-1]
    
  # 단축키로 쓸만한 글자가 없으면 출력할 옵션 문자열이 없다
  # 대괄호가 추가되지 않은 문자열을 저장함
  if new_option == '':
    new_option = option
    
  # 단축키가 있다면 단축키 리스트에 저장
  if temp_shortcut != '':
    shortcuts.append(temp_shortcut)
  # 새로운 option 문자열 저장
  options.append(new_option)

# 그리고 출력
for option in options:
  print(option)




alphabets = {
  'a': 'A',
  'b': 'B',
  'c': 'C',
  'd': 'D',
  'e': 'E',
  'f': 'F',
  'g': 'G',
  'h': 'H',
  'i': 'I',
  'j': 'J',
  'k': 'K',
  'l': 'L',
  'm': 'M',
  'n': 'N',
  'o': 'O',
  'p': 'P',
  'q': 'Q',
  'r': 'R',
  's': 'S',
  't': 'T',
  'u': 'U',
  'v': 'V',
  'w': 'W',
  'x': 'X',
  'y': 'Y',
  'z': 'Z'
}
