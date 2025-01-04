# Create a function that takes in a tuple of strings. It should return a  tuple
# including only the strings that are greater than 8 letters in length.

# Write your function here.
def big_words(a):
    b=list(a)
    return tuple(filter(lambda x: len(x)>8, b))

print(big_words(('earth', 'jupiter', 'mars', 'neptune'))) #> ()
print(big_words(('wakanda', 'melbourne', 'london', 'france'))) #> ('melbourne',)
print(big_words(('app', 'academy', 'app academy', 'xylophone'))) #> ('app academy', 'xylophone')