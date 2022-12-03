#Second: Dict:-
#Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result=dict(zip(keys,values))
print((result))

#Delete a list of keys from a dictionary
# Keys to remove ,keys = ["name", "salary"]
# output:{'city': 'New york', 'age': 25}
sample_dict = {
                "name": "Kelly",
                "age": 25,
                "salary": 8000,
                "city": "New york"
}
keys=["name" , "salary"]
for value in keys:
     sample_dict.pop(value)
print(sample_dict)