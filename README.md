# 🛠️ Sistema de Tickets para Aprovação de Orçamentos

Este projeto foi desenvolvido como parte da minha prática com **Django**, simulando um fluxo de criação e aprovação de orçamentos para uso administrativo. Ele possui controle de usuários, autenticação, filtros e lógica de permissões baseada em cargos (Administrador e Funcionário).

---

## ✨ Funcionalidades

### 👨‍💼 Usuário Administrador

- Acesso total ao sistema.
- Criação e edição de tickets.
- Cadastro de novos usuários.
- Visualização detalhada dos tickets, com até **3 cotações** enviadas pelo funcionário.
- Aprovação de uma das cotações ou rejeição do ticket.
  - Tickets rejeitados mudam para **vermelho** e tornam-se inacessíveis ao funcionário.

### 👨‍🔧 Usuário Comum (Funcionário)

- Pode criar novos tickets.
- Pode editar **apenas** os tickets que ele mesmo criou.

---

## 🔐 Segurança de Sessão

O sistema implementa configurações para sessões seguras e automáticas:

```python
SESSION_COOKIE_AGE = 900  # 15 minutos de inatividade
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True
```

---

## 🔎 Filtros Disponíveis

Na barra de navegação:

- **Filtro por Filial** (dropdown)
- **Busca por Assunto ou Observação** (campo de texto)

---

## ⚙️ Tecnologias Utilizadas

- **Backend:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Banco de Dados:** PostgreSQL
- **Containerização:** Docker e Docker Compose

---

## 🚀 Executando com Docker (recomendado)

### Pré-requisitos

- Docker
- Docker Compose

### Instruções

Clone o repositório:

```bash
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
```

Suba os containers:

```bash
docker-compose up --build
```

Acesse o sistema em:  
[http://localhost:8000](http://localhost:8000)

> O banco de dados é criado automaticamente com volume persistente.

---

## 💻 Execução Manual (sem Docker)

Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py migrate
```

Rode o servidor:

```bash
python manage.py runserver
```

---

## 🖼️ Capturas de Tela

*(Adicione aqui imagens do sistema em uso — página de login, listagem de tickets, visualização detalhada, etc.)*

---

## 📌 Status

🚧 Projeto em desenvolvimento contínuo como prática e aprendizado em Django + Docker.

---

## 📬 Contato

Desenvolvido por **Marcus Vinícius Quintanilha**  
[LinkedIn](https://www.linkedin.com/in/seu-perfil) • [GitHub](https://github.com/seuusuario)
