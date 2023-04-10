"""Count words in file."""

def word_count_function(filename):    
  file = open(filename)
  # data = file.read()

  word_count = {}

  for line in file:
     line = line.strip()
     words = line.split()
  print(words)
  #    for word in words:
  #         word_count[word] = word_count.get(word, 0) + 1

  # for word, count in word_count.items():
  #   print(word,count)

word_count_function('test.txt')



# # 1. access the file
# # 2. turn the file into a..?
#     # we tried turning it into a list, but a list is unhashable
# # 3. iterate over the..?
