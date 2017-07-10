import json

from process_where import process_where
from process_joins import process_joins
from finalize_where import finalize_where

def process_json(query):
    data = {}

    try:
        data = json.loads(query)
    except Exception, e:
        data = query

    select = None
    from_data = None
    where = None
    joins = None

    # Select, from, and where are required keys that must be present. 
    # We should throw an error if any of them are not present.
    select = data["select"]
    from_data = data["from"]
    where = data["where"]

    where_clauses = []
    join_statements = []
    join_clauses = []

    # Here's where things start getting complicated
    # We need to parse, process, and sort out JOINed records. 
    # Starting with INNER joins, for sanity's sake.
    try:
        joins = data["joins"]
    except Exception, e:
        pass

    # Start an empty query string to be added to by looping
    join_query = ""

    if joins:
        if isinstance(joins, list):
            iter_joins = iter(joins)
            for join_clause in iter_joins:
                join_statement, join_queries = process_joins(join_clause)
                join_statements.append(join_statement)

                for join_query in join_queries:
                    where_clauses.append(join_query)

            # TODO -- add join queries to select statement
            join_output = ""
            for statement in join_statements:
                join_output += " {} ".format(statement)

    query = ""

    # Need to process lists and dicts separately.  Lists should contain
    # dict objects though. 
    if isinstance(where, list):
        iter_where = iter(where)
        for clause in iter_where:
            output = process_where(clause, from_data)
            where_clauses.append(output)

        query += finalize_where(where_clauses)

    if isinstance(where, dict):
        query += process_where(where, from_data)


    if joins:
        output = "SELECT {} FROM `{}` {} WHERE {};".format(select, from_data, join_output, query)
    else:
        output = "SELECT {} FROM `{}` WHERE {};".format(select, from_data, query)
    return output
