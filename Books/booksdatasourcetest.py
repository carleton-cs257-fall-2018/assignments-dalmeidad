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
        self.booksDataSource = booksDataSource.BooksDataSource(books_filename, authors_filename, books_authors_link_filename)

    def tearDown(self):
        pass

    def test_book_method(self):
        self.assertEqual(self.booksDataSource.book(2), {'id': 2, 'title': 'Beloved', 'publication_year': 1987})

    def test_author_method(self):
        self.assertEqual(self.booksDataSource.book(2), {'id': 2, 'last_name': 'Morrison', 'first_name': 'Toni',
        'birth_year': 1931, 'death_year': NULL})

    def test_books_author_id(self):
        self.assertEqual(self.booksDataSource.books(author_id=7), ['Jane Eyre', 'Villette'])

    def test_books_search_text(self):
        self.assertEqual(self.booksDataSource.books(search_text='Dick'), ['Moby Dick'])

    def test_books_start_year(self):
        self.assertEqual(self.booksDataSource.books(start_year=2000), ['All Clear', 'Black Out', 'IQ84','The Power', 'The Fifth Season',
        'The Obelisk Gate', 'The Stone Spy'])

    def test_books_end_year(self):
        self.assertEqual(self.booksDataSource.books(end_year=1820), ['Emma', 'Pride and Prejudice', 'Sense and Sensibility'])

    def test_books_all_fields(self):
        self.assertEqual(self.booksDataSource.books(author_id=2, search_text='Su', start_year=1900, end_year=2000), ['Sula'])

    def test_books_end_year_sort_by_year(self):
        self.assertEqual(self.booksDataSource.books(end_year=1820, sort_by='year'), ['Pride and Prejudice', 'Sense and Sensibility', 'Emma'])

    def test_authors_book_id(self):
        self.assertEqual(self.booksDataSource.authors(book_id=8), ['Pelham Grenville Wodehouse'])

    def test_authors_search_text(self):
        self.assertEqual(self.booksDataSource.authors(search_text='Wode'), ['Pelham Grenville Wodehouse'])

    def test_authors_start_year(self):
        self.assertEqual(self.booksDataSource.authors(start_year=2018), ['Connie Willis', 'Toni Morrison', 'Sinclair Lewis',
        'Neil Gaiman', 'Salman Rushdie', 'Lois McMaster Bujold', 'Haruki Murakami', 'Naomi Alderman', 'N.K. Jemisen',
        'John Le Carré'])

    def test_authors_end_year(self):
        self.assertEqual(self.booksDataSource.authors(end_year= 1818), ['Charlotte Brontë', 'Emily Brontë', 'Charles Dickens'])

    def test_authors_all_fields(self):
        self.assertEqual(self.booksDataSource.authors(book_id=0, search_text='Wi', start_year=1950, end_year=1960), ['All Clear'])

    def test_authors_end_year_sort_by_birth_year(self):
        self.assertEqual(self.booksDataSource.authors(end_year=1818, sort_by='birth_year'), ['Charles Dickens',
        'Charlotte Brontë', 'Emily Brontë'])

    def test_books_for_author(self):
        self.assertEqual(self.booksDataSource.books_for_author(0), [{'id': 0, 'title': 'All Clear', 'publication_year': 2010}, {'id': 3, 'title': 'Blackout', 'publication_year': 2010}, {'id': 27, 'title': 'To Say Nothing of the Dog', 'publication_year': 1997}])

    def test_authors_for_book(self):
        self.assertEqual(self.booksDataSource.authors_for_book(6), [5, 6])

if __name__ == '__main__':
    unittest.main()
