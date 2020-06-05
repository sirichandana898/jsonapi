Title:Implementation of CRUD operations using html and Json formats.

Description:
Implementation of CRUD operations using html and Json formats.There are different url's for different actions. We can do create,read,update,delete operations in both HTML and Json formats.
If we want to do the operations using html forms,we can use the below urls,
http://127.0.0.1:8000/student_create --->create student record using html form
http://127.0.0.1:8000/display/html   --->display using html
http://127.0.0.1:8000/student_update/id --->updates respective record matching the given id
http://127.0.0.1:8000/student_delete/id --->deletes the record matching the given id

If we want in json format,we can use the below API's,
http://127.0.0.1:8000/api/studentcreate   --->for creating student entry
http://127.0.0.1:8000/api/studentmodify/id --->for update and delete operations
http://127.0.0.1:8000/display/json --->for displaying the data in Json format


Install 
Python,Django,djangorestframework to be installed.


Usage
Run the code in IDE's like pycharm and browse the urls in browser.














