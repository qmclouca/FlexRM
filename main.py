import FlexRM

try:
    # FlexRM.example_of_beam_creation()
    FlexRM.input_beam_data()
    FlexRM.beam_creation(FlexRM.lenght_of_beam, FlexRM.start_point)

except NameError as e:
    print("There is a problem/Ocorreu um problema: ", e)

finally:
    print("O programa foi encerrado! Obrigado por usar.")
