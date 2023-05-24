from pypika import Field


def _field__get_item__(self, idx: int):
    assert 1 <= idx
    self.idx = idx
    return self


Field.__getitem__ = _field__get_item__


original_field_get_sql = Field.get_sql


def _field_get_sql(self, **kwargs) -> str:
    field_sql = original_field_get_sql(self, **kwargs)
    if hasattr(self, "idx"):
        return f"{field_sql}[{self.idx}]"
    return field_sql


Field.get_sql = _field_get_sql
