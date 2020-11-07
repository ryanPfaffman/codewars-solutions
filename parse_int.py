'''
parseInt() reloaded
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them
'''

def parse_int(string):
    lst = string.strip().split(' ')

    digit_nary = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19}

    tens_nary = {'ten': 10, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fourty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}

    hundred_nary = {'hundred': 100}

    thousand_nary = {'thousand': 1000}

    million_nary = {'million': 1000000}

    rtn_number_2 = 0

    def get_num(num):
        rtn_num = 0
        new_num = num.split('-')
        for x in new_num:
            if x in digit_nary.keys():
                rtn_num += digit_nary[x]
            elif x in tens_nary.keys():
                rtn_num += tens_nary[x]
            elif x in hundred_nary.keys():
                rtn_num += hundred_nary[x]
            elif x in thousand_nary.keys():
                rtn_num += thousand_nary[x]
            elif x in million_nary.keys():
                rtn_num += million_nary[x]
        return rtn_num

    def get_num_subset(lst):
        rtn_number = 0
        for x in lst:
            if x in digit_nary.keys():
                rtn_number += get_num(x)
            elif x in tens_nary.keys():
                rtn_number += get_num(x)
            elif x in hundred_nary.keys():
                rtn_number *= get_num(x)
            elif x in thousand_nary.keys():
                rtn_number *= get_num(x)
            elif x in million_nary.keys():
                rtn_number *= get_num(x)
            else:
                rtn_number += get_num(x)
        return rtn_number

    baby_lst = []
    index = 0
    while index < len(lst):
        baby_lst.append(lst[index])
        if lst[index] == 'thousand':
            rtn_number_2 += get_num_subset(baby_lst)
            baby_lst = []
        elif lst[index] == 'million':
            rtn_number_2 += get_num_subset(baby_lst)
            baby_lst = []
        index += 1
    rtn_number_2 += get_num_subset(baby_lst)

    return rtn_number_2

print(parse_int('eighty-eight hundred thousand eighty-eight hundred'))

'''
At first, I was completely stuck on this. I eventually figured out how to find the solutions to around half of the assertions on Codewars, but many of them were failing because of my initial method. The get_num_subset() function was the only method that was being used, and I would multiply the added numbers * either one hundred or one thousand respectively. This led to errors in cases such as "eighty-eight hundred thousand eighty-eight hundred". The algorithm would return 880008800 instead of 8808800 because it was multiplying the ENTIRE number by 100 with the eighty-eight hundred part. Eventually, I figured out that I had to break the initial list down into subsets using the keywords "million" and "thousand". I then made the get_num_subset function that allowed me to get the numbers each of the subsets. Finally, I added all of the numbers returned by the get_num_subset function to the rtn_number_2 integer and then returned rtn_number_2. This was a great exercise and allowed me to use a while loop. However, it took me a while (no pun intended) to figure out how to effectively implement a while loop. Therefore, I probably need some refreshers about how to correctly use while loops.

Another thing is that the algorithm is definitely is running a bit long.

A few of the users on Codewars were able to find a solution that only used THREE for loops. Mine used two for loops and while loop. I still am confused about how to correctly calculate the O Notation, but I suspect that the time complexity of this algorithm is close to O(n2), where n in the length of the initial lst created by splitting the string. The get_num_subset function runs on O(n^2) time complexity, and then you have to add the while loop itself, which runs on O(n). Therefore, I believe that it is possibly accurate to say that the algorithm is running on O(n^2) time complexity. However, I am not completely sure. I will need to do some more research about how to accurately calculate Big O notation of algorithms.

ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
        'eighteen', 'nineteen']
TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def parse_int(string):
    print(string)
    numbers = []
    for token in string.replace('-', ' ').split(' '):
        if token in ONES:
            numbers.append(ONES.index(token))
        elif token in TENS:
            numbers.append((TENS.index(token) + 2) * 10)
        elif token == 'hundred':
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers = [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    return sum(numbers)

'''
