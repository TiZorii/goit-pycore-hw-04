
def total_salary(path):
    total_salary = 0
    num_of_developers = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = map(str.strip, line.split(','))
                total_salary += int(salary)
                num_of_developers += 1
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print(f"Помилка: {e}")
        return None, None
    
    average_salary = total_salary / num_of_developers if num_of_developers > 0 else 0
    return total_salary, average_salary

# Приклад використання
total, average = total_salary("\1\salery_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
