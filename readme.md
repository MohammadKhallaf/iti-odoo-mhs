
### Lab 3
#### Continue with our previously created module "hms":

- [x]  Add email field to patients' model and make sure that it is:
   - [x]  a valid and
   - [x]  unique email address
- [x]  Link patient model with customers model from CRM module by adding a new field in customers model called "
  **related_patient_id"** and show this field inside **Misc** group within sales and purchase tab
- [x]  Convert the patient's age field to be auto calculated based on birthdate
- [x]  Add a constraint on CRM customer model which prevents linking customer with email which already exists in patient
  model.
- [x]  Prevent users to delete any customer linked to a patient
- [x] Show website field in the list view for customers
- [x]  Make the Tax ID field mandatory for CRM Customers