## Home task. Working with Files and Modular System

#### Task Description

**Task 1**

Your task is to develop a function **`total_salary(path)`** that analyzes a text file containing information about monthly salaries of developers in your company. Each line in the file contains the developer's last name and their salary, separated by a comma without spaces.

For example:

```
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```

**Requirements for the task:**

- The **`total_salary(path)`** function should take one argument - the path to the text file **`(path)`**.
- The file contains data about the salaries of developers, separated by commas. Each line indicates one developer.
- The function should analyze the file, calculate the total and average sum of salaries.
- The function's output is a tuple of two numbers: the total sum of salaries and the average salary.

**Recommendations for execution:**

1. Use the context manager with for reading files.
2. Remember to set the encoding when opening files.
3. You can use the split(',') method to split the data in each line.
4. Calculate the total sum of salaries first, and then divide it by the number of developers to get the average salary.
5. Handle possible exceptions when working with files, such as the absence of a file.

> [!TIP]
> Example of using the function:
>
> ```
> total, average = total_salary("path/to/salary_file.txt")
> print(f"Total salary sum: {total}, Average salary: {average}")
> ```
>
> Expected output:
>
> ```
> Total salary sum: 6000, Average salary: 2000
> ```

**Task 2**

You're tasked with developing a function called **`get_cats_info(path)`** that reads a text file containing information about cats and returns a list of dictionaries with information about each cat.

```
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
```

**Requirements for the task:**

- The **`get_cats_info(path)`** function should take one argument - the path to the text file **`(path)`**.
- The file contains data about cats, where each record contains a unique identifier, the cat's name, and its age.
- The function should return a list of dictionaries, where each dictionary contains information about one cat.

**Recommendations for execution:**

1. Use **`with`** for safe file reading.
2. Remember to set the encoding when opening files.
3. For each line in the file, use **`split(',')`** to extract the identifier, name, and age of the cat.
4. Create a dictionary with keys `"id"`, `"name"`, `"age"` for each cat and add it to the list to be returned.
5. Handle possible exceptions related to file reading.

> [!TIP]
> Example usage of the function:
>
> ```
> cats_info = get_cats_info("path/to/cats_file.txt")
> print(cats_info)
> ```
>
> Expected result:
>
> ```
> [
>     {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
>     {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
>     {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
>     {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
>     {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
> ]
> ```

**Task 3**

Develop a script that takes a directory path as a command line argument and visualizes the structure of this directory by displaying the names of all subdirectories and files. For better visual perception, directory and file names should be displayed in different colors.

**Requirements for the task:**

- Create a Python virtual environment to isolate the project's dependencies.
- The script should receive the directory path as an argument when executed. This path specifies where the directory whose structure needs to be displayed is located.
- Use the **`colorama`** library to implement colored output.
- The script should correctly display both directory and file names using a recursive method of traversing directories (you can use a non-recursive method if desired).
- Error checking and handling should be implemented, such as if the specified path does not exist or does not lead to a directory.

**Recommendations for execution:**

1. First, install the `colorama` library. To do this, create and activate a Python virtual environment, and then install the package using **`pip`**.
2. Use the **`sys`** module to obtain the directory path as a command line argument.
3. Use the **`pathlib`** module to work with the file system.
4. Ensure proper formatting of the output using **`colorama`** functions.

> [!TIP]
>
> Example usage:
> If you execute the script and pass an absolute path to the directory as a parameter.
>
> ```
> python hw03.py /path/to/your/directory
> ```
>
> This will result in the script printing a list of all subdirectories and files in the specified directory to the terminal using different colors for directories and files, facilitating visual perception of the file structure.
>
> For a directory with the following structure:
>
> ```
> 📦picture
> ┣ 📂Logo
> ┃ ┣ 📜IBM+Logo.png
> ┃ ┣ 📜ibm.svg
> ┃ ┗ 📜logo-tm.png
> ┣ 📜bot-icon.png
> ┗ 📜mongodb.jpg
> ```
>
> The script should output a similar structure.
> ![structure example]

**Task 4**

Write a console assistant bot that recognizes commands entered from the keyboard and responds accordingly to the entered command.

> 👆 The assistant bot should become a prototype for the assistant application we will
> develop in the next homework assignments. The assistant application initially should be
> able to work with a contact book and calendar.

In this homework, we will focus on the interface of the bot itself. The simplest and most convenient interface at the initial stage of development is a Command Line Interface (CLI). A CLI is relatively easy to implement.

Any CLI consists of three main elements:\

**Command parser**. This part is responsible for parsing the strings entered by the user, extracting keywords and command modifiers from the string.\
**Command handler functions** - a set of functions, also called `handler`, responsible for directly executing commands.\
**Request-response loop**. This part of the application is responsible for receiving data from the user and returning responses from the `handler` functions.

In the first stage, our assistant bot should be able to store names and phone numbers, find a phone number by name, change the stored phone number, and output all saved records to the console. To implement such simple logic, we will use a dictionary. We will store the user's name as the key and the phone number as the value.

**Requirements for the task:**

- The program should have a **`main()`** function that manages the main command processing loop.
- Implement the **`parse_input()`** function, which will parse the string entered by the user into a command and its arguments. Commands and arguments should be recognized regardless of input case.
- Your program should expect user input commands and process them using the appropriate functions. If the user enters the command **`"exit"`** or **`"close"`**, the program should terminate.
- Write handler functions for various commands, such as **`add_contact()`**, **`change_contact()`**, **`show_phone()`**, etc.
- Use a Python dictionary to store names and phone numbers. The name will be the key, and the phone number will be the value.
- Your program should be able to identify and report incorrectly entered commands.
