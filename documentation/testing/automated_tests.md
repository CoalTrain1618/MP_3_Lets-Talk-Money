# Automated Testing Document

## Introduction
For this project, I wanted to use Test Driven Development (TDD) to make sure my code works as expected and is easy to maintain. TDD means writing tests before writing the actual code, which helps me think about what each part of the project should do from the start.

Using TDD and automated tests brings a lot of benefits: 
- I can spot mistakes early, before they become bigger problems.
- It’s easier to change or improve my code later, because the tests will catch anything that breaks.
- I spend less time manually checking if things work, since the tests do it for me.
- My project is more reliable and ready for future updates.


### Finances app - Testing Models
I wrote unit tests for all the main models in my finance app, including Budget, Income, Category, and Expenses. These tests check that each model can be created correctly, that relationships between models (like linking an income to a budget or an expense to a category) work as expected, and that the right data is stored in the database.

After running the tests with `python manage.py test finances`, all tests passed successfully. This gives me confidence that the core parts of my app are working as intended and that future changes can be made safely, knowing that the tests will catch any major issues.

## Finance app - Testing Views

### Initial Test - BudgetView
I want the user to go to the budget_form.html, input amount, month and year. I want them to only see their budget. Upon sumbission, they get redirected, maybe back to dashboard, where the list will be, and a success message.

Test Outcome: Failure 

Expected Outcomes:
- Only logged-in users can access the budget creation page.
- The for display for a GET request.
- Submitting valid data creates a new Budget for the logged in user.
- The user is redirected to the dashboard after submission.
- A success message is displayed.

#### Test 1 Outcomes:
##### During the test, three errors were produced. 
- TemplateDoesNotExist: 
    - The template finances/budget_form.html could not be found, causing the test to fail. 
- NoReverseMatch: 
    - The url pattern named 'dashboard' could not be found.
- Dependant test failure:
    - Since two test failed, the proceeding failed.

##### Remedial Work: 
- Create budget_form.html template.
    - This way totally missed prior to origianl test.
- Create Dashboard template, add url and create simple render view.
    - I wans't plannig to create the dashboard this early originally, but I clearly overlooked that it would be needed during testing. 

#### Test 2 Outcome: 
##### During this test, one error was found. 
- ImportError:
    - Django could not import 'h'

##### Remedial Work: 
- I traced back to where the error was found in views.py
    - Small typo in the import, I typed a h and commited. This is now removed. 

#### Test 3 Outcome:
##### During test 3, Two errors were found:
- TemplateDoesNotExist
    - I believe the file structure is making an error.

##### Remidial Work:
- I removed budget_form to finances/templates and deleted /finances/templates/budget_form dir ready for test 4.

#### Test 4 Outcome:
##### During test 4, the saem errors were recorded.
- TemplateDoesNotExist

##### Remidial work:
This time I decided to move both templates into a finance folder, within templates dir. 

#### Test 5 Outcome:
##### During test 5, test passed
- Yay !!


### IncomeView testing
IncomeView was designed using the base of budgetView.

Income view will allow logged in user to record an income using a form. The form will be it's own page income_form.html. The form will use the Income model and contain the following fields ['amount', 'source', 'budget selection']. 

I will need to create a view and urls pattern to link this up. The view will be designed to ensure the logged in user can only access their own data. Upon successful submit, the user will be ported back to dashboard and should be able to see a success message. 

Initial test: Fail

Created view to requirments. Developed testcases to test income creation functionality. 

#### Expected outcomes:
- Authorised user can input Income into form field
- User can submit Income data and it will post the data to DB Income table

#### Test One: 
