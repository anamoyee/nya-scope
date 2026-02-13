import pytest
from nya_scope import Scope


def test_instantiate_scope():
	class ExampleScope__(Scope):
		example_value = 42

	with pytest.raises(TypeError):
		ExampleScope__()
