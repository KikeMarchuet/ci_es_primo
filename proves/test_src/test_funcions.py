import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from funcions import es_primo

def test_primo_1():
    assert es_primo(1) == False

def test_es_primo_numero_primo():
    assert es_primo(2) == True

def test_es_primo_negativo():
    assert es_primo(-10) == False

def test_es_primo_numero_primo_mayor_2():
    assert es_primo(29) == True

def test_es_primo_numero_no_primo_mayor_2():
    assert es_primo(28) == False