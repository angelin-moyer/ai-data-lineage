from src.parsers.schema_parser import extract_schema_metadata

sql = """
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255)
);
"""

metadata = extract_schema_metadata(sql)

print(metadata)