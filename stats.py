def get_book_text(filepath):
        with open(filepath) as f:
                contents = f.read()
        return contents

def get_num_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	char_counts = {}
	for char in text:
		char = char.lower()
		if char.isalpha():
			if char in char_counts:
				char_counts[char] += 1
			else:
				char_counts[char] = 1
	return(char_counts)

def sort_characters(char_counts):
	sorted_list = []
	for char, count in char_counts.items():
		sorted_list.append({"character": char, "count": count})
    
    # Sort the list from greatest to least by count
	def sort_on(dict):
		return dict["count"]
    
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list

