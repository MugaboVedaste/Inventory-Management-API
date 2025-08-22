Inventory Management API
Project Overview

The Inventory Management API is a backend system built with Django REST Framework that allows users to manage store inventory.
The API supports creating, viewing, updating, and deleting inventory items, tracking stock levels, and maintaining a change history for each item.
Users are authenticated before they can manage inventory data.

This project is part of a Capstone Project divided into 5 phases: Idea & Planning, Design, Start Building, Continue Building, and Finalize & Submit.

Features Implemented (Week 3 – Start Building)

Custom User Model

Fields: username, full_name, telephone, email, password

Token-based authentication (DRF Token Authentication)

Category Model

Fields: name, description

InventoryItem Model

Fields: name, description, category, supplier, quantity, price, date_added, last_updated, owner

supplier field is manually entered and can later be used for search/filter

InventoryChangeHistory Model

Logs changes in inventory quantities with details of the user who made the change and timestamp

API Endpoints (partial implementation)

POST /api/register/ – Register a new user

POST /api/login/ – Log in and receive authentication token

GET /api/items/ – List inventory items (basic)

POST /api/items/ – Create inventory items (authenticated users only)

PUT /api/items/{id}/ – Update inventory items (owner only)

DELETE /api/items/{id}/ – Delete inventory items (owner only)

Project Structure
inventory_api/
│
├── inventory/                 # Django app
│   ├── migrations/            
│   ├── models.py              # User, Category, InventoryItem, InventoryChangeHistory
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # ViewSets for API
│   ├── urls.py                # API routing
│
├── inventory_api/             # Project settings
│   ├── settings.py            # Add rest_framework, custom user model
│   └── urls.py
│
├── manage.py
└── README.md                  # Project documentation

Installation & Setup

Clone the repository:

git clone <repository_url>
cd inventory_api


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows


Install dependencies:

pip install django djangorestframework


Apply migrations:

python manage.py makemigrations
python manage.py migrate


Create a superuser (optional for testing):

python manage.py createsuperuser


Start the development server:

python manage.py runserver

Authentication

Users authenticate using DRF Token Authentication.

Generate a token for a user:

python manage.py drf_create_token <username>


Include token in API requests:

Authorization: Token <token_value>

Next Steps (Week 4 & Beyond)

Implement search, filtering, pagination, and sorting for inventory items

Add InventoryChangeHistory logging on item updates

Enhance API permissions

Write tests and finalize documentation

Deploy the API on Heroku or PythonAnywhere
