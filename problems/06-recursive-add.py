# Create a recursive function that takes a tuple as an argument and returns the
# summed values in the tuple.

# Write your function here.
def recursive_add(a):
    b=list(a)
    result=0
    for n in b:
        result+=n
    return result
# or simple: return sum(a)

print(recursive_add((2, )))               #> 2
print(recursive_add((2, 4, 6, 8, 10)))    #> 30
print(recursive_add((25, 50, 75, 100)))   #> 250