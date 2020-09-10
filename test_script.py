import pytest
from script import %def_name%


def test_%def_name%():
	a = 2
	assert a+1 == %def_name%(a)
