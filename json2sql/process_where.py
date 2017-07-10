import json
from json2sql import convert_operator

# TODO - Implement table name attribute.  Must be here to do joins
# TODO - Implement comparison2, value2
def process_where(where, table=None):
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
        raise ValueError("You must provide a value1 that relates to the value we should attempt to query")

    try:
        data_type = where["type"]
        where.pop("type")
    except Exception, e:
        raise ValueError("You must provide a column type")

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

    # TODO - This feels janky.
    try:
        value2 = where["value2"]
        where.pop("value2")
    except Exception, e:
        pass

    operator1 = convert_operator.convert_operator(operator1, data_type)
    WHERE = ""

    if data_type == "integer":
        if table:
            WHERE += "`{}`.`{}`{}{}".format(table, attribute, operator1, value1)
        else:
            WHERE += "`{}`{}{}".format(attribute, operator1, value1)

    if data_type == "string" or data_type == "CharField":
        if table:
            WHERE += "`{}`.`{}`{}'{}'".format(table, attribute, operator1, value1)
        else:
            WHERE += "`{}`{}'{}'".format(attribute, operator1, value1)

    if data_type == "boolean":
        if table:
            WHERE += "`{}`.`{}`{}{}".format(table, attribute, operator1, value1)
        else:
            WHERE += "`{}`{}{}".format(attribute, operator1, value1)

    if data_type == "date":
        if operator1 == "between":
            if table:
                WHERE += "`{}`.`{}` {} '{}' AND '{}'".format(table, attribute, operator1, value1, value2)
            else:
                # TODO - Missing something here, but it works anyway. :-\
                WHERE += "`{}` {} '{}' AND '{}'".format(attribute, operator1, value1, value2)
        else:
            if table:
                WHERE += "`{}`.`{}` {} '{}'".format(table, attribute, operator1, value1)
            else:
                # TODO - Missing something here, but it works anyway. :-\
                WHERE += "`{}` {} '{}'".format(attribute, operator1, value1)

    if data_type == "datetime":
        if operator1 == "between":
            if table:
                WHERE += "`{}`.`{}` {} '{}' AND '{}'".format(table, attribute, operator1, value1, value2)
            else:
                # TODO - Missing something here, but it works anyway. :-\
                WHERE += "`{}` {} '{}' AND '{}'".format(attribute, operator1, value1, value2)
        else:
            if table:
                WHERE += "`{}`.`{}` {} '{}'".format(table, attribute, operator1, value1)
            else:
                # TODO - Missing something here, but it works anyway. :-\
                WHERE += "`{}` {} '{}'".format(attribute, operator1, value1)

    return WHERE
