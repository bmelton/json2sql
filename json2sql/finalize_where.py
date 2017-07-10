def finalize_where(where_clauses):
    output = ""
    for i in range(len(where_clauses)):
        if i == 0:
            output += where_clauses[i]
        else:
            output += " AND {}".format(where_clauses[i])

    return output
