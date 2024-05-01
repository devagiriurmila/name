def analyze_text(filename):
    with open(filename, 'r') as file:
        text = file.read()
        word_count = len(text.split())
        alpha_count = sum(c.isalpha() for c in text)
        digit_count = sum(c.isdigit() for c in text)
        space_count = sum(c.isspace() for c in text)
        
        print("Number of words:", word_count)
        print("Number of alphabets:", alpha_count)
        print("Number of digits:", digit_count)
        print("Number of spaces:", space_count)

# Replace 'filename.txt' with the path to your text file
filename = 'urmila.txt'
analyze_text(filename)