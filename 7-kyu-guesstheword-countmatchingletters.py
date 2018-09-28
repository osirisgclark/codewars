#7 kyu Guess the Word: Count Matching Letters
def count_correct_characters(a, b):
	if len(correct)!=len(guess):
        raise ValueError
    return [int(correct[i:i+1]==guess[i:i+1]) for i in range(max(len(correct),len(guess)))].count(1)
	
print(count_correct_characters("dog", "car"), 0)
print(count_correct_characters("dog", "god"), 1)
print(count_correct_characters("dog", "cog"), 2)
print(count_correct_characters("dog", "cod"), 1)
print(count_correct_characters("dog", "bog"), 2)
print(count_correct_characters("dog", "dog"), 3)
print(count_correct_characters("dog", "cart"), 0)