def count_words(text):
    """
    Function to count the number of words in a given text.
    """
    if not text:
        return 0
    
    # Split the text into words using whitespace as the separator
    words = text.split()
    
    return len(words)

def main():
    """
    Main function for user input and output.
    """
    print("Word Counter Program")
    print("Enter a sentence or paragraph:")

    # Prompt user for input
    user_input = input()

    try:
        # Call the function to count words
        word_count = count_words(user_input)

        # Display the word count
        print(f"\nWord Count: {word_count}")
    except Exception as e:
        # Handle potential errors
        print(f"Error: {e}")

if __name__ == "__main__":
    # Run the program
    main()

