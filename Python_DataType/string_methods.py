s = input("what is your favorite movie?")
len_string=len(s)
# Length should be 20
print("Length of s = {}".format(len_string))
# Number of a's should be 2
count_n=s.count("n")
print("n occurs {} times".format(count_n))
#Convert everything to uppercase
print("String in uppercase",s.upper())
# Convert everything to lowercase
print("String in lowercase",s.lower())

print("string in title form",s.title())
# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string",s.split(" "))

