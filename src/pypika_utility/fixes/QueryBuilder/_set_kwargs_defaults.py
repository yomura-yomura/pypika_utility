from pypika.queries import QueryBuilder


default_set_kwargs_defaults_method = QueryBuilder._set_kwargs_defaults


def _set_kwargs_defaults(self, kwargs: dict) -> None:
    default_set_kwargs_defaults_method(self, kwargs)
    kwargs.setdefault("groupby_alias", False)


QueryBuilder._set_kwargs_defaults = _set_kwargs_defaults
