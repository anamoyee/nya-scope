from nya_scope import Scope


def test_access_field():
	class ExampleScope__(Scope):
		example_value = 42

	assert ExampleScope__.example_value == 42


def test_access_field_multilevel():
	class ExampleScope__(Scope):
		class Inner__(Scope):
			example_value = 42

	assert ExampleScope__.Inner__.example_value == 42
