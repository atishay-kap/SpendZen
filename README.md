SpendZen 💸

SpendZen is a personal finance tracker built with Django that helps users manage expenses, set budgets, and gain insights into their spending habits.
It aims to provide a simple yet powerful way to stay mindful of money and make smarter financial decisions.

🚀 Features

✅ User authentication & profiles

✅ Add, edit, and delete expenses

✅ Categorize expenses (food, travel, bills, etc.)

✅ Monthly budget planning & tracking

✅ Interactive charts for spending insights

✅ (Future) AI-powered financial recommendations

🛠 Tech Stack

Backend: Django (Python)

Frontend: Django Templates + Tailwind CSS

Database: SQLite (development), PostgreSQL (production)

Version Control: Git & GitHub

📂 Project Structure
SpendZen/
│── core/           # Project settings & configs
│── apps/           # Django apps (users, expenses, budgets, analytics)
│── templates/      # HTML templates
│── static/         # CSS, JS, images
│── media/          # Uploaded receipts/docs
│── docs/           # Documentation
│── requirements.txt
│── README.md

⚡ Getting Started
1. Clone the repository
git clone https://github.com/<your-username>/SpendZen.git
cd SpendZen

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py migrate

5. Start the server
python manage.py runserver


Now visit 👉 http://127.0.0.1:8000/

📌 Roadmap

 Add recurring expenses

 Export data to CSV/PDF

 Integrate AI (Gemini/OpenAI) for insights

 Mobile-friendly responsive design

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is licensed under the MIT License.