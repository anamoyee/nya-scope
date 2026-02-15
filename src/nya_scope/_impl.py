from typing import Never


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
	def __new__(cls):
		raise TypeError(...)  # to appease the type checkers
