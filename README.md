## nya-scope (import name: `nya_scope`)

A small, but opinionated helper library for creating named scopes/inline modules
Classes marked explicitly as scopes prevent their own intialization with a runtime error

### Style Guide (optional)

You are free to adopt it in full, part, or not for your for your project, this is just what I found the most convenient for my projects for visual clarity & separation from other (regular) classes.

1. Use `PascalCase` (like PEP8 for classes), with a modificiation to append `__` after every name of classes that inherit from `Scope`:
	```python
	class ExampleScope__(Scope): # Easy to know at a glance that given identifier is of type `type[Scope]`
		example_field = 42
	```
2. Manually mark all methods as either `@staticmethod` or `@classmethod`:
	```python
	class Outer__(Scope):
		class Inner__(Scope):
			value = 42

			@classmethod # while there could've been also a mechanism to append those `@classmethod`s or `@staticmethod`s automatically at runtime, this was deemed infeasible due to 1. conflicts with other decorators (namely: order matters), 2. typing; therefore for now until a new solution is found, either @classmethod or @staticmethod is required to be specified manually, unless you don't care about typing.
			def class_method(here):  # noqa: N804 <-- if using ruff, or disable this rule for projects using this package entirely if preferred
				# name your `cls`, `here` instead, it makes sense in this context
				print(here.value)

			@staticmethod
			def static_method():
				print(Outer__.Inner__.value)  # Inner__.value does not work
	```
