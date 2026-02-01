# Django-job-board

job board platform built with Django, allowing companies to post jobs and users to browse and apply. The project popular job board websites like Indeed or LinkedIn

## 🚀 Features
- User authentication (sign up, login, logout).
- Job management (add, edit, delete jobs).
- Job listings with details such as title, description, salary, and company.
- Blog section for articles or news related to the job market.
- Contact page with Gmail integration for sending messages.
- Media upload support for images and files.
- Frontend built with HTML, CSS, Bootstrap 4, JavaScript, and SCSS.

---

## ⚙️ Tech Stack
- **Backend:** Django (Python) , Django REST Framework , Redis , Celery
- **Frontend:** HTML, CSS, JavaScript, SCSS ,bootstrap 4
- **Database:** PostgreSQL
- **Email Integration:** Send Grid
- **Version Control:** Git + GitHub
- **IDE Config:** VS Code
- **Containerization:** Docker & Docker Compose


## 🐳 Running with Docker

The easiest way to get the project running is using **Docker**. This handles all dependencies, Python environment, and database setups for you.

### 1. Build and Start the Containers
Open your terminal in the project root directory and run:

docker-compose up --build

### 2. Setup Database
In a new terminal, run the migrations inside the container:
docker-compose exec web python manage.py migrate

### 3. Create Admin (Optional)
docker-compose exec web python manage.py createsuperuser
The site will be live at: http://127.0.0.1:8000


## 🖥️ Getting Started

1. Clone the repository
2. https://github.com/abdalahhamwi/Django-job-Board.git
3. Create a virtual environment and install dependencies
python -m venv venv

source venv/bin/activate   # Linux/Mac

venv\Scripts\activate      # Windows

pip install -r requirements.txt
5. Apply migrations
python manage.py migrate
6. Run the development server
python manage.py runserver
7. Open in browser
http://127.0.0.1:8000


```
## 📂 Project Structure
Job-Board/
│
├── accounts/        # User management
├── blog/            # Blog section
├── contact/         # Contact form and email integration
├── home/            # Homepage
├── job/             # Core job board app
├── media/           # Uploaded files and images
├── static/          # CSS/JS/Images
├── templates/       # HTML templates
│
├── Dockerfile       # Docker build instructions
├── docker-compose.yml # Container orchestration
├── db.sqlite3       # Default database
├── manage.py        # Django project manager
└── .gitignore       # Ignored files for Git
```
