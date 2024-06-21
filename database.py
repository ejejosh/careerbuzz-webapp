from sqlalchemy import create_engine, MetaData, Table, select
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
