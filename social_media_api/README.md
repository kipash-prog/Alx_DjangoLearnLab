# Social Media API

This is a social media API built with Django and Django REST Framework. The API allows users to register, log in, create posts, like/unlike posts, follow/unfollow users, and receive notifications for relevant actions.

## Features

- User registration and authentication
- Create, update, and delete posts
- Like and unlike posts
- Follow and unfollow users
- Comment on posts
- Receive notifications for likes, comments, and follows
- Fetch notifications, including unread notifications

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/kipash-prog/social_media_api.git
   cd social_media_api

### Create and activate a virtual environment(optional)
   python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
### Install the dependencies:

pip install -r requirements.txt

### DJANGO_SECRET_KEY=your-secret-key

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

### Apply the migrations:

python manage.py makemigrations
python manage.py migrate

### createsuperuser
python manage.py createsuperuser

###  the development server:
python manage.py runserver


### Production Setup
   1- Set DEBUG to False in settings.py.
   2-Configure ALLOWED_HOSTS with your domain names.
   3- set up a production database and update the DATABASES in settings.py.
   5- Configure static and media file storage.
   6- Set up a web server (e.g., Nginx) and a WSGI server (e.g., Gunicorn) to serve the application.

### API Endpoints

### Authentication
    POST /api/register/ - Register a new user
    POST /api/login/ - Log in and obtain a token

### Posts
GET /api/posts/ - List all posts
POST /api/posts/ - Create a new post
GET /api/posts/<id>/ - Retrieve a post
PUT /api/posts/<id>/ - Update a post
DELETE /api/posts/<id>/ - Delete a post
POST /api/posts/<id>/like/ - Like a post
POST /api/posts/<id>/unlike/ - Unlike a post

### Comments
GET /api/posts/<post_id>/comments/ - List all comments for a post
POST /api/posts/<post_id>/comments/ - Create a new comment
GET /api/comments/<id>/ - Retrieve a comment
PUT /api/comments/<id>/ - Update a comment
DELETE /api/comments/<id>/ - Delete a comment

### Notifications
GET /api/notifications/ - List all notifications
GET /api/notifications/unread/ - List unread notifications

### Security Settings
The following security settings are configured for production use:

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

### License
This project is licensed under the MIT License. See the LICENSE file for details.