import Model.department_job_title_functions as deptModel

departments_dictionary = deptModel.get_dict()
deptModel.remove_department_by_id(4, departments_dictionary)
