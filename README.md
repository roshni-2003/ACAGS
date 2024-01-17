# ACAGS
Automatic Code Assignment Grading System

**1.1 Purpose:**
The purpose of the Automatic Code Assignment Grading System (ACAGS) is to provide instructors with a streamlined method of grading student code assignments. The system aims to reduce manual grading efforts, provide timely grades, and generate accurate grades for each assignment.

**1.2 Scope:**
The ACAGS will accept unzipped code assignments in Python. It will run predefined tests on the code to evaluate its correctness. The system will generate Grade files containing grade information for each test, as well as a grade indicating the overall assignment grade. Instructors can review and modify the grade before uploading them back to the Learning Management System (Mylearningspace).

**1.3 Definitions, acronyms, and abbreviations:**
ACAGS: Automatic Code Assignment Grading System
SRS: Software Requirements Specification
GUI: Graphical User Interface
MLS: Mylearningspace

**1.4 References:**
[1] IEEE Standard for Software Requirements Specifications. IEEE Std 830-1998.
[2] Sommerville, I. (2015). Software Engineering (10th ed.). Pearson.
[3] myLearningSpace: The university's existing Learning Management System.

**1.5 Overview:**
The remainder of this document provides a detailed description of the ACAGS, including its functionality, user characteristics, constraints, and specific requirements. It also includes use cases, sequence diagrams, state diagrams, and a prototype of the product GUI. This document serves as a reference for the design, development, and testing of the ACAGS.



**2.1 Product perspective**
The ACAGS is a standalone system designed to integrate with the university's Learning Management System (Mylearningspace). Instructors will manually download student code assignment zip files from the MLS and unzip it then upload the unzipped code files to the ACAGS. The system will then run predefined tests on the code and generate grade files. Instructors can review and modify these files before uploading them back to the MLS for students to access.

**2.2 Product functions**
The main functions of the ACAGS include:
Accepting unzipped code assignments from instructors: The system will provide a simple interface for instructors to upload unzipped code assignments. The interface will support the upload of two files: one file containing the correct answer and another file containing the student's code.
Running predefined tests on the submitted code: The system will execute a series of predefined tests on the student's code to evaluate its correctness. This includes comparing the output of the student's code with the expected output, checking for specific errors, and evaluating the efficiency of the code.
Grading the assignments based on the test results: The system will grade the assignments based on the results of the tests, primarily considering the number of passed tests. The grading scheme will be customizable to accommodate different assignment requirements.
Generating grade file : The system will generate a grade file for all students. The file will include information on whether the code passed or failed the tests. It will also include the final grade of the assignment.
Allowing instructors to download and review the grade files: The system will allow instructors to review the generated grade files before they are uploaded back to the Mylearningspace.

**2.3 User characteristics**
The primary users of the ACAGS will be course instructors who have a basic understanding of computer programming and are familiar with the use of Mylearningspace. They will use the system to automate the grading of code assignments, thereby saving time and ensuring consistency in grading. Secondary users will be students who will receive grades from the system via the MLS. They are expected to have varying levels of programming skills, from beginners to advanced.

**2.4 Constraints
**The ACAGS must operate within the university's IT infrastructure, adhering to security protocols and data privacy regulations. It should be compatible with various operating systems and browsers to ensure accessibility for all users. The system should be scalable to handle multiple assignments simultaneously, ensuring efficient grading even during peak times
2.5 Assumptions and Dependencies
The ACAGS assumes that instructors have the necessary permissions to download and upload files from the MLS. It depends on the availability and reliability of the MLS for the file transfer process. The system also assumes that instructors will provide clear assignment instructions to students and define the predefined tests to be run on the code.
