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