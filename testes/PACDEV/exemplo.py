import pytest

from myapp.mymodule.funcoes import *


@pytest.mark.easy_operation
def test_add():
    #  Essa funcao deve ser usada para soma, recebe 2 parametros (int,int) e tem como retorno o resultado da soma
    assert add(4, 8) == 14

@pytest.mark.easy_operation
def test_subtract():
    #  Essa funcao deve ser usada para subtracao, recebe 2 parametros (int,int) e tem como retorno o resultado da subtracao
    assert subtract(3, 6) == -3

@pytest.mark.difficult_operation
def test_multiply():
    #  Essa funcao deve ser usada para multiplicao, recebe 2 parametros (int,int) e tem como retorno o resultado da multiplicao deles
    assert multiply(4, 5) == 20

@pytest.mark.difficult_operation
def test_divide():
    #  Essa funcao deve ser usada para divisao, recebe 2 parametros (int,int) e tem como retorno o resultado da soma
    assert divide(56, 8) == 7
