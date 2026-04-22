# Write a function that takes a sentence and returns the number of vowels in it.
 
def find_vowels(word):
    count = 0
    vowels = "aeiou,AEIOU"

    for char in word:
        if char in vowels:
          count +=1

    return(count)
print(find_vowels("anudeep"))
