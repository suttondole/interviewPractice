##creating function to be called from shell
def inclusiveListRanges(start, end):
    ##variable to keep track of number that is being inserted into list
    numToInsert = start
    ##empty list **note in order to add things we must use a.insert(location, value)
    a = []
    ##x represents where we are in list (locations work the same as arrays)
    ##for range(number), number represents where we stop, noninclusive i.e. loop will not
    ##run when x = number so we add one so that the end value is added
    for x in range((end - start) + 1):
        a.insert(x, numToInsert)
        ##incrementing number by one since we want sequential list of numbers
        numToInsert = numToInsert + 1
    ##printing whole list (python allows this lol)
    print(a)
