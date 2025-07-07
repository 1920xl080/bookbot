
def num_of_words(file_path):
    with open(file_path) as file :
        file_content = file.read()
        words = file_content.split()
        return "Found "+str(len(words))+" total words"




def num_of_each_letter(file_path):
    with open(file_path) as file:
        file_content = file.read()
        letter_count = {}
        for letter in file_content:
            if letter.isalpha():
                letter = letter.lower()
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
        # Sort by count descending
        sorted_items = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
        # Convert to list of dictionaries
        result = [f"{letter}: {count}" for letter, count in sorted_items]
        return result
        
        
        
        
        
        
        
        