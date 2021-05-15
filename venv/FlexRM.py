from symbeam import *
# L = lenght, E = Young Modulus, I = Inertia Modulus
from sympy.abc import L, E, I
import sympy


def input_beam_data():
    global lenght_of_beam, young_modulus, inertia_modulus, start_point
    lenght_of_beam = input("Entre o comprimento, em metros, da viga.\n")
    start_point = input("Entre o ponto inicial da viga, em metros.\n")
    young_modulus = input("Entre o módulo de Young do material da viga.\n")
    inertia_modulus = input("Entre o módulo de inércia da viga.\n")
    return lenght_of_beam, young_modulus, inertia_modulus


def beam_creation(lenght_of_beam, start_point):
    work_beam = beam(lenght_of_beam, x0=start_point)
    print(f'work_beam criada em: {work_beam}')


def definition_of_beam_properties():
    work_beam.set_young(0, L / 2, E)  # set Young Modulus on first segment
    work_beam.set_young(L / 2, L, E / 10)  # set Young Modulus on second segment

    work_beam.set_inertia(0, L / 2, I)  # set Inertia Moment on first segment
    work_beam.set_inertia(L / 2, L, I / 2)  # set Inertia Moment on second segment


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


def example_of_definition_of_beam_properties():
    """
    Nesta seção são definidos o módulo de Young e o
    Momento de Inércia (Second moment of area)
    A beam must be associated with some distribution of material
    properties and section geometry along its length, namely,
    the Young modulus of the material and the second moment
    of area of the section. While these are not required for
    finding the bending diagrams, as these results simply from
    equilibrium considerations, they are mandatory for computing
    the deflections of the beam.
    In SymBeam, these properties can be set in individual segments
    along the beam, such that the set of segments for each property
    must encompass all the beam span and not be overlapping
    at any region. For example, consider a beam of length L,
    the Young modulus and second moment of area are set by passing
    the starting and ending coordinate and the value to the methods
    set_young() and set_inertia() as follows

    new_beam.set_young(x_start, x_end, value)

    new_beam.set_inertia(x_start, x_end, value)
    """
    new_beam = beam(L)

    new_beam.set_young(0, L / 2, E)  # set Young Modulus on first segment
    new_beam.set_young(L / 2, L, E / 10)  # set Young Modulus on second segment

    new_beam.set_inertia(0, L / 2, I)  # set Inertia Moment on first segment
    new_beam.set_inertia(L / 2, L, I / 2)  # set Inertia Moment on second segment