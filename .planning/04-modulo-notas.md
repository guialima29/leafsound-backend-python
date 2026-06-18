# Modulo Notas

## Objetivo

Permitir CRUD de notas pertencentes a workspaces do usuario autenticado. A nota possui titulo, favorito e `content` JSON do Editor.js.

## Estado atual

- Existe `app/notes/model.py` com `Note`.
- Existem schemas `NoteCreate`, `NoteUpdate` e `NoteRead` em `app/notes/schema.py`.
- `create_note` salva uma nota, mas listagem, busca e delete precisam receber `db` na rota.
- O model atual usa nomes antigos no banco, mas a API deve expor `title`, `is_favorite`, `content` e `workspace_id`.

## Modelo sugerido

Campos iniciais:

- `note_id`: id da nota.
- `title`: titulo da nota.
- `is_favorite`: indica se a nota esta favoritada.
- `content`: JSON generico recebido do cliente.
- `workspace_id`: workspace dono.

## Schemas sugeridos

- `NoteCreate`: `title`, `is_favorite` e `content`.
- `NoteUpdate`: `title`, `is_favorite` e `content`, todos opcionais para update parcial.
- `NoteRead`: dados completos da nota.

## Rotas sugeridas

| Metodo | Caminho | Acao |
| --- | --- | --- |
| POST | `/workspaces/{workspace_id}/notes` | Criar nota no workspace. |
| GET | `/workspaces/{workspace_id}/notes` | Listar notas do workspace. |
| GET | `/notes/{note_id}` | Abrir uma nota. |
| PATCH | `/notes/{note_id}` | Atualizar nota. |
| DELETE | `/notes/{note_id}` | Remover nota. |

## Regras

- Nota sempre pertence a um workspace.
- Usuario so acessa notas de workspaces proprios.
- `content` deve aceitar JSON valido do Editor.js.
- `workspace_id` e definido pela URL `POST /workspaces/{workspace_id}/notes`.
- O backend nao valida semantica musical do conteudo neste escopo.

## Checklist de implementacao

- [x] Importar `Base` de `app/database.py`.
- [x] Corrigir rotas para injetar `db`.
- [x] Criar update de `title`, `is_favorite` e `content`.
- [x] Criar schemas de resposta.
- [x] Garantir que nota pertence ao workspace do usuario autenticado.
- [x] Remover campos extras do contrato publico da nota.

## Implementado agora

- `POST /workspaces/{workspace_id}/notes`: cria nota com titulo, favorito e `content` JSON.
- `GET /workspaces/{workspace_id}/notes`: lista notas do workspace.
- `GET /notes/{note_id}`: abre uma nota do usuario autenticado.
- `PATCH /notes/{note_id}`: atualiza titulo, favorito e/ou `content`.
- `DELETE /notes/{note_id}`: remove a nota.
- Compatibilidade: a tabela antiga usa `note_title`, `note_fav` e `note_content`, mas a API expõe `title`, `is_favorite` e `content`.

## Criterios de aceite

- Usuario cria nota em um workspace proprio.
- Usuario lista notas do workspace.
- Usuario abre, atualiza e remove nota.
- Usuario nao acessa notas de workspaces de outra pessoa.
- Conteudo JSON enviado e recuperado sem alteracao inesperada.
