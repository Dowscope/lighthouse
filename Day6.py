def find_the_gate(spots, vehicle):
    for i in range(len(spots)):
        if vehicle == 'wide' and spots[i] == 'W':
            return i
        elif vehicle == 'narrow' and (spots[i] == 'W' or spots[i] == 'N'):
            return i
    return False



print(find_the_gate(
  ['w','n','N'], 'narrow'
))

print(find_the_gate(
  ['w','n','N','`W`','n','W'],'wide'
))

print(find_the_gate(
  ['w','n','n','w','n','n'], 'narrow'
))

print(find_the_gate(
  ['w','n','n','w','N','n','w','N','N','w','n','n','w','n','n','W','W','W','W','n','n','w','n','n'], 'wide'
))