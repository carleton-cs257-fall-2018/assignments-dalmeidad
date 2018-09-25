#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018
    Implemented by Dawson D'almeida and Conor Gormally

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class, Fall 2018.
'''
import csv, sys

class BooksDataSource:
    '''
    A BooksDataSource object provides access to data about books and authors.
    The particular form in which the books and authors are stored will
    depend on the context (i.e. on the particular assignment you're
    working on at the time).

    Most of this class's methods return Python lists, dictionaries, or
    strings representing books, authors, and related information.

    An author is represented as a dictionary with the keys
    'id', 'last_name', 'first_name', 'birth_year', and 'death_year'.
    For example, Jane Austen would be represented like this
    (assuming her database-internal ID number is 72):

        {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}

    For a living author, the death_year is represented in the author's
    Python dictionary as None.

        {'id': 77, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': None}

    Note that this is a simple-minded representation of a person in
    several ways. For example, how do you represent the birth year
    of Sophocles? What is the last name of Gabriel García Márquez?
    Should we refer to the author of "Tom Sawyer" as Samuel Clemens or
    Mark Twain? Are Voltaire and Molière first names or last names? etc.

    A book is represented as a dictionary with the keys 'id', 'title',
    and 'publication_year'. For example, "Pride and Prejudice"
    (assuming an ID of 132) would look like this:

        {'id': 193, 'title': 'A Wild Sheep Chase', 'publication_year': 1982}

    '''

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        ''' Initializes this data source from the three specified  CSV files, whose
            CSV fields are:

                books: ID,title,publication-year
                  e.g. 6,Good Omens,1990
                       41,Middlemarch,1871


                authors: ID,last-name,first-name,birth-year,death-year
                  e.g. 5,Gaiman,Neil,1960,NULL
                       6,Pratchett,Terry,1948,2015
                       22,Eliot,George,1819,1880

                link between books and authors: book_id,author_id
                  e.g. 41,22
                       6,5
                       6,6

                  [that is, book 41 was written by author 22, while book 6
                    was written by both author 5 and author 6]

            Note that NULL is used to represent a non-existent (or rather, future and
            unknown) year in the cases of living authors.

            NOTE TO STUDENTS: I have not specified how you will store the books/authors
            data in a BooksDataSource object. That will be up to you, in Phase 3.
        '''
        self.books_filename = books_filename
        self.authors_filename = authors_filename
        self.books_authors_link_filename = books_authors_link_filename
        self.books_data = []
        self.authors_data = []
        self.books_authors_link = []

        with open(self.books_filename, newline='') as f:
            book_data_file_reader = csv.reader(f)
            for row in book_data_file_reader:
                self.books_data.append(self.create_dictionary(book_id=row[0],
                                                              title=row[1],
                                                              publication_year=row[2]))

        with open(self.authors_filename, newline='') as f:
            author_data_file_reader = csv.reader(f)
            for row in author_data_file_reader:
                self.authors_data.append(self.create_dictionary(author_id=row[0], last_name=row[1],
                                                                first_name=row[2], birth_year=row[3],
                                                                death_year=row[4]))

        with open(self.books_authors_link_filename, newline='') as f:
            book_author_link_file_reader = csv.reader(f)
            for row in book_author_link_file_reader:
                self.books_authors_link.append(self.create_dictionary(book_id=row[0], author_id=row[1]))

    def create_dictionary(self, *, author_id=None, last_name=None,
                          first_name=None, birth_year=None,
                          death_year=None, book_id=None,
                          title=None, publication_year=None):
        dictionary_to_return = {}
        if id_authors and id_books:
            dictionary_to_return['id_authors'] = int(id_authors)
            dictionary_to_return['id_books'] = int(id_books)
        elif author_id:
            dictionary_to_return['author_id'] = int(author_id)
            if last_name:
                dictionary_to_return['last_name'] = last_name
            else:
                dictionary_to_return['last_name'] = None
            if first_name:
                dictionary_to_return['first_name'] = first_name
            else:
                dictionary_to_return['First_name'] = None
            if birth_year:
                dictionary_to_return['birth_year'] = int(birth_year)
            else:
                dictionary_to_return['birth_year'] = None
            if death_year == 'NULL':
                dictionary_to_return['death_year'] = death_year
            elif death_year:
                dictionary_to_return['death_year'] = int(death_year)
            else:
                dictionary_to_return['death_year'] = None
        elif book_id:
            dictionary_to_return['book_id'] = int(book_id)
            if title:
                dictionary_to_return['title'] = title
            else:
                dictionary_to_return['title'] = None
            if publication_year:
                dictionary_to_return['publication_year'] = int(publication_year)
            else:
                dictionary_to_return['publication_year'] = None

        return dictionary_to_return

    def book(self, book_id):
        ''' Returns the book with the specified ID. (See the BooksDataSource comment
            for a description of how a book is represented.) '''
        return self.books_data[book_id]

    def get_author_id(self, book_id):
        list_of_matching_authors = []
        for book in self.books_authors_link:
            if book['book_id'] == book_id:
                list_of_matching_authors.append(book['author_id'])
        return author_id_list

    def get_book_id(self, author_id):
    list_of_matching_books = []
    for author in self.books_authors_link:
        if author['author_id'] == author_id:
            list_of_matching_books.append(author['book_id'])
    return book_id_list

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        ''' Returns a list of all the books in this data source matching all of
            the specified non-None criteria.

                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year

            Note that parameters with value None do not affect the list of books returned.
            Thus, for example, calling books() with no parameters will return JSON for
            a list of all the books in the data source.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year

            See the BooksDataSource comment for a description of how a book is represented.
        '''
        books_to_return = []
        for book_dictionary in self.books_data:
            #generate list of authors connected to book_id
            author_link = self.get_author_id(book_dictionary['book_id'])
            #checks if at least one of the authors in the list matches the author_id in the user's search
            if ((author_id is None or any([author == author_id for author in author_link])) and
               (start_year is None or book_dictionary['publication_year'] >= start_year) and
               (end_year is None or book_dictionary['publication_year'] <= end_year) and
               (search_text is None or (search_text) in book_dictionary['title'])):
               books_to_return.append(book_dictionary)

        if sort_by == "year":
            data_to_return =  sorted(data_to_return, key=lambda book_dict: (book_dict['publication_year'] or ''))

        return books_to_return

    def author(self, author_id):
        ''' Returns the author with the specified ID. (See the BooksDataSource comment for a
            description of how an author is represented.) '''
        return self.authors_data[author_id]

    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):
        ''' Returns a list of all the authors in this data source matching all of the
            specified non-None criteria.

                book_id - only returns authors of the specified book
                search_text - only returns authors whose first or last names contain
                    (case-insensitively) the search text
                start_year - only returns authors who were alive during or after
                    the specified year
                end_year - only returns authors who were alive during or before
                    the specified year

            Note that parameters with value None do not affect the list of authors returned.
            Thus, for example, calling authors() with no parameters will return JSON for
            a list of all the authors in the data source.

            The list of authors is sorted in an order depending on the sort_by parameter:

                'birth_year' - sorts by birth_year, breaking ties with (case-insenstive) last_name,
                    then (case-insensitive) first_name
                any other value - sorts by (case-insensitive) last_name, breaking ties with
                    (case-insensitive) first_name, then birth_year

            See the BooksDataSource comment for a description of how an author is represented.
        '''
        authors_to_return = []
        for author_dictionary in self.authors_data:
            #generate list of books connected to author_id
            book_link = self.get_author_id(book_dictionary['book_id'])

            if ((author_id is None or any([author == author_id for author in author_link])) and
               (start_year is None or book_dictionary['publication_year'] >= start_year) and
               (end_year is None or book_dictionary['publication_year'] <= end_year) and
               (search_text is None or (search_text) in book_dictionary['title'])):
               books_to_return.append(book_dictionary)
        return books_to_return
        return []


    # Note for my students: The following two methods provide no new functionality beyond
    # what the books(...) and authors(...) methods already provide. But they do represent a
    # category of methods known as "convenience methods". That is, they provide very simple
    # interfaces for a couple very common operations.
    #
    # A question for you: do you think it's worth creating and then maintaining these
    # particular convenience methods? Is books_for_author(17) better than books(author_id=17)?

    def books_for_author(self, au1thor_id):
        ''' Returns a list of all the books written by the author with the specified author ID.
            See the BooksDataSource comment for a description of how an book is represented. '''
        return self.books(author_id=author_id)

    def authors_for_book(self, book_id):
        ''' Returns a list of all the authors of the book with the specified book ID.
            See the BooksDataSource comment for a description of how an author is represented. '''
        return self.books(book_id=book_id)


def main():
    book_data_source = BooksDataSource('books.csv', 'authors.csv', 'books_authors.csv')
#    print(book_data_source.book(0))
#    print(book_data_source.author(0))
    print(book_data_source.books(author_id=0)

main()
