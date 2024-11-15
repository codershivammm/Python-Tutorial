#Write a python function to remove a given word from a list ad strip it at the same time

def remove_and_strip(word_list, word_to_remove):
    cleaned_list = []
    for item in word_list:
        stripped_item = item.strip()
        if stripped_item != word_to_remove:
            cleaned_list.append(stripped_item)
    return cleaned_list

# Example usage
words = [" apple ", "banana", "  orange", " apple", "grape "]
result = remove_and_strip(words, "apple")
print(result)  # Output: ['banana', 'orange', 'grape']
