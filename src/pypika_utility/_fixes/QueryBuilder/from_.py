from pypika.queries import QueryBuilder


default_from_method = QueryBuilder.from_


def from_(self, selectable):
    ret = default_from_method(self, selectable)
    assert len(set(table._table_name for table in self._from)) == len(self._from)
    return ret


QueryBuilder.from_ = from_
