# Sistema Nado Livre

**Turma:** InfoWeb 2V

**Equipe:**
* Henzo Nunes Dias Soares
* Paulo Victor Leite Leão
* Ryann Richard Soares Silva

---

## 📌 Apresentação do Sistema

O controle manual de toalhas na escola de natação dificultava o rastreio de empréstimos, causando perda de toalhas e desorganização. Por isso foi desenvolvido um sistema para gerenciar e rastrear todo o ciclo de vida das toalhas (cadastro, retirada e devolução). Onde o sistema é operado pelos atendentes da escola nos balcões de atendimento, registrando as interações dos nadadores. Focando no cadastro de usuários e toalhas, controle de disponibilidade em tempo real e histórico de utilizações.

---

## 🗄️ Modelo Lógico do Banco de Dados (1ª Versão)

Abaixo está o Diagrama de Entidade-Relacionamento que representa a estrutura de dados do sistema.

```mermaid
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