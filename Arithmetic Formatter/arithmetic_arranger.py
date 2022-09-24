def arithmetic_arranger(problems, show_answer = False):
    top_str, bottom_str, line_str, answer_str = str(), str(), str(), str()

    if len(problems) > 5 :
        return "Error: Too many problems."

    count = 0
    while count < len(problems) :
        problem = problems[count]
        problem = problem.split()
        operand1, operator, operand2 = problem[0], problem[1], problem[2]

        if (operand1.isdigit() != True) or (operand2.isdigit() != True) :
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4 :
            return "Error: Numbers cannot be more than four digits."
        if problem[1] != '+' and problem[1] != '-' :
            return "Error: Operator must be '+' or '-'."

        # Get width of largest number add 2 for a space and operator
        width = max(len(operand1),len(operand2)) + 2

        # Build the strings. First time around there should be no space before operator
        if count == 0 :
            top_str = top_str + str(operand1.rjust(width))
            bottom_str = bottom_str + str(operator + " " + operand2.rjust(width - 2))
            line_str = line_str + str('-' * width)
        else :
            top_str = top_str + "    " + str(operand1.rjust(width))
            bottom_str = bottom_str + "    " + str(operator + " " + operand2.rjust(width - 2))
            line_str = line_str + "    " + str('-' * width)

        if show_answer == True :
            if operator == '+' : answer = int(operand1) + int(operand2)
            else : answer = int(operand1) - int(operand2)
            answer = str(answer)

            if count == 0 :
                answer_str = answer_str + str(answer.rjust(width))
            else :
                answer_str = answer_str + "    " + str(answer.rjust(width))

            arranged_problems = f"{top_str}\n{bottom_str}\n{line_str}\n{answer_str}"
        elif show_answer == False :
            arranged_problems = f"{top_str}\n{bottom_str}\n{line_str}"

        count += 1
    return arranged_problems
