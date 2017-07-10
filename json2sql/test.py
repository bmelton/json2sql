import json
from apps.facts.jsonsql import convert_operator, query1, query2, query3

def process_where(where):
    data_type = None
    operator1 = None
    operator2 = None
    value1 = None
    value2 = None
    attribute = None

    try:
        attribute = where["attribute"]
        where.pop("attribute")
    except Exception, e:
        raise ValueError("You must provide an attribute that relates to the column we should attempt to query")

    try:
        value1 = where["value1"]
        where.pop("value1")
    except Exception, e:
        raise ValueEerror("You must provide a value1 that relates to the value we should attempt to query")

    try:
        data_type = where["type"]
        where.pop("type")
    except Exception, e:
        raise ValueError("You must provide a column type of either 'string', 'integer', or 'date'")

    try:
        operator1 = where["operator1"]
        where.pop("operator1")
    except Exception, e:
        raise ValueError("Comparison operator is missing, and is required.")

    try:
        operator2 = where["operator2"]
        where.pop("operator2")
    except Exception, e:
        # Second comparison operator is optional
        pass

    operator1 = convert_operator(operator1, data_type)

    WHERE = ""
    # WHERE += "name='{}'".format(attribute)
    if data_type == "integer":
        WHERE += "`{}`{}{}".format(attribute, operator1, value1)
    if data_type == "string":
        WHERE += "`{}`{}'{}'".format(attribute, operator1, value1)

    return WHERE

def process_json(query):
    data = {}

    try:
        data = json.loads(query)
    except Exception, e:
        data = query


    select = data["select"]
    from_data = data["from"]
    where = data["where"]
    query = ""

    # Need to process lists and dicts separately.  Lists should contain
    # dict objects though. 
    if isinstance(where, list):
        iter_rows = iter(where)
        # select += process_where(iter_rows[0])
        first = next(iter_rows)

        query += "({})".format(process_where(first))
        for row in iter_rows:
            query += " AND ({})".format(process_where(row))
            # select += process_where(row)

    if isinstance(where, dict):
        query += process_where(where)

    output = "SELECT {} FROM `{}` WHERE {}".format(select, from_data, query)
    return output
