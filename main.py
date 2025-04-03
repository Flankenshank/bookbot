import sys

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

# Import the functions from stats.py
from stats import get_book_text, get_num_words, count_characters, sort_characters

def main():
    # Path to the book
    path = sys.argv[1]
    
    # Get the text from the book
    text = get_book_text(path)
    
    # Get the word count
    word_count = get_num_words(text)
    
    # Get the character counts
    char_counts = count_characters(text)
    
    # Sort the character counts
    sorted_chars = sort_characters(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        character = char_dict["character"]
        count = char_dict["count"]
        print(f"{character}: {count}")
    
    print("============= END ===============")

# Call the main function
if __name__ == "__main__":
    main()
