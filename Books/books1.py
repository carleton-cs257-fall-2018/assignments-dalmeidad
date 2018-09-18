# @author Dawson D'almeida
# @author Conor Gormally
# First assignment in the 'books' series


import csv, sys, re


def books1():
    #taking and checking user arguments for future use
    file_name = sys.argv[1]
    try:
        data_to_display = sys.argv[2]
    except IndexError:
        catch_user_error()
    try:
        sort_direction = sys.argv[3]
    except IndexError:
        sort_direction = None
    #initialize lists of authors and titles
    title_data = []
    author_data = []
    #creates a csv reader and parses through the csv file to fill the lists
    with open(file_name, newline='') as f:
        file_reader = csv.reader(f)
        print('test')
        for row in file_reader:
            parse_book_data(row, title_data, author_data)
        author_data = sort_data(author_data)
        title_data = sort_data(title_data)
    #uses arguments and filled list to print correct data in correct sort direction
    check_user_input(data_to_display, sort_direction, title_data, author_data)

#re-sorts the list if user wants list in reverse order, prints data based on user input
def check_user_input(data_to_display, sort_direction, title_data, author_data):
    if(sort_direction == 'reverse'):
        title_data.reverse()
        author_data.reverse()
    if(data_to_display == 'books'):
        print(title_data)
    elif(data_to_display == 'authors'):
        print(author_data)
    else:
        catch_user_error()

def catch_user_error():
    print('Usage: \'books\' or \'authors\', sort direction is \'forward\' or \'reverse\' and is optional, file = sys.stderr')
    exit(0)

def parse_book_data(title_year_author, title_data, author_data):
    title_data.append(title_year_author[0])
    get_correct_author_syntax(title_year_author, author_data)


def get_correct_author_syntax(title_year_author, author_data):
    just_author_names = re.sub(r'\([^()]*\)', '', title_year_author[2])
    for authors in just_author_names.split('and'):
        authors = authors.strip()
        author_first_last_name = authors.split(' ')
        last_name = author_first_last_name[-1] + ', '
        author_first_last_name = author_first_last_name[0:-1]
        proper_name_display = last_name + " ".join(str(x) for x in author_first_last_name)
        if proper_name_display not in author_data:
            author_data.append(proper_name_display)

def sort_data(author_or_title):
    return mergesort_data(author_or_title)

def mergesort_data(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        center = len(x)//2
        a = mergesort_data(x[0:center])
        b = mergesort_data(x[center:])
        return merge(a, b)

def merge(a, b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] <= b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    elif len(b) == 0:
        c += a
    return c

books1()
