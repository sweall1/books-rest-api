1. Update database with given category
localhost:8000/post/q=war
localhost:8000/post/q=hobbit

2. List of all books
localhost:8000/books

3. Get book with id (ids are taken from google api)
localhost:8000/books/hFfhrCWiLSMC

4. Select authors (separate with comma)
http://localhost:8000/books/?authors=['J. R. R. Tolkien'],['Devin Brown']

5. Select published date
http://localhost:8000/books/?published_date__iexact=2004

6.Date descending
http://localhost:8000/books/?ordering=-published_date

7.Date ascending
http://localhost:8000/books/?ordering=published_date