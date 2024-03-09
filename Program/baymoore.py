def preprocess_pattern(pattern):
    bad_char_shift = {}
    pattern_length = len(pattern)
    for i in range(pattern_length - 1):
        bad_char_shift[pattern[i]] = pattern_length - i - 1
    return bad_char_shift
def boyer_moore_search(text, pattern):
    bad_char_shift = preprocess_pattern(pattern)
    text_length = len(text)
    pattern_length = len(pattern)
    occurrences = []
    i = pattern_length - 1
    while i < text_length:
        j = pattern_length - 1
        k = i
        while j >= 0 and text[k] == pattern[j]:
            k -= 1
            j -= 1
        if j == -1:
            occurrences.append(k + 1)
            bad_char_shift_value = bad_char_shift.get(text[i], pattern_length)
            i += max(1, pattern_length - j, bad_char_shift_value)
        else:
            bad_char_shift_value = bad_char_shift.get(text[i], pattern_length)
            i += max(1, bad_char_shift_value)
    return occurrences


# Get input from the user
text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")
# Perform search
results = boyer_moore_search(text, pattern)
# Display result
if results:
 print("Pattern found at indices:", results)
else:
 print("Pattern not found in the text.")
