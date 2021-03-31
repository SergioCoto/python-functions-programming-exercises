names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']
## CREATE YOUR FUNCTION HERE
def sort_names(names1): 
    names1.sort(reverse=False)   
    return names1
print(sort_names(names))
