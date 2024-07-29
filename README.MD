# Research MetaData - Test

### Prerequisites

Make sure you have Python 3.8 or newer and pip installed. You'll also need Django, which can be installed via pip.

### Installation

1. **Create environment and install requirements:**
    - Environment creation:
         ```shell
         python3 -m venv .venv
         ```
    - Environment activation (Unix/macOS):
         ```shell
         source .venv/bin/activate
         ```
    - Environment activation (Windows):
         ```shell
         .venv\Scripts\activate
         ```
    - Install requirements:
         ```shell
         pip install ./requirements.txt
         ```

2. **Set Up the Secret Key:**
    - Generate a new secret key for Django. You can use an online tool like [Djecrety](https://djecrety.ir/) to generate
      it.
    - Store your secret key in a `.env` file at the root of your project. It should look something like this:
      ```
      SECRET_KEY=your_secret_key_here
      ```

3. **Database Setup:**
    - Navigate to your project directory and run the following commands to set up your database:
      ```shell
      python manage.py makemigrations
      python manage.py migrate
      ```

4. **Create an Admin User:**
    - Set up a superuser for the admin panel by running:
      ```shell
      python manage.py createsuperuser
      ```
    - Follow the prompts to create the user.

5. **Import SQL Test Data (Optional):**
    - If you have pre-defined SQL data, import it into your newly created `.sqlite3` database file from
      the `meta_form/sql_test` directory. Alternatively, you can manually add data via the Django admin panel.

## Running the Project

1. **Start the Server:**
    - Run the following command to start the Django development server:
      ```shell
      python manage.py runserver
      ```

2. **Access the Application:**
    - The server will typically start at http://127.0.0.1:8000. You can access the application through the following
      URLs:
        - **/form** - This page allows you to add, view, and download research metadata.
        - **/admin** - Access the Django admin panel to manage the application, including database entries.


## Test project

### Database dump setup (Optional)

Before running the tests, you can create a database dump of the relevant models using the following command:

```shell
python -Xutf8 .\manage.py dumpdata meta_form.<model_name> -o meta_form/fixtures/pluggy_server_<model_name_lower_camel_case>.json
```

Replace <model_name> with the actual name of your model and <model_name_lower_camel_case> with the camel case version 
of the model name. For example, if your model is ResearchMetadata, the command would be:

```shell
python -Xutf8 .\manage.py dumpdata meta_form.ResearchMetadata -o meta_form/fixtures/pluggy_server_research_metadata.json
```

**MetaForm project have already had necessary dumps in *./meta_form/fixtures/* folder.** Please do additional dumps 
only if you extend current tests and models

### Running tests

Once the database dump is prepared, you can run the tests using the following command:

```shell
python manage.py test meta_form
```

This command will execute all the tests defined in the meta_form application. The test results will be displayed in 
the console, showing which tests passed, failed, or encountered errors.

