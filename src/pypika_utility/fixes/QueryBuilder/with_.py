from pypika.queries import QueryBuilder, AliasedQuery


default_with_method = QueryBuilder.with_


def with_(self, selectable, name) -> "QueryBuilder":
    if isinstance(name, AliasedQuery):
        name = name.name
    return default_with_method(self, selectable, name)


QueryBuilder.with_ = with_
