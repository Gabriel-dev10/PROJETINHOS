print('Agendamento')
print('Médicos disponíveis:')
medicos = ['Gabriel', 'Lucas', 'José' , 'Chico']
result = ' | '.join(medicos)
print(result)
escolha = str(input('Escolha o medico desejado:',))
if escolha == 'Lucas':
    print('Horarios Disponiveis:')
    hr_lucas = ['9H','12H' ,'13H']
    for m1 in hr_lucas:
        print(m1)
    marcar = str(input('Selecione o horario desejado:', ))
    print(marcar, 'Seu horario foi agendado com sucesso ;)')
elif escolha == 'Gabriel':
    print('Horarios Disponiveis:')
    hr_gabriel = ['7H','14H' ,'15H']
    for med2 in hr_gabriel:
        print(med2)
    marcar = str(input('Selecione o horario desejado:', ))
    print(marcar, 'Seu horario foi agendado com sucesso ;)')
elif escolha == 'José':
    print('Horarios Disponiveis:')
    hr_José = ['5H','13H' ,'20H']
    for med3 in hr_José:
        print(med3)
    marcar = str(input('Selecione o horario desejado:', ))
    print(marcar, 'Seu horario foi agendado com sucesso ;)')
elif escolha == 'Chico':
    print('Horarios Disponiveis:')
    hr_chico = ['6H','16H' ,'19H']
    for med4 in hr_chico:
        print(med4)
    marcar = str(input('Selecione o horario desejado:', ))
    print(marcar, 'Seu horario foi agendado com sucesso ;)')
else:
    print('Médico indisponivel!')





