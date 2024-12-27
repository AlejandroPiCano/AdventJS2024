def create_xmas_tree(height, ornament):
  result = ''
  for i in range(1, height+1):
    spaces = '_'*(height-i)
    result += spaces + ornament*(2*i-1) + spaces + '\n'
   
  result += '_'*(height-1) + '#' + '_'*(height-1) + '\n'
  result += '_'*(height-1) + '#' + '_'*(height-1)
  return result

print(create_xmas_tree(5, '*'))