
"""
In the previous exercise we defined our function fully, to the point where
it would have been possible to call it outside of `map`.

But you don't need to do this; you can instead use what's known as a "lambda"
or anonymous function. These are single-use, disposable functions.

Lambdas differ from normal Python methods/functions in that they have only one
expression, can't contain any other statements, and return a function object.

The syntax is:
    lambda [argument]: [return expression / condition]
"""


shopping_list = ["Tomatoes", "Bananas", "Crackers",
                 "Sugar", "Icecream", "Bread", "Bananas", "Chocolate"]
print(shopping_list)

mapped = map(
    lambda item: item[0] == "B",
    shopping_list
)

print(list(mapped))
