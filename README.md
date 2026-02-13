## nya-scope (import name: `nya_scope`)

Small helper library for creating named scopes/inline modules
Classes marked explicitly as scopes prevent intialization with a runtime error

### Style Guide (optional)

You are free to adopt it in full, part, or not for your for your project, this is just what I found the most convenient for my projects for visual clarity & separation from other (regular) classes.

1. Append `__` after every name of classes that inherit from `Scope`:
	```python
	class ExampleScope__(Scope):
		example_field = 42
	```
2. Manually mark all methods as either `@staticmethod` (and always provide full absolute path) or `@classmethod`
	```python
	class Outer__(Scope):
		class Inner__(Scope):
			value = 42

			@classmethod
			def class_method(here):  # noqa: N804 <-- if using ruff
				# name your `cls`, `here` instead - it makes sense in this context
				_ = here.value

			@staticmethod
			def static_method():
				_ = Outer__.Inner__.value  # Inner__.value does not work
	```
