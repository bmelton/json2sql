def convert_operator(operator, data_type):
    if data_type == "boolean":
        if operator == "is":
            return "="

    if data_type == "string":
        if operator == "is" or operator == "is_exactly":
            return "="

        if operator == "=":
            return "="

    if data_type == "datetime":
        return operator

    if data_type == "date":
        return operator

    if data_type == "integer":
        if operator == "is":
            return "="

        if operator == "=":
            return "="

        return operator

    if data_type == "decimal":
        if operator == "is":
            return "="

        if operator == "=":
            return "="

    # If all else fails...
    return "="
