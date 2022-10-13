def IsPalindrome(list):
    list.lower()
    for i in range(0,len(list)-1):
        if(list[i] == list[len(list)]):
            print(list + " jest palindromem")
    else:
        print(list + " Nie jest palindromem")

list = "zakopanenapokaz"

def reversial:
    wrd=input("Please enter a word")
    wrd=str(wrd)
    rvs=wrd[::-1]
    print(rvs)
    if wrd == rvs:
        print("This word is a palindrome")
    else:
        print("This word is not a palindrome")
        
def loops:
    ef reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

    word = input('give me a word:\n')
    x = reverse(word)
    if x == word:
        print('This is a Palindrome')
    else:
        print('This is NOT a Palindrome')

IsPalindrome(list)
