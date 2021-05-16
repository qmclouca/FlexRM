from symbeam import *
# L = lenght, E = Young Modulus, I = Inertia Modulus
from sympy.abc import L, E, I
import sympy
import matplotlib.pyplot as plt


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
    global new_beam 
    new_beam = beam(L)

    new_beam.set_young(0, L / 2, E)  # set Young Modulus on first segment
    print("Módulo de Young do primeiro segmento foi definido corretamente")
    new_beam.set_young(L / 2, L, E / 10)  # set Young Modulus on second segment
    print("Módulo de Young do segundo segmento foi definido corretamente")

    new_beam.set_inertia(0, L / 2, I)  # set Inertia Moment on first segment
    print("Momento de inércia do primeiro segmento foi definido corretamente")
    new_beam.set_inertia(L / 2, L, I / 2)  # set Inertia Moment on second segment
    print("Momento de inércia do segundo segmento foi definido corretamente")

def example_of_adding_supports():
    """
    The beam must be connected to the exterior via a given number of supports,
    which materialise the geometric boundary conditions of the problem.
    Currently, SymBeam can only solve statically determinate beams, therefore,
    redundant supports cannot be handled. Supports can be added to the beam by
    specifying the coordinate and the type of support. Exemplarily, this is
    accomplished by calling the method add_support()

    The types of support available in SymBeam are:
    roller : a roller, fixed in the transverse direction and allows rotations in the bending plane
    pin : a pinned support, fixed in the axial and transverse directions and allows rotations in the bending plane
    fixed : a fixed/clamped support, all degrees of freedom are constrained (no displacements and no rotation)
    hinge : allows distinct rotations on the left and right of the point, but does not fix the beam in any direction

    new_beam.add_support(x_coord, type)
    """
    new_beam.add_support(0, 'fixed')
    new_beam.add_support(L, 'roller')
    new_beam.add_support(3*L/4, 'hinge')

def example_of_adding_loads():
    """
    The applied external loads are the missing item for completely defining
    the beam bending problem. These can be point-type, namely, transverse point
    loads/forces and moments, and segment-type loads, this is, transverse forces
    distributed along the span of the beam. Point loads and moments are incorporated
    by calling the add_point_load() and add_point_moment() methods, which receive
    the coordinate of the point and the value of the load. Distributed loads are
    applied by calling the add_distributed_load() method, which takes the starting
    and ending point of the distributed load and the associated expression.
    """
    new_beam.add_point_load(3 * L / 4, -10)  #P = -10
    new_beam.add_point_load(3 * L / 7, -20)
    new_beam.add_point_moment(L, 10) #M = 10
    new_beam.add_distributed_load(0, L / 2, -2 * 2) #q = -2 x= 2

def example_of_solving():
    """
    After specifying the beam properties, supports and loads, the problem
    can be solved by calling the method solve(). The program will proceed as follows
    check if the input data is consistent define the individual beam segments,
    such that each one is associated with a continuous function of the Young modulus,
    second moment of area and distributed load: in sum, this subdivision must guarantee
    that the shear force and bending moment diagrams are continuous in each segment
    and piecewise continuous along the span of the beam solve for the reaction forces
    and moments of the supports (equilibrium equations) solve for the internal loads
    (integrate the differential equations for beam equilibrium) solve for the deflections
    (integrate the elastic curve equation) output the results (can be suppressed if
    the optional argument output=False): identified segments, exterior reactions,
    shear force, bending moment, slope and deflection for each beam segment. For the
    current example, the output shall be as follows. The results can be plotted with
    matplotlib by calling the method plot on the beam object. The produced figure contains
    a schematic representation of the problem the shear force diagram the bending moment
    diagram the deformed shape of the beam. At this stage, to be able to plot the
    expressions, all the parameters of the problem must be substituted by numerical
    values, with the natural exception of the x variable, since this is the independent
    variable. This is can be accomplished by passing the optional argument subs to
    the plot method. This must be a dictionary whose keys are the string representations
    of the variables and the values are the effective numerical values. Example
    substitutions L=2, P=1000, q=5000 and M=1000.
    """
    new_beam.solve()
    new_beam.plot(subs={'P': 1000, 'q': 5000, 'L': 5, 'M': 1000})
    plt.savefig("beam.pdf")