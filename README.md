# Django-job-board

A simple job board platform built with Django, allowing companies to post jobs and users to browse and apply. The project is designed as a learning exercise to simulate popular job board websites like Indeed or LinkedIn but in a simplified form.

## 🚀 Features
- User authentication (sign up, login, logout).
- Job management (add, edit, delete jobs).
- Job listings with details such as title, description, salary, and company.
- Blog section for articles or news related to the job market.
- Contact page with Gmail integration for sending messages.
- Media upload support for images and files.
- Frontend built with HTML, CSS, JavaScript, and SCSS.

---

## ⚙️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript, SCSS
- **Database:** PostgreSQL
- **Email Integration:** Gmail SMTP
- **Version Control:** Git + GitHub
- **IDE Config:** VS Code


## 🖥️ Getting Started

1. Clone the repository
2. https://github.com/abdalahhamwi/Django-job-Board.git
3. Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
4. Apply migrations
python manage.py migrate
5. Run the development server
python manage.py runserver
6. Open in browser
http://127.0.0.1:8000


📌 Conclusion
The Job Board Project is a practical example of building a Django-based job listing platform. It provides a foundation for learning user authentication, job management, and integration of multiple apps within a single Django project. With further development, it can evolve into a fully functional professional job board.

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
├── db.sqlite3       # Default database
├── manage.py        # Django project manager
└── .gitignore       # Ignored files for Git
