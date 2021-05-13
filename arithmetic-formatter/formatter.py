"""
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
"""
# input => ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
def arithmetic_arranger(problems, answer=False):
    arranged_problems = ""
    space_between = " " * 4
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""
    problems_left = len(problems)

    # too many problems
    if problems_left > 5:
        return "Error: Too many problems."

    # loop through items in the list
    for problem in problems:
        # separate the first number, operation sign and second number
        separated = problem.split(" ")
        first_number = separated[0]  # string format
        operador = separated[1]
        second_number = separated[2]

        # only digits
        if first_number.isdecimal() and second_number.isdecimal():
            pass
        else:
            return "Error: Numbers must only contain digits."

        # 4 digits
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        # wrong operador
        if operador not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        num1 = int(first_number)  # integer format
        num2 = int(second_number)

        # check how big need to be
        width = max(len(first_number), len(second_number)) + 2

        # add problems to each line
        dash = "-" * (width)
        first_line += first_number.rjust(width)
        second_line += operador + second_number.rjust(width - 1)
        dash_line += dash
        if operador == "+":
            ans = num1 + num2
        elif operador == "-":
            ans = num1 - num2
        str_ans = str(ans)
        answer_line += str_ans.rjust(width)

        problems_left -= 1
        if problems_left > 0:  # change to problems left
            first_line += space_between
            second_line += space_between
            dash_line += space_between
            answer_line += space_between
        
        if answer:
            arranged_problems = first_line + "\n" + second_line + "\n" + dash_line + "\n" + answer_line
        else:
            arranged_problems = first_line + "\n" + second_line + "\n" + dash_line

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
