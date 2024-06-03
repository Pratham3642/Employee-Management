### Reservation Management

The Employee Management System is a Python application that leverages Tkinter for its graphical user interface (GUI) and SQLite for its database management. The system allows users to manage employee records efficiently and includes features such as adding, viewing, updating, and deleting employee information. Additionally, it provides functionalities to display current location and temperature, as well as visualizing the top 5 employees by salary using a bar chart.

## Database:

1. Install sqlite3
2. In terminal Open or Create database with **sqlite3 employee.db** and table name **employee**
3. CREATE TABLE employee(id INTEGER PRIMARY KEY,name TEXT,salary REAL);

## Key Features

**Add Employee:**

  -  Allows users to add a new employee by entering their ID, name, and salary.
  -  Validates input to ensure that the employee ID is unique, the name is valid, and the salary is a positive number.

**View Employees:**

  -  Displays a list of all employees stored in the database.
  -  Each employee entry includes ID, name, and salary.

**Update Employee:**

  -  Allows users to update the details of an existing employee.
  -  Users can modify the employee's name and salary based on the employee ID.

**Delete Employee:**

  -  Enables users to delete an employee record from the database using the employee ID.

**Location Display:**

  -  Fetches and displays the current location (city and region) of the user using the ipinfo.io API.

**Temperature Display:**

  -  Fetches and displays the current temperature in a specified city (e.g., Mumbai) using the OpenWeatherMap API.

**Salary Chart:**

  -  Generates and displays a bar chart of the top 5 employees by salary.
  
  -  Uses Matplotlib to create the chart and updates it dynamically based on the current database entries.

## Implementation Details

**GUI:** The GUI is built using Tkinter, providing a user-friendly interface for interacting with the system. The main window includes buttons for different functionalities, and additional Toplevel windows are used for specific tasks like adding, updating, and deleting employees.

**Database:** SQLite is used for storing employee records. The database (employee.db) contains a table named employee with columns for ID, name, and salary.

## APIs:

**Location:** The ipinfo.io API is used to fetch the user's current location.

**Temperature:** The OpenWeatherMap API is used to fetch the current temperature in a specified city.

**Data Validation:** Functions are implemented to validate employee ID, name, and salary inputs to ensure data integrity.

## Input Validations:

**Employee ID Validation (validateid()):**

-  Checks if the ID field is empty.
-  Verifies if the ID is a positive integer.
-   eturns appropriate error messages if validation fails.

**Employee Name Validation (validatename()):**

-  Ensures that the name field is not empty and does not contain only spaces.
-  Validates if the name contains only alphabetical characters.
-  Checks if the name length is between 2 and 50 characters.
-  Returns specific error messages based on validation results.

**Salary Validation (validatesalary()):**

-  Validates if the salary field is not empty.
-  Verifies if the salary is a positive number.
-  Returns appropriate error messages if validation fails.

## Output 

**Main window:**

![Screenshot 2024-06-03 225102](https://github.com/Pratham3642/Employee-Management/assets/162919475/8a257442-2f5b-4bfb-b6f7-0976a5095c9d)

**Add window:**


![Screenshot 2024-06-03 224916](https://github.com/Pratham3642/Employee-Management/assets/162919475/83b31f73-9604-4df4-97f0-8272c482cf02)

**View Window:**

![Screenshot 2024-06-03 225023](https://github.com/Pratham3642/Employee-Management/assets/162919475/e1803ba6-6e42-4aac-a91a-c5d155c262f0)

**Update Window:**

![Screenshot 2024-06-03 225035](https://github.com/Pratham3642/Employee-Management/assets/162919475/6e3b0e25-d1a0-447c-b3c9-b774ea2d398c)

**Delete Window:**

![Screenshot 2024-06-03 225048](https://github.com/Pratham3642/Employee-Management/assets/162919475/6fb164ca-d15a-4192-ba9e-f5179f4375f1)

**Chart :**

![Screenshot 2024-06-03 225116](https://github.com/Pratham3642/Employee-Management/assets/162919475/83842660-be31-4cbf-b7dd-fbd0f470ea58)
