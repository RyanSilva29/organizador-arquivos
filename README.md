# Automated File Organizer CLI

Um utilitário de automação de infraestrutura local que organiza dinamicamente diretórios bagunçados (como pastas de downloads, servidores locais de arquivos ou partições de logs). O script faz o mapeamento de metadados, cria árvores de diretórios sob demanda e mantém logs de auditoria.

## 🚀 Funcionalidades
- Escaneamento de sistema de arquivos local (`File System Integration`).
- Mapeamento dinâmico e classificação de arquivos por tipo de extensão.
- Criação condicional e movimentação segura de arquivos via sistema operacional.
- Geração automática de logs cronológicos para auditoria de processos automatizados.

## 🛠️ Tecnologias Utilizadas
- **Python 3** (Módulos nativos de OS: `os`, `shutil`, `datetime`)

## 📋 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com
   ```
2. Configure a variável `pasta_teste` no código apontando para o diretório que deseja limpar ou execute diretamente para testar o ambiente controlado criado pelo próprio script:
   ```bash
   python organizador.py
   ```
