def verificacao(S):

    if S[2] != '/' or S[5] != '/':
        print("Erro, barra inválida!")
        return False

    if not S[0:2].isdigit():
        print("Erro. Não contém números no dia.")
        return False

  
    if not S[3:5].isdigit():
        print("Erro. Não contém números no mês.")
        return False

 
    if not S[6:10].isdigit():
        print("Erro. Não contém números no ano.")
        return False

    return True


def main():
   
    S = input("Digite a data (DD/MM/AAAA): ")

    
    if verificacao(S):
        print("Data válida!")
       
        D, M, A = map(int, S.split('/'))
        print(f"Dia: {D}, Mês: {M}, Ano: {A}")
    else:
        print("Data inválida!")


if __name__ == "__main__":
    main()
