## Book API Endpoints:

- GET /api/books/ - Retrieve a list of all books.
- GET /api/books/<id>/ - Retrieve a specific book by ID.
- POST /api/books/ - Create a new book (authenticated users only).
- PUT /api/books/<id>/ - Update a book by ID (authenticated users only).
- DELETE /api/books/<id>/ - Delete a book by ID (authenticated users only).

"""
BookListView: - Filter by title, author, and publication_year using the following query parameters: - title - author\_\_name - publication_year - Search by title or author name using the 'search' query parameter. - Order by title or publication_year using the 'ordering' query parameter. - Use '-field_name' for descending order.
"""
