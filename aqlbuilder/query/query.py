"""
This module contains the Query models of the ArangoQueryBuilder.

Query models represent the sub parts of an AQL query.

E.g. In the following query:

    FOR item IN items
        FILTER item.sku == "123"
        RETURN item

The query model for the item.sku == "123" part is the Query model
with the following attributes:
    {
        "operator": "EQ",
        "field": "sku",
        "target": {
            "type": "string",
            "value": "123"
        }
    }
"""


