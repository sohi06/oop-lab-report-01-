def convert_case(s):
  
    converted_string = ''.join(char.upper() if char.islower() else char.lower() for char in s)
    return converted_string

print(convert_case("Hello World! This is Python."))
