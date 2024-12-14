# Quiz Application

A web-based quiz application built with Django and Bootstrap that allows users to start a quiz, answer questions, track progress, and view the results at the end. This application features a dynamic, interactive interface for answering questions, and allows users to navigate directly to any question in the quiz.

## Features

- **Dynamic Quiz Start**: Users can start a quiz by selecting the number of questions.
- **Question Navigation**: Users can jump to any question in the quiz.
- **Answer Submission**: Users can submit answers to questions, and the quiz tracks their progress.
- **Results Summary**: At the end of the quiz, users are shown a detailed summary of their performance, including correct/incorrect answers and score percentage.
- **Error Handling**: Appropriate error messages are displayed for invalid actions or sessions.

## Table of Contents

1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [Setting Up the Environment](#setting-up-the-environment)
4. [Usage](#usage)
5. [Running the Development Server](#running-the-development-server)
6. [Testing](#testing)
7. [Licenses](#licenses)
8. [Contributing](#contributing)

## Installation

### Prerequisites

Make sure you have Python 3.6+ and pip installed on your machine. If you don't have them, you can download and install Python from [here](https://www.python.org/downloads/).

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/quiz-app.git
    cd quiz-app
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the database**:
    Run migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (optional, for admin access)**:
    ```bash
    python manage.py createsuperuser
    ```

## Project Structure

Here's an overview of the project's file structure:

```
quiz-app/
│
├── quiz/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── quiz/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
```

- **quiz/**: The main app containing all quiz-related functionality, including views, models, and templates.
- **requirements.txt**: Lists the Python packages required to run the project.
- **manage.py**: The main script for managing the Django project.
- **README.md**: This file, providing project documentation.

## Setting Up the Environment

To ensure everything works properly, follow these steps:

1. Clone the repository and set up the virtual environment as mentioned earlier.
2. Make sure to install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run migrations to create the necessary database tables:
    ```bash
    python manage.py migrate
    ```

4. You may need to load some sample quiz data (questions). You can create a superuser and add questions via the Django admin interface at `http://localhost:8000/admin/`.

## Usage

### Starting a Quiz

1. Navigate to the homepage (`/start/`), where you can choose the number of questions for the quiz.
2. After choosing the number of questions, click on **Start Quiz**, and you’ll be redirected to the first question.
3. Answer the questions by selecting one of the multiple-choice options.
4. You can jump to any question using the **All Questions** list on the side.
5. After answering all questions, you will be redirected to the **Summary** page with your quiz results.

### Admin Panel

For administrative access to the site:

1. Go to `http://localhost:8000/admin/`
2. Log in with the superuser credentials you created.
3. Manage questions, users, and other parts of the quiz app.

## Running the Development Server

To start the local development server:

```bash
python manage.py runserver
```

Once the server is running, open your browser and visit `http://localhost:8000` to access the application.

## Testing

The application includes test coverage for most of the functionality. To run tests, use:

```bash
python manage.py test
```

This will run the test cases defined in the `tests.py` file.

## Licenses

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this project, make improvements, and submit pull requests. If you have any questions, issues, or ideas for improvements, please open an issue on GitHub.
