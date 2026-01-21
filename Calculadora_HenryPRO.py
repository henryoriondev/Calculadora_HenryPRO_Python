def calculadora():
    historico = [] # Nossa lista para guardar os logs
    
    while True:
        print("\n" + "="*30)
        print("CALCULADORA HENRY PRO")
        print("="*30)
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Ver Histórico")
        print("0. Sair")
        
        try:
            opcao = input("\nEscolha uma operação: ")
            
            if opcao == "0":
                print("Desligando sistema... Até logo!")
                break
            
            if opcao == "5":
                print("\nHISTÓRICO DE OPERAÇÕES:")
                for item in historico:
                    print(item)
                continue

            if opcao in ["1", "2", "3", "4"]:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if opcao == "1":
                    resultado = num1 + num2
                    operacao = f"{num1} + {num2} = {resultado}"
                elif opcao == "2":
                    resultado = num1 - num2
                    operacao = f"{num1} - {num2} = {resultado}"
                elif opcao == "3":
                    resultado = num1 * num2
                    operacao = f"{num1} * {num2} = {resultado}"
                elif opcao == "4":
                    if num2 == 0:
                        print(" Erro Crítico: Divisão por zero não permitida!")
                        continue
                    resultado = num1 / num2
                    operacao = f"{num1} / {num2} = {resultado}"

                print(f"\nResultado: {resultado}")
                historico.append(operacao) # Salva no histórico
            else:
                print("Opção inválida! Tente novamente.")

        except ValueError:
            print("Erro: Por favor, digite apenas números válidos.")

# Iniciar a ferramenta
calculadora()