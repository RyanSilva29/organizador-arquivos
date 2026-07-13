import os
import shutil
from datetime import datetime

# Mapeamento de extensões para suas respectivas pastas de destino
MAPEAMENTO_DIRETORIOS = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Instaladores": [".exe", ".msi", ".dmg", ".pkg"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

def organizar_diretorio(caminho_alvo):
    if not os.path.exists(caminho_alvo):
        print(f"Erro: O diretório '{caminho_alvo}' não existe.")
        return

    print(f"Varrendo o diretório: {caminho_alvo}\n")
    arquivos_movidos = 0
    
    for item in os.listdir(caminho_alvo):
        caminho_item = os.path.join(caminho_alvo, item)
        
        # Ignora se for um diretório
        if os.path.isdir(caminho_item):
            continue
            
        _, extensao = os.path.splitext(item)
        extensao = extensao.lower()
        
        # Descobre o destino correto baseado na extensão
        pasta_destino = "Outros"
        for categoria, extensoes in MAPEAMENTO_DIRETORIOS.items():
            if extensao in extensoes:
                pasta_destino = categoria
                break
                
        diretorio_destino = os.path.join(caminho_alvo, pasta_destino)
        
        # Cria a pasta caso ela não exista
        if not os.path.exists(diretorio_destino):
            os.makedirs(diretorio_destino)
            
        # Move o arquivo de forma segura
        shutil.move(caminho_item, os.path.join(diretorio_destino, item))
        print(f"📦 Movido: {item} -> Falder: {pasta_destino}")
        arquivos_movidos += 1

    # Registra a atividade em um arquivo de log histórico
    if arquivos_movidos > 0:
        with open(os.path.join(caminho_alvo, "historico_limpeza.log"), "a", encoding="utf-8") as log:
            agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"[{agora}] Sucesso: {arquivos_movidos} arquivos organizados automaticamente.\n")
            
    print(f"\n✨ Concluído! Total de arquivos organizados: {arquivos_movidos}")

if __name__ == "__main__":
    # Substitua pelo caminho de uma pasta de testes no seu computador
    pasta_teste = "./minha_pasta_bagunçada"
    
    # Criando pasta de teste local apenas para simulação
    if not os.path.exists(pasta_teste):
        os.makedirs(pasta_teste)
        # Cria um arquivo de texto falso para teste
        with open(os.path.join(pasta_teste, "documento_teste.txt"), "w") as f: f.write("Demo")
        with open(os.path.join(pasta_teste, "foto.jpg"), "w") as f: f.write("Demo")

    organizar_diretorio(pasta_teste)
