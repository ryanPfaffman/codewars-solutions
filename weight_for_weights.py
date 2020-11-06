'''
My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.
I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.
For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?
Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"
When two numbers have the same "weight", let us class them as if they were strings and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9) it comes before as a string.
All numbers in the list are positive numbers and the list can be empty.
Notes
Don't modify the input
For C: The result is freed.
'''
#my solution
def order_weight(string):
    string_list = sorted(string.strip().split(' '))

    temp_list = []
    first_tuples = []
    sorted_tuples = []
    return_string = ''


    for num in string_list:
        for x in num:
            temp_list.append(int(x))
        first_tuples.append((num,sum(temp_list)))
        temp_list = []

    def getKey(item):
        return item[1]

    sorted_tuples = sorted(first_tuples, key=getKey)

    for x,y in sorted_tuples:
        return_string += str(x) + " "

    return return_string.strip()
'''
Figuring out this solution was definitely difficult for me. I started my thought process by wanting to do a nested loop:
def order_weight(string):
    string_list = string.strip().split(' ')

    temp_list = []
    first_tuples = []
    sorted_tuples = []
    return_string = ''
    
    for x in string_list:
        for x in num:
            temp_list.append(int(x))
        first_tuples.append((num,sum(temp_list))
        temp_list = []

    def getKey(item):
        return item[1]

    sorted_tuples = sorted(first_tuples, key=getKey)

    for x,y in sorted_tuples:
        return_string += str(x) + " "

    return return_string

I completely forgot about to sort the string during the first .splice() method. Oops. I also had a trailing " " at the end of the return string and that was leading to errors. After some
editing, I was finally able to get the code to pass. However, it still uses a nested loop and another loop to loop through the list of tuples.
But, I got some more experience with the tuples. So that's always good I guess.
 
Finally, when trying to solve these, I always seem to be taking the long way, when there always seems to be a simple solution there somewhere. After about an hour and a
half, I ended up having to finally search for the answer.
'''

#better solution written by Manish-Giri
def order_weight(string):

    def sort_by(list):
        return sum([int(x) for x in list])

    string_list = sorted(string.strip().split(' '))

    return_list = sorted(string_list, key=sort_by)

    return " ".join(return_list)
