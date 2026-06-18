# Backend Atual

## Stack observada

- FastAPI para API HTTP.
- SQLAlchemy para modelos e sessoes de banco.
- PostgreSQL configurado por variaveis de ambiente em `app/variables.py`.
- Estrutura modular inicial em `app/users`, `app/workspaces` e `app/notes`.

## Arquivos principais

- `app/main.py`: cria o app FastAPI, registra rotas e chama `Base.metadata.create_all(bind=engine)`.
- `app/database.py`: define `engine`, `SessionLocal`, `Base` e dependencia `get_db`.
- `app/variables.py`: monta a string de conexao do Postgres.
- `app/users/*`: esqueleto de usuario.
- `app/workspaces/*`: esqueleto de workspace.
- `app/notes/*`: criacao de nota com service parcialmente implementado.

## Rotas atuais

| Modulo | Metodo | Caminho | Estado |
| --- | --- | --- | --- |
| root | GET | `/api/` | Retorna `Hello World`. |
| users | POST | `/users/register/{email}` | Mock, nao salva no banco. |
| users | GET | `/users/login` | Mock, nao autentica. |
| workspaces | POST | `/workspaces/{user_id}` | Mock, nao salva no banco. |
| workspaces | GET | `/workspaces/{user_id}` | Mock, nao busca no banco. |
| workspaces | DELETE | `/workspaces/{workspace_id}` | Mock, nao remove no banco. |
| notes | POST | `/notes/` | Tenta salvar nota no banco. |
| notes | GET | `/notes/{workspace_id}` | Planejada, chamada atual esta inconsistente. |
| notes | GET | `/notes/note/{id}` | Planejada, chamada atual esta inconsistente. |
| notes | DELETE | `/notes/{id}` | Planejada, chamada atual esta inconsistente. |

## Modelos atuais

### User

Campos atuais:

- `user_id`: UUID, chave primaria.
- `user_name`: string unica.
- `user_email`: string.

Lacunas:

- Falta estrategia de autenticacao.
- Falta campo para vinculo com Google, se o login Google for implementado diretamente no banco local.
- Falta schema de entrada/saida.
- Falta service.
- `Base` local impede integracao direta com `app/database.py`.

### Workspace

Campos atuais:

- `workspace_id`: inteiro autoincremental.
- `workspace_name`: string unica.
- `user_id`: foreign key para `users.user_id`.

Lacunas:

- `user_id` esta como inteiro, mas `users.user_id` esta como UUID.
- Nome unico global pode impedir usuarios diferentes de terem workspaces com o mesmo nome.
- Falta schema e service.
- `Base` local impede integracao direta com `app/database.py`.

### Note

Campos atuais:

- `note_id`: inteiro autoincremental.
- campos extras que nao entram mais no escopo.
- `content`: JSON no modelo alvo.
- `workspace_id`: foreign key para `workspaces.workspace_id`.

Lacunas:

- Novo escopo da nota deve manter apenas `content` JSON como dado editavel.
- Falta update de nota.
- Rotas de listagem, busca e delete nao injetam `db`.
- `Base` local impede integracao direta com `app/database.py`.

## Debitos tecnicos prioritarios

- Usar o mesmo `Base` de `app/database.py` em todos os modelos.
- Padronizar IDs e foreign keys.
- Corrigir injecao de `Session` nas rotas de notas.
- Criar schemas Pydantic para todos os inputs e outputs.
- Trocar respostas mockadas por services reais.
- Adicionar tratamento de erro com `HTTPException`.
- Criar estrutura de autenticacao para proteger workspaces, notes e feedback.
- Adicionar suporte ao login com Google.
- Evitar `create_all` como estrategia definitiva e planejar migracoes com Alembic.
- Criar arquivo `.env.example` sem segredos reais.

## Decisoes sugeridas

- Manter FastAPI + SQLAlchemy + PostgreSQL.
- Usar `uuid.UUID` para `User.user_id`.
- Usar relacionamento: `User -> Workspace -> Note`.
- Simplificar notas para armazenarem apenas `content` JSON como dado editavel.
- Criar Feedback como modulo proprio: `app/feedback`.
