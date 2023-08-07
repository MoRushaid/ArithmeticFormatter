def arithmetic_arranger(problems, condition = False):
        
  def count_digits(num):
    digits = 0
    while(num > 0):
      digits += 1
      num = num // 10
    return digits

  def formulate_operands(operand_1, operand_2, operator):
    
    operand_digits_1 = len(str(operand_1))
    operand_digits_2 = len(str(operand_2))
  
    max_digits = max(operand_digits_1, operand_digits_2)
    
    if operand_digits_1 == max_digits:
      first = '  ' + str(operand_1)
      second = operator + (' '* (max_digits + 1 - operand_digits_2)) + str(operand_2)
    else:
      first = '  ' + (' ' * (operand_digits_2 - operand_digits_1)) + str(operand_1)
      second = operator + ' ' + str(operand_2)

    return first, second 

  def formulate_seperator(length):
    return '-' * length
    
  def formulate_answer(a,b, operator):
    if operator == '+':
      ans = a + b
    else:
      ans = a - b
    final_ans = (' ' * (len(seperator) - len(str(ans)))) + str(ans) 
    return final_ans

  def formulate_to_string(blocks):
    
    string = ''
  
    for i in range(len(blocks[0])):
      row = ''
      for j in range(len(blocks)):
        row += blocks[j][i]
        if j < len(blocks) - 1:
          row += '    '
      string += row
      if i < len(blocks[0]) - 1:
        string += '\n'

    return string
    
  import re
  
  if len(problems) > 5:
    return 'Error: Too many problems.'
    
  all_operands = []
  all_operators = []
  blocks = []
  
  for problem in problems:
    operands = re.findall('[0-9]*', problem)
    operands = [int(num) for num in operands if num != '']
    
    try:
      operator = re.findall('[+,-]', problem)[0]
    except:
      return "Error: Operator must be '+' or '-'." 
      
    all_operands.append(operands)
    all_operators.append(operator)
  
    if len(all_operands[0]) > 2:
      return "Error: Numbers must only contain digits."
      
  for i in range(len(problems)):
    
    a, b = all_operands[i]
    operator = all_operators[i]
    
    if (str(a).isdigit() or str(b).isdigit()) == False:
      return "Error: Numbers must only contain digits."
    elif a > 9999 or b > 9999:
      return "Error: Numbers cannot be more than four digits."
  
    first, second = formulate_operands(a, b, operator)
    seperator = formulate_seperator(len(first))
    answer = formulate_answer(a, b, operator)
    
    if condition == True:
      blocks.append([first, second, seperator, answer])
    else:
      blocks.append([first, second, seperator])
  
  string = formulate_to_string(blocks)
  
  return string
