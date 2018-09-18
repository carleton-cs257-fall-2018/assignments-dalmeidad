# @author Dawson D'almeida
# @author Conor Gormally
# First assignment in the 'books' series


import csv, sys, re


def books1():
    #taking and checking user arguments for future use
    try:
        file_name = sys.argv[1]
    except IndexError:
        catch_user_error()
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

#exit case for user input error
def catch_user_error():
    print('Usage: \'books\' or \'authors\', sort direction is \'forward\' or \'reverse\' and is optional, file = sys.stderr')
    exit(0)

#puts book data into author and title lists
def parse_book_data(title_year_author, title_data, author_data):
    title_data.append(title_year_author[0])
    get_correct_author_syntax(title_year_author, author_data)

#switches name order and removes birth (and death) years from author names
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

#runs a merge sort on our lists of data
def sort_data(author_or_title):
    return mergesort_data(author_or_title)

#we wrote a merge sort function
def mergesort_data(list):
    if len(list) == 0 or len(list) == 1:
        return list
    else:
        center = len(list)//2
        first_half = mergesort_data(list[0:center])
        second_half = mergesort_data(list[center:])
        return merge(first_half, second_half)

#merge sort helper function
def merge(first_half, second_half):
    merged_list = []
    while len(first_half) != 0 and len(second_half) != 0:
        if first_half[0] <= second_half[0]:
            merged_list.append(first_half[0])
            first_half.remove(first_half[0])
        else:
            merged_list.append(second_half[0])
            second_half.remove(second_half[0])
    if len(first_half) == 0:
        merged_list += second_half
    elif len(second_half) == 0:
        merged_list += first_half
    return merged_list

books1()
