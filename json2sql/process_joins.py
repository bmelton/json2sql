import json
import process_where
from finalize_where import finalize_where

def process_joins(join_query):
    output_string = ""

    where_clauses = []

    try:
        join_type = join_query["type"]
        join_query.pop("type")
    except Exception, e:
        raise ValueError("Generic Error - Barry will fix this.")

    try:
        local_table = join_query["local_table"]
        join_query.pop("local_table")
    except Exception, e:
        raise ValueError("Generic Error - Barry will fix this.")

    try:
        local_column = join_query["local_column"]
        join_query.pop("local_column")
    except Exception, e:
        raise ValueError("Generic Error - Barry will fix this.")

    try:
        join_table = join_query["join_table"]
        join_query.pop("join_table")
    except Exception, e:
        raise ValueError("Generic Error - Barry will fix this.")

    try:
        join_column = join_query["join_column"]
        join_query.pop("join_column")
    except Exception, e:
        raise ValueError("Generic Error - Barry will fix this.")

    try:
        where = join_query["where"]
        join_query.pop("where")
    except Exception, e:
        pass
        # raise ValueError("There's not really any point in adding a join if you aren't going to perform a 'where' against it..")

    if join_type == "inner" or join_type == "left":
        output_string += "{} JOIN `{}` ON `{}`.`{}` = `{}`.`{}`".format(
            join_type.upper(), join_table, join_table, join_column, local_table, local_column
        )

    # Set an empty query list to populate
    query = ""

    # Need to process lists and dicts separately.  Lists should contain
    # dict objects though. 

    try:
        if isinstance(where, list):
            iter_where = iter(where)
            # first = next(iter_where)

            # query += "({})".format(process_where.process_where(first, join_table))
            for clause in iter_where:
                output = process_where.process_where(clause, join_table)
                where_clauses.append(output)
                # query += " AND ({})".format(process_where.process_where(clause, join_table))

    except Exception, e:
        # Where clauses may be optional
        pass

    return ( output_string, where_clauses )
