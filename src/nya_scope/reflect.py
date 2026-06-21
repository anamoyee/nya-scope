from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

from ._impl import Scope

if TYPE_CHECKING:
	import builtins

T = TypeVar("T")


def to_keys(Scope: type[Scope]) -> tuple[str, ...]:
	return tuple(
		key
		for key in Scope.__dict__
		if key
		not in {
			"__module__",
			"__doc__",
		}
	)


def to_values(Scope: type[Scope]) -> tuple[T, ...]:
	return tuple(
		getattr(Scope, key)
		for key in to_keys(Scope)
		if key
		not in {
			"__module__",
			"__doc__",
		}
	)


def to_dict(Scope: type[Scope]) -> builtins.dict[str, T]:
	return {
		key: getattr(Scope, key)  # this prevents mismatch between __dict__'s version and the received version as if dot-accessed.
		for key in to_keys(Scope)
		if key
		not in {
			"__module__",
			"__doc__",
		}
	}


def _is_scope_subclass(item: Any) -> bool:
	try:
		return isinstance(item, type) and issubclass(item, Scope)
	except Exception:
		return False


def to_dict_recursive(
	Scope: type[Scope],
	*,
	include_explored_scopes: bool = False,
) -> builtins.dict[str, Any]:
	res: builtins.dict[str, Any] = {}
	for key in to_keys(Scope):
		value = getattr(Scope, key)
		if _is_scope_subclass(value):
			if include_explored_scopes:
				res[key] = value
			for sub_key, sub_val in to_dict_recursive(
				value,
				include_explored_scopes=include_explored_scopes,
			).items():
				res[f"{key}.{sub_key}"] = sub_val
		else:
			res[key] = value
	return res


def to_keys_recursive(
	Scope: type[Scope],
	*,
	include_explored_scopes: bool = False,
) -> tuple[str, ...]:
	return tuple(
		to_dict_recursive(
			Scope,
			include_explored_scopes=include_explored_scopes,
		).keys()
	)


def to_values_recursive(
	Scope: type[Scope],
	*,
	include_explored_scopes: bool = False,
) -> tuple[Any, ...]:
	return tuple(
		to_dict_recursive(
			Scope,
			include_explored_scopes=include_explored_scopes,
		).values()
	)
