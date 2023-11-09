def freq(word_input):
    letters_dict = {}
    max_frequency = 0
    # Build a dict of all 26 letters of the alphabet (you can use
    for letter_ord in range(ord('a'), ord('z')):
        letters_dict[chr(letter_ord)] = 0
    # Normalize to lowercase
    word = word_input.lower()
    for letter in word:
        # If that letter is in the dict
        if letter in letters_dict:
            # Increase the frequency for that letter
            letters_dict[letter] += 1
            # and decide if it is the new max_frequency
            max_frequency = max(max_frequency, letters_dict[letter])
    final = ''
    for letter in letters_dict:
        # if the frequency of that letter is the same as the max_frequency append to the final string
        if letters_dict[letter] == max_frequency:
            final += letter
    print(final)
    return final


assert freq("Computers account for only 5% of the country's commercial electricity consumption") == "co"
assert freq("Input") == "inptu"
assert freq("frequency letters") == "e"
