def ler_dataset(caminho_arquivo):
    obras = []
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        cabecalhos = linhas[0].strip().split(',')
        
        for linha in linhas[1:]:
            valores = linha.strip().split(',')
            
            obra = {}
            for i, valor in enumerate(valores):
                if i < len(cabecalhos):
                    obra[cabecalhos[i]] = valor
            
            obras.append(obra)
    
    return obras

def listar_compositores(obras):
    compositores = set()
    for obra in obras:
        if 'compositor' in obra:
            compositores.add(obra['compositor'])
    
    return sorted(list(compositores))

def distribuicao_por_periodo(obras):
    contagem = {}
    for obra in obras:
        if 'periodo' in obra:
            periodo = obra['periodo']
            if periodo in contagem:
                contagem[periodo] += 1
            else:
                contagem[periodo] = 1
    
    return contagem

def dicionario_periodos_titulos(obras):
    periodos_titulos = {}
    
    for obra in obras:
        if 'periodo' in obra and 'titulo' in obra:
            periodo = obra['periodo']
            titulo = obra['titulo']
            
            if periodo in periodos_titulos:
                periodos_titulos[periodo].append(titulo)
            else:
                periodos_titulos[periodo] = [titulo]
    
    for periodo in periodos_titulos:
        periodos_titulos[periodo] = sorted(periodos_titulos[periodo])
    
    return periodos_titulos

def main():
    caminho_arquivo = 'obras_musicais.txt'
    
    try:
        obras = ler_dataset(caminho_arquivo)
        
        compositores = listar_compositores(obras)
        print("\nLista ordenada de compositores:")
        for compositor in compositores:
            print(f"- {compositor}")
        
        distribuicao = distribuicao_por_periodo(obras)
        print("\nDistribuição de obras por período:")
        for periodo, quantidade in distribuicao.items():
            print(f"- {periodo}: {quantidade} obras")
        
        periodos_titulos = dicionario_periodos_titulos(obras)
        print("\nObras por período:")
        for periodo, titulos in periodos_titulos.items():
            print(f"\n{periodo}:")
            for titulo in titulos:
                print(f"- {titulo}")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    main()
