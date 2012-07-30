### run 

###### when run, it runs main & shows an example of LRUCache usage

python lrucache.py

### Unittests:

nosetests

(to use nosetest, if nose is not installed, pip install nose)

### design decisions
I was going to use a list to keep track of orders w/in the dict, 
but I find it's just easier to use the interface of heapq, for quickly accessing the least frequently used item, 
and log n time to remove an item (which would be done frequently)