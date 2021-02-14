API Testing framework for functional testing of REST APIs
============================================================

Installation and how to run the tests
-------------------------------------

Please make sure you have python version greater than or equal to 3.7 installed on your system. You can install it from official python website: https://www.python.org/downloads

- Download or clone the code from the api-testing GitHub repository to your system

  https://github.com/sumansuddala/api-testing  

- Go to the directory location of downloaded or cloned code folder - "api-testing"
  
  ```python
   cd api-testing
   ```
- Run the following command to install the dependencies listed in requirements.txt

  ```python
  pip3 install -r requirements.txt
  ```
-
- New test cases can be added to the folder "tests".
- Run the following command to run the test cases written under the "tests" folder
Syntax:
  ```python
  python main.py servicename(Sheetname) organization emailid
  ```
Example:
  ```python
  python main.py TIME_SERIES_DAILY deshaw ssuman.testengineer@gmail.com
  ```

You can go through the folder structure of the api-testing module to get familier with testing framework.

