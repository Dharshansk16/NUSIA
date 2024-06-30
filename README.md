# NUSIA - Nitte University Student Information Access

Welcome to NUSIA, a student management project designed to streamline the process of managing student information for authorized users, such as teachers and professors. This project is part of my college internship and is built using Django and Bootstrap.

## Features

- **User Authentication:** Secure login for authorized users.
- **CRUD Operations:** Create, Read, Update, and Delete student details.
- **Search Functionality:** Easily search for student information.
- **Responsive Design:** User-friendly interface accessible on various devices.





### Login Page
![Login Page](https://github.com/Dharshansk16/NUSIA/assets/142658700/de6c4c20-9696-410a-abc5-8fce4038f6d2)

The login page provides a secure gateway for authorized users to access the system. Users must enter valid credentials to proceed to the main interface.

### Home Page
![Home Page](https://github.com/Dharshansk16/NUSIA/assets/142658700/fe087b82-d9c0-4ddd-b2d5-a94d28d7fcca)

The home page serves as the dashboard, offering an overview of the system and quick links to various functionalities such as student management, profile settings, and more.

### Profile Page
![Profile Page](https://github.com/Dharshansk16/NUSIA/assets/142658700/9edacda9-919b-452c-9271-90ea0793feb5)

The profile page allows authorised users to view and update student information, ensuring their details are always current and accurate.

### Student Registration Page
![Student Registration Page](https://github.com/Dharshansk16/NUSIA/assets/142658700/2b056219-f7d1-41bc-a984-64f13207e002)

The student registration page enables authorized users to add new student information to the database. It includes fields for entering various details like name, picture, cgpa , USN, course, contact information and placement details.

### Update Page
![Update Page](https://github.com/Dharshansk16/NUSIA/assets/142658700/283b9aad-6bc9-470e-a11f-9f96b9420e34)

The update page provides functionality for modifying existing student records. Users can update details like course information, grades, and personal information.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Dharshansk16/NUSIA.git
2. **Navigate to the project directory:**
   ```sh
   cd NUSIA
   
3. **Install the required Python packages:**
   ```sh
   pip install -r requirements.txt
4. **Apply database migrations**

   ```sh
   python manage.py migrate
5. **Create a superuser to access the admin panel:**

   ```sh
   python manage.py createsuperuser
6. **Run the development server:**

   ```sh
   python manage.py runserver

7.Open your web browser and go to http://127.0.0.1:8000/ to access the application.

# Log in using the superuser credentials.<br>
Navigate through the different sections to manage student information.<br>

Django - The web framework used.<br>
Bootstrap - Frontend framework for responsive design.<br>


## Contributions are welcome! Please fork the repository and create a pull request with your changes.



