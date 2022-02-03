I chose to use global variables, which I understand are generally a bad idea, but in this case felt necessary.
In a different context and perhaps with more time, I could have implemented a blackjack class and stored some of those variables
as private class instances so they are accessed by all methods while still being protected in a sense.

I make the assumption that the game does not run out of cards in the first deal

I calculate the value of each hand every time, which might be a little inefficient as opposed to keeping a counter.
The reason is I want to be able to explore the different values of A's since it can take 1 or 11, and keeping track of
this in a counter might be a little complicated.

I would test all of the functions independently with unit tests. One challenge there might be keeping track of values in the global variables  which I could handle by defining and calling getter methods on them. One other challenge might be having tests for void functions since they do not return anything, in which case I might have them return some numbers or booleans to show the task was successful, and examine parameters that might have been passed by reference.


