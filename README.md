
Maiz Yield Calculator
=====================

A modern web application to estimate corn (maize) production and profit based on field and market data. Built with Django and styled for a clean, responsive user experience.

Features
--------
- Calculate total plants, cobs, and estimated profit from user input
- Modern, mobile-friendly UI with dark mode support
- Instant results without page reload (AJAX)
- No data is stored in the database—calculations are done in-memory

Usage
-----
1. Clone the repository:
   ```sh
   git clone https://github.com/Jenser-Najar/Maiz_Yield_Calculator.git
   cd Maiz_Yield_Calculator
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On Linux/macOS:
   source env/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations (required by Django, but no data is stored):
   ```sh
   python manage.py migrate
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```
6. Open your browser and go to `http://127.0.0.1:8000/`

Project Structure
-----------------
- `core/` — Main Django app (forms, views, models, static, templates)
- `core/static/core/` — CSS and JavaScript files
- `core/templates/core/` — HTML templates
- `maiz_yield_calculator/` — Project settings and URLs
- `requirements.txt` — Python dependencies
- `.gitignore` — Files and folders excluded from version control
- `LICENSE` — MIT License

License
-------
This project is licensed under the MIT License. See the LICENSE file for details.

Author
------
Jenser Najar
