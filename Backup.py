import shutil
import datetime

def fazer_backup(diretorio_origem, diretorio_destino):
    # Criar um nome de arquivo único usando a data e hora atual
    data_atual = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    nome_arquivo = f'backup_{data_atual}.zip'

    # Criar o caminho completo para o arquivo de backup
    caminho_arquivo = f'{diretorio_destino}/{nome_arquivo}'

    try:
        # Criar um arquivo zip contendo todos os arquivos do diretório de origem
        shutil.make_archive(caminho_arquivo, 'zip', diretorio_origem)
        print(f"Backup criado com sucesso: {caminho_arquivo}")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o backup: {str(e)}")

# Exemplo de uso
diretorio_origem = '/caminho/do/diretorio/origem'
diretorio_destino = '/caminho/do/diretorio/destino'

fazer_backup(diretorio_origem, diretorio_destino)
