"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):
    # Your code here
    # lst.sort(key = lambda each_item: len(each_item))
    lst.sort(key = len, reverse=True)
    print(lst)
    
sort_by_length(["may", "april", "september", "august"])    
sort_by_length(["apple", "pie", "shortcake"])    

