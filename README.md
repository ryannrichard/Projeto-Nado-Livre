# Projeto-Nado-Livre
Repositório para salvar as alterações do projeto em python Nado Livre

Nome do Sistema: Sistema Nado Livre
Turma: InfoWeb 2V
Integrantes:Henzo Nunes Dias Soares, Paulo Victor Leite Leão, Ryann Richard Soares Silva

erDiagram
  NADADOR {
        string id PK
        string nome
    }

    TOALHA {
        string id PK
        string status
    }

    ATENDENTE {
        string id PK
        string nome
    }

    UTILIZACAO {
        string id PK
        string status
    }

    NADADOR ||--o{ UTILIZACAO : "solicita"
    TOALHA ||--o{ UTILIZACAO : "usada_em"
    ATENDENTE ||--o{ UTILIZACAO : "realiza_entrega"
    ATENDENTE |o--o{ UTILIZACAO : "recebe_devolucao"
