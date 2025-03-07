# Generator for Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fibonacci(12)))

# Generator for prime numbers up to n
def primes(n):
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
print(list(primes(100)))

# Generator for words in a string
def word_generator(text):
    for word in text.split():
        yield word
text = "The alphabets are a,b,c,d,e,etc"
print(list(word_generator(text)))

# Generator for unique words in a list
def unique_words(words):
    seen = set()
    for word in words:
        if word.lower() not in seen:
            seen.add(word.lower())
            yield word
words_list = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
print(list(unique_words(words_list)))

# Generator for sublists of length n
def sublists(lst, n):
    for i in range(len(lst) - n + 1):
        yield lst[i:i+n]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(sublists(numbers, 3)))