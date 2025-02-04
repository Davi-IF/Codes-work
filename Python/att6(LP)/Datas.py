def verificacao(data):
    # Verificar se as barras estão nas posições corretas
    if data[2] != '/' or data[5] != '/':
        print("Erro, barra inválida!")
        return False

    # Verificar se os caracteres nas posições do dia, mês e ano são números
    for i in range(0, 2):
        if not data[i].isdigit():
            print("Erro. Não contém números no dia.")
            return False
    
    for i in range(3, 5):
        if not data[i].isdigit():
            print("Erro. Não contém números no mês.")
            return False
    
    for i in range(6, 10):
        if not data[i].isdigit():
            print("Erro. Não contém números no ano.")
            return False

    return True

def main():
    # Solicitar ao usuário para digitar a data
    S = input("Digite a data (DD/MM/AAAA): ")

    # Verificar a data
    if verificacao(S):
        print("Data válida!")
        D, M, A = map(int, S.split('/'))
        print(f"Dia: {D}, Mês: {M}, Ano: {A}")
    else:
        print("Data inválida!")

if __name__ == "__main__":
    main()
