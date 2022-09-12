from django.db.models import Q


operators = \
    {
        "like": "contains",
        "not_like": "contains",
        "eq": "iexact",
        "not_eq": "iexact",
        "lt": "lt",
        "gt": "gt",
        "null": "isnull",
        "not_null": "isnull"
    }

negative_operators = {"not_eq", "not_like","not_in"}

like_commands = ["exact", "startswith", "endswith", "contains"]


def conjunction(qa, qb):
    return qa & qb


def disjunction(qa, qb):
    return qa | qb


def proccess_query(query):
    q = None
    logic = query.get("logic")
    if logic == "and":
        q = combine_conditions(conjunction, *query["cond"])
    if logic == "or":
        q = combine_conditions(disjunction, *query["cond"])
    return q


def combine_conditions(operator, *qs):
    print(" Conditions: ")
    print(qs)
    q_index = 1
    condition = proccess_condition(qs[0])
    while q_index < len(qs):
        sub_condition = proccess_condition(qs[q_index])
        condition = operator(condition, sub_condition)
        q_index += 1
    return condition


def proccess_condition(condition):
    print("proccessing condition: ")
    print(condition)
    print(condition.get("filter"))
    if condition.get("filter") is not None:
        return proccess_query(condition["filter"])
    operator_index = 0
    operator = operators[condition["operator"]]
    value = condition.get("value")
    if(condition["operator"] == "null"):
        value = True
    if (condition["operator"] == "not_null"):
        value = False


    if condition["operator"] == "like" or condition["operator"] == "not_like":
        print(condition["value"][0])
        print(condition["value"][-1])
        if condition["value"][0] == '%':
            value = value[1:]
            operator_index |= 1
        if condition["value"][-1] == '%':
            value = value[:-1]
            operator_index |= 2
        print(operator_index)
        operator = like_commands[operator_index]
    argument = {"__".join([condition["field"], operator]): value}
    condition_query = Q(**argument)
    if condition["operator"] in negative_operators:
        condition_query.negate()

    print(condition_query)
    return condition_query



# operators = \
#     {
#         "like": "contains",
#         "not_like": "contains",
#         "eq": "iexact",
#         "not_eq": "iexact",
#         "lt": "lt",
#         "gt": "gt",
#         "null": "isnull",
#         "not_null": "isnull"
#     }
#
# negative_operators = {"not_eq", "not_like","not_in"}
#
# like_commands = ["exact", "startswith", "endswith", "contains"]
#
#
# def conjunction(qa, qb):
#     return qa & qb
#
#
# def disjunction(qa, qb):
#     return qa | qb
#
#
# def proccess_query(query):
#     q = None
#     logic = query.get("logic")
#     if logic == "and":
#         q = combine_conditions(conjunction, *query["cond"])
#     if logic == "or":
#         q = combine_conditions(disjunction, *query["cond"])
#     return q
#
#
# def combine_conditions(operator, *qs):
#     print(" Conditions: ")
#     print(qs)
#     q_index = 1
#     condition = proccess_condition(qs[0])
#     while q_index < len(qs):
#         sub_condition = proccess_condition(qs[q_index])
#         condition = operator(condition, sub_condition)
#         q_index += 1
#     return condition
#
#
# def proccess_condition(condition):
#     print("proccessing condition: ")
#     print(condition)
#     print(condition.get("filter"))
#     if condition.get("filter") is not None:
#         return proccess_query(condition["filter"])
#     operator_index = 0
#     operator = operators[condition["operator"]]
#     value = condition.get("value")
#     if(condition["operator"] == "null"):
#         value = True
#     if (condition["operator"] == "not_null"):
#         value = False
#
#
#     if condition["operator"] == "like" or condition["operator"] == "not_like":
#         print(condition["value"][0])
#         print(condition["value"][-1])
#         if condition["value"][0] == '%':
#             value = value[1:]
#             operator_index |= 1
#         if condition["value"][-1] == '%':
#             value = value[:-1]
#             operator_index |= 2
#         print(operator_index)
#         operator = like_commands[operator_index]
#     argument = {"__".join([condition["field"], operator]): value}
#     condition_query = Q(**argument)
#     if condition["operator"] in negative_operators:
#         condition_query.negate()
#
#     print(condition_query)
#     return condition_query