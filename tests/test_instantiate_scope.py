import pytest

from nya_scope import Scope


@pytest.fixture
def TestScope__():
	class TestScope__(Scope):
		example_value = 42

	return TestScope__


def test_instantiate_scope(TestScope__):
	with pytest.raises(TypeError):
		TestScope__()
