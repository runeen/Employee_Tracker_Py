import json
#import employee_functions

def get_dict() -> dict:

    try:
        with open('Data/departments.json', 'r') as file:
            departments_dict = json.load(file)
    except FileNotFoundError:
        departments_dict = {
            'last_department_id': 0,
            'departments': []
        }

    return departments_dict

def update_json(departments_dict: dict) -> None:

    with open('Data/departments.json', 'w') as file:
        json.dump(departments_dict, file, indent=4)

def get_department_ID_by_name(name: str, departments_dict : dict) -> int:

    for department in departments_dict['departments']:
        if department['name'] == name:
            return department['department_id']

    return -1



def add_department(name: str, departments_dict : dict) -> int:

    if get_department_ID_by_name(name, departments_dict) != -1:
        return -1

    new_department = {
        'name': name,
        'department_id': departments_dict['last_department_id'] + 1,
        'job_titles': []
    }

    departments_dict['last_department_id'] += 1
    departments_dict['departments'].append(new_department)

    update_json(departments_dict)

    return departments_dict['last_department_id']

def remove_department_by_id(department_id: int, departments_dict: dict) -> int:

    for department in departments_dict['departments']:
        if department['department_id'] == department_id:
            remove_job_titles(department['job_titles'], department_id, departments_dict)
            departments_dict['departments'].remove(department)

        update_json(departments_dict)

        return 0

    return -1

def remove_job_titles(names: list[str], department_id : int, departments_dict: dict) -> None:
    for job in names:
        print(f'FAKE REMOVED JOB {job}')

def edit_department(department_id: int, name: str):
    pass




