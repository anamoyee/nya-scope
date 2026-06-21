from typing import Literal

import pytest

import nya_scope
from nya_scope import Scope


@pytest.fixture
def ReflectionTestScope__():
	class ReflectionTestScope__(Scope):
		example_value = 42

		@staticmethod
		def static_method() -> Literal[42]:
			return 42

		class NestedScope__(Scope):
			nested_value = 123

		class EmptyScope__(Scope): ...

	return ReflectionTestScope__


def test_reflection_keys(ReflectionTestScope__):
	assert nya_scope.reflect.to_keys(ReflectionTestScope__) == (
		"example_value",
		"static_method",
		"NestedScope__",
		"EmptyScope__",
	)


def test_reflection_values(ReflectionTestScope__):
	assert nya_scope.reflect.to_values(ReflectionTestScope__) == (
		42,
		ReflectionTestScope__.static_method,
		ReflectionTestScope__.NestedScope__,
		ReflectionTestScope__.EmptyScope__,
	)


def test_reflection_keys_recursive(ReflectionTestScope__):
	assert nya_scope.reflect.to_keys_recursive(ReflectionTestScope__) == (
		"example_value",
		"static_method",
		"NestedScope__.nested_value",
	)


def test_reflection_keys_recursive_keep_explored(ReflectionTestScope__):
	assert nya_scope.reflect.to_keys_recursive(ReflectionTestScope__, include_explored_scopes=True) == (
		"example_value",
		"static_method",
		"NestedScope__",
		"NestedScope__.nested_value",
		"EmptyScope__",
	)


def test_reflection_values_recursive(ReflectionTestScope__):
	assert nya_scope.reflect.to_values_recursive(ReflectionTestScope__) == (
		42,
		ReflectionTestScope__.static_method,
		123,
	)


def test_reflection_values_recursive_keep_explored(ReflectionTestScope__):
	assert nya_scope.reflect.to_values_recursive(ReflectionTestScope__, include_explored_scopes=True) == (
		42,
		ReflectionTestScope__.static_method,
		ReflectionTestScope__.NestedScope__,
		123,
		ReflectionTestScope__.EmptyScope__,
	)


def test_reflection_dict_recursive(ReflectionTestScope__):
	assert nya_scope.reflect.to_dict_recursive(ReflectionTestScope__) == {
		"example_value": 42,
		"static_method": ReflectionTestScope__.static_method,
		"NestedScope__.nested_value": 123,
	}


def test_reflection_dict_recursive_keep_explored(ReflectionTestScope__):
	assert nya_scope.reflect.to_dict_recursive(ReflectionTestScope__, include_explored_scopes=True) == {
		"example_value": 42,
		"static_method": ReflectionTestScope__.static_method,
		"NestedScope__": ReflectionTestScope__.NestedScope__,
		"NestedScope__.nested_value": 123,
		"EmptyScope__": ReflectionTestScope__.EmptyScope__,
	}
