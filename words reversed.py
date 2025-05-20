def reverse_words(text):

    splitted_word = text.split(" ")
#  return splitted_word
    reverse_words = [word[::-1] for word in splitted_word]
#   return rev
    return " ".join(reverse_words) 

print(reverse_words('  double  spaced  words  '))