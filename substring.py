def count_substring(string, substring):
    count = 0
    start = 0

    while True:
        start = string.find(substring, start)
        if start == -1:  # No more occurrences found
            break
        count += 1
        start += 1  # Move to the next character after the found substring

    return count

# Input string and substring
main_string = "Hello, welcome to the world of programming. Programming is fun!"
substring = "programming"  # Change this to any substring you want to search for

# Count occurrences
occurrences = count_substring(main_string.lower(), substring.lower())

print(f"The substring '{substring}' occurs {occurrences} time(s) in the given string.")
