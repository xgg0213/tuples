# Create a function that takes in a `tuple` of tuples with varying lengths, a
# given `value`, and a given `length`. The function should return a copy of
# tuple where each nested tuple has the specified `length`. To increase a
# tuple's length, the function should append the value the necessary number of
# times. (You may assume that all tuples originally in the tuple have a length
# <= `length`.)

# Write your function here.
def fill_tuple(tup, val, leng):
    b=list(tup)
    new_list=[]
    for n in b:
        length=len(n)
        if length>=leng:
            new_list.append(n)
        else: 
            while length<leng:
                n=n+(val,)
                length+=1
            new_list.append(n)
    return tuple(new_list)

# can also do in list comprehension
# return tuple(
#         n if len(n) >= min_length else n + (val,) * (min_length - len(n))
#         for n in tup
#     )

print(fill_tuple(((58, 1, 5), (0, 3), (45, ), (24, 23)), 2, 3))    #> ((58, 1, 5), (0, 3, 2), (45, 2, 2), (24, 23, 2))
print(fill_tuple(((1, ), (5, 7), (55, 22), (80, 52, 20)), 5, 4))   #> ((1, 5, 5, 5), (5, 7, 5, 5), (55, 22, 5, 5), (80, 52, 20, 5))
print(fill_tuple(((), (0, 14), (5, 2, 8), (2, 4, 2, 3)), 0, 5))    #> ((0, 0, 0, 0, 0), (0, 14, 0, 0, 0), (5, 2, 8, 0, 0), (2, 4, 2, 3, 0))