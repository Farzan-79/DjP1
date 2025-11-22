
# 📘 DjP1 — Interactive Recipe & Article Platform (Django + HTMX + Bootstrap)

A full-stack, dynamic web application for managing recipes, articles, and user profiles — built entirely with Django and enhanced with HTMX for a seamless, single-page-app feel.

## 🌟 Overview

DjP1 is a complete recipe-sharing platform that demonstrates modern Django development with dynamic form interactions, user authentication, validation logic, and clean UX without using heavy frontend frameworks.

The project blends:

✔️ Django (Models, Forms, Views, Auth)

✔️ HTMX for SPA-like interactions

✔️ Bootstrap for styling

✔️ Custom validation and automatic unit conversion

✔️ Image uploads for recipes & profiles

✔️ Permissions + ownership checks

✔️ Full CRUD for recipes & articles

This repository serves as a strong portfolio project, showing skill in handling complex relationships, dynamic forms, server-side validation, and full user interaction flows.

## 🎥Demo Video 

https://github.com/user-attachments/assets/f2d345f4-b65f-4d33-b520-d926289f6309

## 🚀 Key Features

### 🍽️ Recipes Module

Recipes are the heart of this project. Each recipe includes:

- Recipe title
- Description
- Directions (multi-step instructions)
- Image upload
- Ingredient list (dynamic with HTMX)

  
### 📚 Articles Module

- Create and edit articles with:
    - Title
    - Description / body
- Authors can edit or delete their own articles
- Article list + article detail pages
- Uses clean Bootstrap layout

### 🔐 Authentication & Profiles

- User signup, login, logout
- Profile pages with:
    - Bio text
    - Profile picture upload
    - Optional social media links
- Only authenticated users can create/edit/delete content
- Users may only edit or delete their own recipes and articles

#### Dynamic Ingredient Forms (HTMX powered)

Users can:

- Add ingredient rows instantly
- Remove ingredient rows
- Edit rows without full page reload

Each ingredient has:

- Ingredient name
- Quantity
- Unit

#### Smart Ingredient Validation

A major highlight of this project:

Users can input quantities in many formats, e.g.:

- 1
- 1.5
- 1 1/2
- 3/4
- 2 g
- 1 1/2 grams

The system parses, cleans, and converts these values into a normalized format:

- 1 1/2 g → 1.5 g
- 3/4 cup → 0.75 cup

Custom validation ensures:

- Valid units
- Valid numeric formats
- Ingredient rows aren’t left empty

### 📷 Media Handling

- Recipe images
- User profile pictures
- Unique upload paths
- Clean fallback defaults for missing images

### 🔍 Search Functionality

Powerful search for recipes & articles:

- Title search
- Description search
- Ingredients search (depending on structure)
- Clean results page

### 🧠 HTMX Integration Throughout

HTMX provides SPA-like user experience:

- Add/delete ingredient forms dynamically
- Inline edits
- Partial page reloads
- Zero JavaScript written manually

You get a dynamic feel without the complexity of React/Vue.

## 🛠️ Tech Stack
Layer	Tools
- Backend: Django 4.x (Views, Models, Forms, Auth), Custom validators
- Frontend: HTML, Bootstrap 5, HTMX
- Database: SQLite (dev) or PostgreSQL (production-ready)
- Media: Django FileStorage
- Authentication: Django Authentication System
- Deployment Ready: Configurable for Railway / Render / DigitalOcean

## 📂 Project Structure (High-Level)
```
DjP1/
│
├── accounts/                 # user profiles, auth extensions
├── recipes/                  # recipes CRUD, ingredient logic
├── articles/                 # articles CRUD
├── templates/                # shared and app-specific templates
├── static/                   # CSS, JS, Bootstrap assets
├── media/                    # uploaded images
└── DjP1/                     # project settings
```

## ⚙️ Setup & Installation
1. Clone the Repository
```
git clone https://github.com/Farzan-79/DjP1.git
cd DjP1
```

2. Create & Activate Virtual Environment
```
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts ctivate       # Windows
```

3. Install Dependencies
```
pip install -r requirements.txt
```

4. Apply Migrations
```
python manage.py migrate
```

5. Create Superuser
```
python manage.py createsuperuser
```

6. Run Development Server
```
python manage.py runserver
```





## 📄 License

MIT License — free to use, modify, and study.
