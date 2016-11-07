#Leo Ascenzi
#sets up empty string
ohne_vowels = ""

#gets response
resp = str(raw_input("Enter a message: "))

#for loop to check if character is in a string
for char in resp:
    if char not in "aeiouAEIOU":
        ohne_vowels += char
        
print ohne_vowels
