N, M = map(int, input().split())
S = {}
prefixes = []

for i in range(N):
  word = input()
  node = S
  for letter in word:
    if not node.get(letter):
      node[letter] = {}
    node = node[letter]

def startsWith(word):
  global S
  node = S
  for char in word:
    if not node.get(char):
      return False
    node = node[char]
  return True
  
count = 0
for i in range(M):
  prefix = input()
  isStartsWith = startsWith(prefix)
  if isStartsWith:
    count += 1
  
print(count)

# 1 3
# yerami
# y
# yeramimi
# yeram
# hiyerami
# helloyeramimi
  
# {'b': 
#   {'a': 
  #   {'e': 
    #   {'k': 
      #   {'j': 
        #   {'o': 
          #   {'o': 
            #   {'n': 
            #     {'o': {'n': {'l': {'i': {'n': {'e': {'j': {'u': {'d': {'g': {'e': {}}}}}}}}}}}}}}}}}}},
            
            
# ,'s': 
#   {'t': {'a': {'r': {'t': {'l': {'i': {'n': {'k': {}}}}}}}}, 
#     'u': {'n': {'d': {'a': {'y': {'c': {'o': {'d': {'i': {'n': {'g': {}}}}}}}}}}}},