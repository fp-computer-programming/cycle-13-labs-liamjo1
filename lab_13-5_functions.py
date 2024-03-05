# Liam O'Hara

def calculate_average(numbers):
   total = sum(numbers)
   average = total / len(numbers)
   return average

def find_max_value(numbers):
   maximum = max(numbers)
   return maximum

def count_vowels(text):
   vowels = 'aeiou'
   count = 0
   for char in text:
       if char.lower() in vowels:
           count += 1
   return count

def check_palindrome(word):
   return word == word[::-1]

def reverse_string(sentence):
   return sentence[::-1]

def update_dictionary(key, value, dictionary):
   dictionary[key] = value
   return dictionary

def remove_duplicates(items):
   unique_items = []
   for item in items:
       if item not in unique_items:
           unique_items.append(item)
   return unique_items

def count_odd_numbers(numbers):
   count = 0
   for num in numbers:
       if num % 2 != 0:
           count += 1
   return count

def find_index_of_item(item, items):
   for index, value in enumerate(items):
       if value == item:
           return index
   return -1

def capitalize_words(sentence):
   words = sentence.split()
   capitalized_words = [word.capitalize() for word in words]
   return ' '.join(capitalized_words)

# You can add more functions according to the requirements