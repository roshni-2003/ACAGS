import os
import zipfile
import subprocess
import csv

def parse_teacher_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    output_dict = {}
    for line in lines:
        function, result = line.strip().split(':')
        output_dict[function] = result
    return output_dict

def grade_students(zipfile_name, teacher_dict):
    with zipfile.ZipFile(zipfile_name, 'r') as zip_ref:
        zip_ref.extractall('student_scripts')
    student_grades = {}
    for filename in os.listdir('student_scripts'):
        if filename.endswith('.py'):
            student_number = filename.split('.')[0]
            with open(f'student_scripts/{filename}', 'r') as f:
                script = f.read()
            grade = 0
            for function, expected_result in teacher_dict.items():
                try:
                    result = subprocess.check_output(['python', '-c', f'{script}\nprint({function})'], universal_newlines=True)
                    if str(result.strip()) == str(expected_result):
                        grade += 1
                except subprocess.CalledProcessError:
                    pass
            student_grades[student_number] = grade
    return student_grades

def export_grades_to_csv(grades_dict, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Student Number", "Grade"])
        for student, grade in grades_dict.items():
            writer.writerow([student, grade])
