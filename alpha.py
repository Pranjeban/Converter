def test_alpha(input_alpha):

    for i in range(len(input_alpha)):

        if input_alpha[i].isdigit() == True:
            return False

        if input_alpha[i] == '-':
            return False

    return True