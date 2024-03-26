def main():
	word_split = []
	letter_count = {}

	with open("/home/dc/workspace/github.com/zfbs/bookbot/books/frankenstein.txt") as f:
		file_contents = f.read()
		
	
	word_split = file_contents.split()
	wordcount = len(word_split)
	#print(file_contents, wordcount)

	#lowering the characters in the book, and counting the occurences of letters
	lowered_string = file_contents.lower()
	letter_split = [character for character in lowered_string]

	for letter in letter_split:
		#define whether the character is alphabetic (isalpha function)
		if letter.isalpha():
			letter_count[letter] = letter_count.get(letter, 0) + 1
	
	letter_count = dict(sorted(letter_count.items(), key=lambda item:item[1], reverse=True))
	
	#letter count report
	print(f"--- Begin report of books/frankenstein.txt ---\n{wordcount} words found in the document\n")
	for key, value in letter_count.items():
		print(f"The '{key}' character was found {value} times")
	print("--- End Report ---")

if __name__ == '__main__':
	main()
