query1 = (
    {
        "select" : "COUNT(DISTINCT(id))",
        "from": "patients_member",
        "where": [
            { "attribute": "state", "value1": "MD", "operator1": "is", "type": "string" },
            { "attribute": "zipcode", "value1": "21108", "operator1": "is", "type": "string" },
        ]
    }
)

# Query2 is the same basic one as query 1, but uses a dict 'where' instead of list.
query2 = (
    {
        "select" : "COUNT(DISTINCT(id))",
        "from": "patients_member",
        "where": {
            "attribute": "state",
            "value1": "MD",
            "operator1": "is",
            "type": "string"
        }
    }
)


query3 = (
    {
        "where": [
            {
                "name" : "age",
                "fact_integer": 36,
                "comparison": "between",
                "fact_integer2": 41,
                "comparison2": "<=",
                "fact_type": 1
            },
            {
                "name" : "age",
                "fact_integer": 31,
                "comparison": "between",
                "fact_integer2": 48,
                "comparison2": "<=",
                "fact_type": 1
            }
        ]
    }
)
