# ArithmeticFormatter
A function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function will optionally take a second argument. When the second argument is set to True, the answers would be displayed.

Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
- If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
- The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
- Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
- Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.

If the user supplied the correct format of problems, the conversion will follow these rules:
- There would be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, and both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
- Numbers would be right-aligned.
- There would be four spaces between each problem.
- There would be dashes at the bottom of each problem. The dashes would run along the entire length of each problem individually.
