import sqlglot
from sqlglot import exp


def extract_schema_metadata(sql: str):
    parsed = sqlglot.parse_one(sql)

    table_name = parsed.this.this.name
    columns = []

    for column in parsed.find_all(exp.ColumnDef):
        column_name = column.this.name
        data_type = column.kind.sql()

        is_primary_key = any(
            isinstance(constraint.kind, exp.PrimaryKeyColumnConstraint)
            for constraint in column.constraints
        )

        columns.append(
            {
                "name": column_name,
                "type": data_type,
                "primary_key": is_primary_key,
            }
        )

    return {
        "table_name": table_name,
        "columns": columns,
    }


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