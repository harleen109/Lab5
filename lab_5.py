def main():
  sentence = input("Enter a sentence: ")
  dictionary = create_dictionary("textese.txt")
  translate(sentence, dictionary)

def create_dictionary(txt_file):
  infile = open(txt_file, "r")
  words = [word.rstrip() for word in infile]
  infile.close()
  return dict([word.split(",") for word in words])

def translate(sentence, dictionary):
  words = sentence.split()
  for word in words:
    print(dictionary.get(word, word), " ", end= "")

main()