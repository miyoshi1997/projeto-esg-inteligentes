# Projeto - Cidades ESGInteligentes
Link GitHub: https://github.com/miyoshi1997/projeto-esg-inteligentes
## Como executar localmente com Docker
Para subir a aplicação e o banco de dados, utilize o comando:
```bash
docker-compose up --build

Como executar localmente com Docker
1.Certifique-se de ter o Docker e o Docker Compose instalados.
2.No terminal, dentro da pasta raiz do projeto, execute:
docker-compose up --build
3.O sistema irá buildar a imagem Python, iniciar o MongoDB e realizar o registro automático de coletas.

Pipeline CI/CD
Utilizamos o GitHub Actions para gerenciar o ciclo de vida da aplicação (ALM). O funcionamento baseia-se em:
Ferramenta: GitHub Actions via arquivo main.yml
Etapas:


Build: Geração automática da imagem Docker a partir do Dockerfile.


Test: Validação de sintaxe e integridade do script Python.


Deploy: Simulação de entrega contínua nos ambientes de Staging e Produção.

ContainerizaçãoA estratégia adotada foca no isolamento e portabilidade:
Dockerfile: Utiliza a imagem base python:3.9-slim para manter o container leve.
Orquestração: O docker-compose.yml gerencia a comunicação entre o app (Python) e o db (MongoDB) através de uma rede interna.
Persistência: Uso de Volumes para garantir que os dados do MongoDB em Londrina não sejam perdidos ao reiniciar os containers.

Prints do funcionamento
As evidências completas de execução (Terminal), persistência (MongoDB Compass) e deploy (GitHub Actions) estão detalhadas no Relatório Técnico (PDF) anexo a este repositório ou na pasta imagens.

ecnologias utilizadas

Linguagem: Python 3.9.


Banco de Dados: MongoDB (NoSQL).


Infraestrutura: Docker e Docker Compose.


Pipeline: GitHub Actions.
