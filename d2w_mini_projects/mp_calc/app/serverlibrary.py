
import math
def merge(array, p, q, r, byfunc):
    n_left = q - p
    n_right = r - q
    left_array=array[p:q]
    right_array=array[q:r]
    left_idx = 0
    right_idx = 0
    dest_idx = p
    while (left_idx < n_left) and (right_idx < n_right):
        if (byfunc(left_array[left_idx]) <= byfunc(right_array[right_idx])):
            array[dest_idx]=left_array[left_idx]
            left_idx = left_idx + 1
        else:
            array[dest_idx]=right_array[right_idx]
            right_idx = right_idx + 1
        dest_idx = dest_idx + 1
        
    while (left_idx < n_left):
        array[dest_idx] = left_array[left_idx]
        left_idx = left_idx + 1
        dest_idx = dest_idx + 1
        
    while (right_idx < n_right):
        array[dest_idx] = right_array[right_idx]
        right_idx = right_idx + 1
        dest_idx = dest_idx + 1

    return None

def mergesort_recursive(array, p, r,byfunc):
    
    q = math.ceil((p+r)/2)
    
    num_of_ele_in_array=r-p
    
    if( num_of_ele_in_array <= 1 ):
        return None
    else:
        if num_of_ele_in_array > 1:
            mergesort_recursive(array,p,q,byfunc)    
            mergesort_recursive(array,q,r,byfunc)
            merge(array,p,q,r,byfunc)
    return None

def mergesort(array, byfunc=lambda item: item):
    p = 0
    r = len(array)
    mergesort_recursive(array,p,r,byfunc)
    return None

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) >= 1:
            return self.__items.pop()

    def peek(self):
        if len(self.__items) >=1:
            return self.__items[-1]

    @property
    def is_empty(self):
        return self.__items == []

    @property
    def size(self):
        return len(self.__items)
    
class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self.expr=""
    self.expression=string

  @property
  def expression(self):
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    hasInvalidChar=False
    if(isinstance(new_expr,str)):
      for char in new_expr:
        if char not in self.valid_char:
              hasInvalidChar=True
              break
    else:
      hasInvalidChar=True

    if(hasInvalidChar==True):
      self.expr = ""
    else:
      self.expr = new_expr
      
  def insert_space(self):
    my_new_string = ""
    valid_operands = '0123456789'
    for char in self.expr:
        if char in valid_operands:
              my_new_string = my_new_string + f"{char}"
        else:
              my_new_string = my_new_string + f" {char} "
    return my_new_string

  def process_operator(self, operand_stack, operator_stack):
    #while operator_stack.is_empty == False and operand_stack.size > 1:
    if operator_stack.is_empty == False and operand_stack.size > 1:
      num1 = operand_stack.pop()
      opr = operator_stack.pop()
      if opr == "/":
        opr="//"
      num2 = operand_stack.pop()
      #print(eval(f"{num2} {opr} {num1}"))
      operand_stack.push(eval(f"{num2} {opr} {num1}"))

  def evaluate(self):
    valid_operands = '0123456789'
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    
    #Phase 1 - Scan Expression Left to Right and extract operands, operators and parentheses
    for char in tokens:
      #1.1 - If Extracted character is an operand, push it to operand_stack
      if char in valid_operands:
            operand_stack.push(int(char))
      #1.2 - If Extracterd character is + or -, process all the operators at the top of the operator_stack
      #       and push extracted operator to operator_stack. You should process all the operators as long
      #       as the operator_stack is not empty and the top of the operator_stack is not (or) symbols
      elif char in "+-":
          while operator_stack.is_empty == False and operator_stack.peek() not in "()":
              self.process_operator(operand_stack,operator_stack)
          operator_stack.push(char)
      #1.3. If the extracted character is a * or / operator, process all the * or / operators at the top of the operator_stack and push the extracted operator to operator_stack. 
      elif char in "*/":
          if operator_stack.is_empty == False:
            while operator_stack.peek() in "*/":
              self.process_operator(operand_stack,operator_stack)
          operator_stack.push(char)
      #1.4  If the extracted character is a ( symbol, push it to operator_stack.
      elif char in "(":
            operator_stack.push(char)
      #1.5  If the extracted character is a ) symbol, repeatedly process the operators from the top of operator_stack until seeing the ( symbol on the stack. 
      elif char in ")":
          if operator_stack.is_empty == False:
            while operator_stack.peek() not in "()":
              self.process_operator(operand_stack,operator_stack)
          operator_stack.pop() #remove (
          #operator_stack.push(char)
    
    #Phase 2: Repeatedly process the operators from the top of operator_stack until operator_stack is empty.
    while operator_stack.is_empty == False and operand_stack.size > 1 :
      self.process_operator(operand_stack,operator_stack)
    
    if operator_stack.is_empty == False:
          return None
    else:
      return int(operand_stack.peek())

  def process_operator(self, operand_stack, operator_stack):
    while operator_stack.is_empty == False and operand_stack.size > 1:
      num1 = operand_stack.pop()
      opr = operator_stack.pop()
      if opr == "/":
        opr="//"
      num2 = operand_stack.pop()
      operand_stack.push(eval(f"{num2} {opr} {num1}"))

def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]