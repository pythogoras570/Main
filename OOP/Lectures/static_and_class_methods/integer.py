class Integer:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):
            return f'value is not a float'
        return cls(int(float_value))

    @staticmethod
    def from_roman(cls, roman_number):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        int_value = 0
        for i in range(len(roman_number)):
            if roman_number[i] in roman_numerals:
                if i + 1 < len(roman_number) and roman_numerals[roman_number[i]] < roman_numerals[roman_number[i + 1]]:
                    int_value -= roman_numerals[roman_number[i]]
                else:
                    int_value += roman_numerals[roman_number[i]]
        return cls(int_value)

    @staticmethod
    def from_string(cls, value):
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"
