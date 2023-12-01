class AdventInput:
    def input_to_list(self, input_file):
        input = []
        with open(input_file) as f:
            input = f.read().splitlines()
        return input

    def input_to_list_list(self, input_file):
        input = []
        with open(input_file) as f:
            for index, line in enumerate(f.read().splitlines()):
                input.append([c for c in line])
        return input

    def input_to_int_list_list(self, input_file):
        input = []
        with open(input_file) as f:
            for index, line in enumerate(f.read().splitlines()):
                input.append([int(c) for c in line])
        return input

    def input_to_int_list(self, input_file):
        input = []
        with open(input_file) as f:
            input = f.read().splitlines()
        input = [int(i) for i in input]
        return input

    def input_to_list_blank_line(self, input_file):
        input = []
        with open(input_file) as f:
            input = f.read().split('\n\n')
        input = [i.replace('\n', ' ') for i in input]
        return input

    def input_to_list_remove_blanks(self, input_file):
        input = []
        with open(input_file) as f:
            input = f.read().split('\n\n')
            # input = [i.replace('\n', ' ') for i in input]
        return input
