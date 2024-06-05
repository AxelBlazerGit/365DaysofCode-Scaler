class Solution:
	# @param A : integer
	# @return a strings
    def split_string_by_groups(self, input_string):
        result = []
        current_group = input_string[0]

        for char in input_string[1:]:
            if char == current_group[-1]:
                current_group += char
            else:
                result.append(current_group)
                current_group = char
    
        result.append(current_group)
        return result

    def countAndSay(self, A):
        if A == 1:
            return "1"
        else:
            prev_sequence = self.countAndSay(A - 1)
            groups = self.split_string_by_groups(prev_sequence)
            count_say_sequence = ""
            for group in groups:
                count_say_sequence += str(len(group)) + group[0]
            return count_say_sequence
