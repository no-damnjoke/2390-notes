s = "I love FINA2390 exam"

s.count("love") #Output: 1

s.find("e") #Output: 5

s.rfind("e") #Output: 16 

s.index("E") #Output: substring not found

s.rindex("e") #Output: 16 

s.lower() #Output: 'i love fina2390 exam'

s.replace("love", "hate") #Output: 'I hate FINA2390 exam'

s.rstrip() #Output: ['I', 'love', 'FINA2390', 'exam']

s.split("e") #Output: ['I lov', ' FINA2390 ', 'xam']

s.split(" ") #Output: ['I', 'love', 'FINA2390', 'exam']
