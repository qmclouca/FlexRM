from symbeam import *
# L = lenght, E = Young Modulus, I = Inertia Modulus
from sympy.abc import L, E, I
import sympy

def input_beam_data():
    global lenght_of_beam, young_modulus, inertia_modulus, start_point
    lenght_of_beam = input("Entre o comprimento, em metros, da viga.")
    start_point = input("Entre o ponto inicial da viga, em metros.")
    young_modulus = input("Entre o módulo de Young do material da viga.")
    inertia_modulus = input("Entre o módulo de inércia da viga.")
    return lenght_of_beam, young_modulus, inertia_modulus

def example_of_beam_creation():
    print("Criando uma viga / Creating a beam")
    # métodos para criar vigas
    # método 1 (numeric input):
    beam_1 = beam(1, x0=0) # comprimento = 1   a viga inicia em 0
    print(f'Viga 1 criada em: {beam_1}')
    # método 2 (numeric input):
    beam_2 = beam(1) # comprimento = 1     a viga tem o início omitido
    print(f'Viga 2 criada em: {beam_2}')
    # método 3 (numeric input from string):
    beam_3 = beam("1") # comprimento = 1     a viga tem o início omitido
    print(f'Viga 3 criada em: {beam_3}')
    # método 4 (Symbolic input from a symbolic variable created with SymPy):
    L = sympy.symbols("L")
    beam_4 = beam(L)
    print(f'Viga 4 criada em: {beam_4}')
    # método 5 (Symbolic input from a symbolic variable provided by SymPy):
    beam_5 = beam(L)
    print(f'Viga 5 criada em: {beam_5}')

def beam_creation(lenght_of_beam, start_point):
    work_beam = beam(lenght_of_beam, x0=start_point)
    print(f'work_beam criada em: {work_beam}')

def example_of_definition_of_beam_properties():
    # Nesta seção são definidos o módulo de Young e o Momento de Inércia (Second moment of area)
    return 0
    
