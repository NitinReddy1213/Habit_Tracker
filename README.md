# Habit Tracker Web App

## Overview
Habit Tracker is a Flask-based web application that allows users to track their daily habits, set goals, and monitor progress. Users can log their habits and view their history over time.

## Features
- User authentication (register, login, logout)
- Add, edit, and delete habits
- View habit tracking history
- Responsive and user-friendly design

## Project Structure
```
nitinreddy1213-habit_tracker/
├── README.md
├── app.py
├── requirements.txt
├── routes.py
├── .ENV
├── .ENV.EXAMPLE
├── static/
│   └── index.css
└── templates/
    ├── add_habit.html
    ├── index.html
    └── layout.html
```

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nitinreddy1213/habit_tracker.git
   cd habit_tracker
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Copy `.ENV.EXAMPLE` to `.ENV` and configure necessary variables like database URL and secret key.

5. **Run the Application**
   ```bash
   flask run
   ```

6. **Access the App**
   - Open your browser and go to `http://127.0.0.1:5000`

## Usage
- Register or log in to start tracking habits.
- Add new habits and log daily progress.
- View and manage habits over time.

## Technologies Used
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Database:** MongoDB

## Contributing
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.
