from typing import TYPE_CHECKING, Never


class __NoInitMeta(type):
	def __call__(cls, *_, **__) -> Never:
		"""### ⚠️ Calling this `nya_scope.Scope`-class (e.g. to try to create a new instance) will raise a TypeError.

		- If you need to create an instance, remove the `Scope` base class from this class's definition
		- If you need to access an attribute or a static/class method, remove the calling parenthesis `()`
		"""

		e = TypeError(
			"This type doesnt support initialization; "  #
			"it is a named scope for values or (static/class)methods only."
		)

		e.add_note(
			"""

Hint: try removing the call:

  ExampleScope__().example_field
                ^^
           remove those
"""[1:-1]
		)

		raise e


class Scope(metaclass=__NoInitMeta):
	"""Create named (or annonymous via `_`) scopes for values or (static/class)methods.

	### Style Guide (optional)

	You are free to adopt it in full, part, or not for your for your project, this is just what I found the most convenient for my projects for visual clarity & separation from other (regular) classes.

	1. Use `PascalCase` (like PEP8 for classes), with a modificiation to append `__` after every name of classes that inherit from `Scope`:
		```python
			class ExampleScope__(Scope):  # Easy to know at a glance that given identifier is of type `type[Scope]`
				example_field = 42
		```
	2. Manually mark all methods as either `@staticmethod` or `@classmethod`:
		```python
			class Outer__(Scope):
				class Inner__(Scope):
					value = 42

					@classmethod  # while there could've been also a mechanism to append those `@classmethod`s or `@staticmethod`s automatically at runtime, this was deemed infeasible due to 1. conflicts with other decorators (namely: order matters), 2. typing; therefore for now until a new solution is found, either @classmethod or @staticmethod is required to be specified manually, unless you don't care about typing.
					def class_method(here):  # noqa: N804 <-- if using ruff, or disable this rule for projects using this package entirely if preferred
						# name your `cls`, `here` instead, it makes sense in this context
						print(here.value)

					@staticmethod
					def static_method():
						print(Outer__.Inner__.value)  # Inner__.value does not work
		```
	"""

	if TYPE_CHECKING:  # to appease the type checkers
		__new__: Never
