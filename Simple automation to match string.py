class StringMatcher:
    def __init__(self):
        self.current_state = 0
    def match(self, input_string):
        for char in input_string:
            if char == 'a':
                self.current_state = 1
            elif char == 'b' and self.current_state == 1:
                self.current_state = 2
            else:
                self.current_state = 0
        return self.current_state == 2
matcher = StringMatcher()
input_strings = ["ab", "abc", "aab", "abab", "cba"]
for input_string in input_strings:
    if matcher.match(input_string):
        print(f"'{input_string}' is accepted")
    else:
        print(f"'{input_string}' is rejected")
