# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
# Because sets do not have duplicates and union combines the sets together
food = fruit.union(vegetables)
print(food)


# Add an item to fruit
fruit.add("grape")

# Remove an item from vegetables
vegetables.discard("leek")

# Find and display symmetric difference of the two sets
sym = fruit.symmetric_difference(vegetables)
print(sym)