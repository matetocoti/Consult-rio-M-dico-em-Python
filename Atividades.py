# Função do consultorio médico
def Consultorio():
        # Fila do consultorio
        fila_de_consultas = ["Ana" ,"Matheus" ,"Lucas" ,"João"]
        # Rodando o programa até o usuário escolher parar
        while True:
            # Tratando exceções
            try:
                #Iniciando contador
                count = 1
                print(f"\t------------------------------------------------------")
                print(f"\n\t--(FILA DE ESPERA)--")
                # Mostrando lista de pacientes enumerados em ordem
                for paciente in fila_de_consultas:
                    print(f"\n\t({count}){paciente}  ")
                    # Contando pacientes da fila
                    count+=1
                print(f"\n\t------------------------------------------------------")
                # Menu de opções do sistema
                print(f"\n\t(1)Atender paciente | (2)Adicionar Paciente | (3)Exit")
                # Escolhendo opção do menu
                option = int(input(f"\n\tOption(1|2|3):"))

                # Se Escolhendo opção1
                if option == 1:
                    # Exibindo messagem falando que o paciente foi atendido e o nome do paciente atendido
                    print(f"\n\tPaciente atendido:\n\tnome: {fila_de_consultas[0]}")
                    # Atendendo paciente e removendo o primeiro item da lista com pop
                    fila_de_consultas.pop(0)
                # Se Escolhendo opção2
                elif option == 2:
                    # Pegando o nome do novo paciente
                    paciente =  input(f"\n\tDigite o nome do novo paciente:")
                    # Se não ha nada digitado
                    if len(paciente.split()) == 0:
                        # Exibindo messagem de error
                        print(f"\n\tNenhum valor digitado!")
                        continue
                    # Colocando novo paciente no fim da fila com pop
                    fila_de_consultas.append(paciente)
                # Se Escolhendo opção 3
                elif option == 3:
                    # Mostrando messagem de encerramento do sistema
                    print(f"\n\tEncerrando...")
                    # Encerrando sistema | Quebrando loop while
                    break
                    # Se escolhendo opção enexistente
                else:
                    # Exibindo messagem falando que a opção escolhida não existe
                    print(f"\n\tOpção invalida!")
                # Error de valor invalido
            except ValueError:
                print(f"\n\tError: Valor invalido")
                # Error inesperado
            except RuntimeError:
                print(f"\n\tError: Runtime")
                # Error de tentar acessar um valor de lista que não existe
            except IndexError:
                print(f"\n\tError: Não há pacientes na fila!")



