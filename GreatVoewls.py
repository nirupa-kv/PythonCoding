#Finds the word(s) in a sentence that contain the highest number of vowels
sentence=str(input("Enter the sentence: "))
word_list=list()
weight_list=list()
great_weightage=[]
word_list=sentence.split(' ')
print(word_list)
vowels=['a','e','i','o','u','A','E','I','O','U'];
for word in word_list:
    weight=0
    for x in word:
        if x in vowels:
            weight=weight+1
    weight_list.append(weight)
word_weight_dict={x:y for x,y in zip(word_list,weight_list)}
print(word_weight_dict)
great=max(weight_list)
for x,y in word_weight_dict.items():
   if y==great:
      great_weightage.append(x)
print("The word with highest number of alphabets is ",','.join(great_weightage)," and the count is ",great);