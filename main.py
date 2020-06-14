import yaml
import argparse

from termcolor import colored

def read_file():
    global data
    data = """from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
"""
    with open('forms.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        forms = yaml.load(file, Loader=yaml.FullLoader)

        for a in range(len(forms)):
            for b in (forms[a]):
                form_name = b
                if form_name == "Register":
                    import sqlite3
                    conn = sqlite3.connect("db.sqlite3")
                    db = conn.cursor()
                    try:
                        db.execute("CREATE TABLE users (user_id INTEGER PRIMARY KEY AUTOINCREMENT);")
                    except Exception as e:
                        print(colored(f"WARNING: {e} has occured, skipping...", "yellow"))
                    conn.commit()

                # data += form_name
                string = f"\nclass {form_name}(FlaskForm):"
                data += string
                for c in (forms[a][b]):
                    for d in c:
                        # StringField('name', validators=[DataRequired()])
                        column_name = d
                        column_data = c[d][0]
                        if column_data == "text":
                            data += f"\n\t{column_name} = StringField('{column_name}', validators=[DataRequired()])"
                        elif column_data == "password":
                            data += f"\n\t{column_name} = PasswordField('{column_name}', validators=[DataRequired()])"
                        elif column_data == "textarea":
                            data += f"\n\t{column_name} = TextAreaField('{column_name}', validators=[DataRequired()])"

                        if form_name == "Register":
                            try:
                                db.execute(f"ALTER TABLE users ADD {column_name} TEXT;")
                            except Exception as e:
                                print(colored(f"WARNING: {e} has occured, skipping...", "yellow"))
                            conn.commit()

                data += f"\n\tsubmit = SubmitField('submit', validators=[DataRequired()])\n"


# print(forms_arr)
def write_file():
    with open("forms.py", "w") as file:
        file.write(data)

def main():
    parser = argparse.ArgumentParser(prog="Flask-Automate")
    # parser.add_argument("write")
    args = parser.parse_args()
    read_file()
    write_file()

