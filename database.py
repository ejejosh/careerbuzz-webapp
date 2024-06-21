from sqlalchemy import create_engine, MetaData, Table, select, text
from dotenv import load_dotenv, dotenv_values
import os


load_dotenv()

db_connection_string = os.getenv("DB_CONNECTION_STRING")

engine = create_engine(db_connection_string)
metadata = MetaData()
table = Table('jobs', metadata, autoload_with=engine)


# Create a connection
def load_jobs_from_db():
    with engine.connect() as connection:
        # Execute a select statement
        stmt = select(table)
        result = connection.execute(stmt)

        # Fetch all rows and convert each to a dictionary
        rows = result.fetchall()
        rows_dicts = [dict(row._mapping) for row in rows]

        jobs = []

        # Append the list of dictionaries to jobs lists
        for row_dict in rows_dicts:
            jobs.append(row_dict)

        return jobs


def load_job_from_db(id):
    # Define your raw SQL query
    sql_query = text("SELECT * FROM jobs WHERE id = :job_id")

    # Create a connection and execute the SQL query
    with engine.connect() as connection:
        result = connection.execute(sql_query, {'job_id': id})

        # Fetch a single row
        row = result.fetchone()

        if row:
            # Convert the row to a dictionary
            row_dict = dict(row._mapping)

            # Print the dictionary
            return row_dict
        else:
            return None
