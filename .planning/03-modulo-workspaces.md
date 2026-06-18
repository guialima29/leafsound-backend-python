# Modulo Workspaces

## Objetivo

Permitir CRUD de workspaces pertencentes ao usuario autenticado. O workspace e apenas um agrupador de notas no backend.

## Estado atual

- Existe `app/workspaces/model.py` com `Workspace`.
- Rotas de criar, listar e deletar retornam mocks.
- `schema.py` e `services.py` estao vazios.
- `user_id` esta como inteiro, mas o usuario atual usa UUID.

## Modelo sugerido

Campos iniciais:

- `workspace_id`: id do workspace.
- `workspace_name`: nome visivel.
- `user_id`: dono do workspace.

## Schemas sugeridos

- `WorkspaceCreate`: nome.
- `WorkspaceUpdate`: nome.
- `WorkspaceRead`: dados do workspace.

## Rotas sugeridas

| Metodo | Caminho | Acao |
| --- | --- | --- |
| POST | `/workspaces` | Criar workspace para usuario autenticado. |
| GET | `/workspaces` | Listar workspaces do usuario autenticado. |
| GET | `/workspaces/{workspace_id}` | Abrir workspace especifico. |
| PATCH | `/workspaces/{workspace_id}` | Atualizar workspace. |
| DELETE | `/workspaces/{workspace_id}` | Remover workspace. |

## Regras

- Um usuario so acessa os proprios workspaces.
- Dois usuarios podem ter workspaces com o mesmo nome.
- O mesmo usuario pode ou nao repetir nomes, conforme decisao de produto.
- Cada usuario pode ter no maximo 5 workspaces.
- Ao deletar workspace, definir se as notas serao removidas em cascata ou bloqueadas por integridade.

## Checklist de implementacao

- [x] Corrigir FK para apontar ao tipo real de `users.user_id`.
- [x] Importar `Base` de `app/database.py`.
- [x] Criar schemas.
- [x] Criar services reais.
- [x] Proteger rotas por usuario autenticado.
- [x] Garantir que queries filtrem pelo dono.
- [x] Aplicar limite de 5 workspaces por usuario.
- [x] Definir politica de delete.

## Implementado agora

- `POST /workspaces/`: cria workspace para o usuario autenticado.
- `GET /workspaces/`: lista apenas workspaces do usuario autenticado.
- `GET /workspaces/{workspace_id}`: abre um workspace do usuario autenticado.
- `PATCH /workspaces/{workspace_id}`: atualiza nome.
- `DELETE /workspaces/{workspace_id}`: remove o workspace.
- Limite: cada usuario pode criar no maximo 5 workspaces.

## Criterios de aceite

- Usuario autenticado cria workspace.
- Usuario nao consegue criar mais de 5 workspaces.
- Listagem retorna apenas workspaces do usuario logado.
- Usuario nao consegue acessar workspace de outra pessoa.
- Atualizacao e remocao respeitam ownership.
