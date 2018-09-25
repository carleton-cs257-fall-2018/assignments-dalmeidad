'''
   booksdatasourcetest
   @author Dawson D'almeida
   @author Conor Gormally

   Tests for the booksdatasource class
'''
import booksdatasource
import unittest

class books_data_source_test(unittest.TestCase):
    def setUp(self):
        self.booksDataSource = booksdatasource.BooksDataSource('books.csv', 'authors.csv', 'books_authors.csv')

    def tearDown(self):
        pass

    def test_book_method(self):
        self.assertEqual(self.booksDataSource.book(2), {'book_id': 2, 'title': 'Beloved', 'publication_year': 1987})

    def test_author_method(self):
        self.assertEqual(self.booksDataSource.author(2), {'author_id': 2, 'last_name': 'Morrison', 'first_name': 'Toni',
        'birth_year': 1931, 'death_year': 'NULL'})

    def test_books_author_id(self):
        self.assertEqual(self.booksDataSource.books(author_id=7), [{'book_id': 7, 'title': 'Jane Eyre', 'publication_year': 1847},
        {'id': 28, 'title': 'Villette', 'publication_year': 1853}])

    def test_books_search_text(self):
        self.assertEqual(self.booksDataSource.books(search_text='Dick'), [{'book_id': 13, 'title': 'Moby Dick', 'publication_year': 1851}])

    def test_books_start_year(self):
        self.assertEqual(self.booksDataSource.books(start_year=2010),
        [{'book_id': 3, 'title': 'Blackout', 'publication_year': 2010},
        {'book_id': 37, 'title': 'The Fifth Season', 'publication_year': 2015},
        {'book_id': 38, 'title': 'The Obelisk Gate', 'publication_year': 2015},
        {'book_id': 35, 'title': 'The Power', 'publication_year': 2016},
        {'book_id': 39, 'title': 'The Stone Spy', 'publication_year': 2015}])

    def test_books_end_year(self):
        self.assertEqual(self.booksDataSource.books(end_year=1820),
        [{'book_id': 5, 'title': 'Emma', 'publication_year': 1815},
        {'book_id': 18, 'title': 'Pride and Prejudice', 'publication_year': 1813},
        {'book_id': 20, 'title': 'Sense and Sensibility', 'publication_year': 1813}])

    def test_books_all_fields(self):
        self.assertEqual(self.booksDataSource.books(author_id=2, search_text='Su', start_year=1900, end_year=2000),
        [{'book_id': 22, 'title': 'Sula', 'publication_year': 1973}])

    def test_books_end_year_sort_by_year(self):
        self.assertEqual(self.booksDataSource.books(end_year=1820, sort_by='year'),
        [{'book_id': 18, 'title': 'Pride and Prejudice', 'publication_year': 1813},
        {'book_id': 20, 'title': 'Sense and Sensibility', 'publication_year': 1813},
        {'book_id': 5, 'title': 'Emma', 'publication_year': 1815}])

    def test_authors_book_id(self):
        self.assertEqual(self.booksDataSource.authors(book_id=8), [{'author_id': 8, 'last_name': 'Wodehouse',
        'first_name': 'Pelham Grenville','birth_year': 1881, 'death_year': 1975}])

    def test_authors_search_text(self):
        self.assertEqual(self.booksDataSource.authors(search_text='Wode'), [{'author_id': 8, 'last_name': 'Wodehouse',
        'first_name': 'Pelham Grenville','birth_year': 1881, 'death_year': 1975}])

    def test_authors_start_year(self):
        self.assertEqual(self.booksDataSource.authors(start_year=2018),
        [{'author_id': 24, 'last_name': 'Carré', 'first_name': 'John Le', 'birth_year': 1931, 'death_year': 'NULL'}
        {'author_id': 2, 'last_name': 'Morrison', 'first_name': 'Toni', 'birth_year': 1931, 'death_year': 'NULL'},
        {'author_id': 0, 'last_name': 'Willis', 'first_name': 'Connie', 'birth_year': 1945, 'death_year': 'NULL'},
        {'author_id': 11, 'last_name': 'Rushdie', 'first_name': 'Salman', 'birth_year': 1947, 'death_year': 'NULL'},
        {'author_id': 12, 'last_name': 'Bujold', 'first_name': 'Lois McMaster', 'birth_year': 1949, 'death_year': 'NULL'},
        {'author_id': 16, 'last_name': 'Murakami', 'first_name': 'Haruki', 'birth_year': 1949, 'death_year': 'NULL'},
        {'author_id': 5, 'last_name': 'Gaiman', 'first_name': 'Neil', 'birth_year': 1960, 'death_year': 'NULL'},
        {'author_id': 20, 'last_name': 'Jemisen', 'first_name': 'N.K.', 'birth_year': 1972, 'death_year': 'NULL'},
        {'author_id': 18, 'last_name': 'Alderman', 'first_name': 'Naomi', 'birth_year': 1974, 'death_year': 'NULL'}])

    def test_authors_end_year(self):
        self.assertEqual(self.booksDataSource.authors(end_year=1818),
        [{'author_id': 4, 'last_name': 'Austen', 'first_name': 'Jane', 'birth_year': 1775, 'death_year': 1817},
        {'author_id': 23, 'last_name': 'Dickens', 'first_name': 'Charles', 'birth_year': 1812, 'death_year': 1870}
        {'author_id': 7, 'last_name': 'Brontë', 'first_name': 'Charlotte', 'birth_year': 1816, 'death_year': 1855},
        {'author_id': 15, 'last_name': 'Brontë', 'first_name': 'Emily', 'birth_year': 1818, 'death_year': 1848}])

    def test_authors_all_fields(self):
        self.assertEqual(self.booksDataSource.authors(book_id=0, search_text='Wi', start_year=1950, end_year=1960),
        [{'author_id': 0, 'last_name': 'Willis', 'first_name': 'Connie', 'birth_year':1945, 'death_year':'NULL'}])

    def test_authors_end_year_sort_by_birth_year(self):
        self.assertEqual(self.booksDataSource.authors(end_year=1818, sort_by='birth_year'),
        [{'author_id': 23, 'last_name': 'Dickens', 'first_name': 'Charles', 'birth_year': 1812, 'death_year': 1870},
        {'author_id': 7, 'last_name': 'Brontë', 'first_name': 'Charlotte', 'birth_year': 1816, 'death_year': 1855},
        {'author_id': 15, 'last_name': 'Brontë', 'first_name': 'Emily', 'birth_year': 1818, 'death_year': 1848}])

    def test_books_for_author(self):
        self.assertEqual(self.booksDataSource.books_for_author(0), [{'book_id': 0, 'title': 'All Clear', 'publication_year': 2010},
        {'book_id': 3, 'title': 'Blackout', 'publication_year': 2010},
        {'book_id': 27, 'title': 'To Say Nothing of the Dog', 'publication_year': 1997}])

    def test_authors_for_book(self):
        self.assertEqual(self.booksDataSource.authors_for_book(6), [{'author_id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry',
        'birth_year': 1948, 'death_year': 2015}, {'author_id': 5, 'last_name': 'Gaiman', 'first_name': 'Neil',
        'birth_year': 1960, 'death_year': 'NULL'}])

if __name__ == '__main__':
    unittest.main()
