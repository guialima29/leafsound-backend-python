# Visao do Produto para o Backend

## Recorte atual

O LeafSound e uma aplicacao de anotacao musical, mas este backend deve cuidar apenas da base de dados e da API necessaria para o produto funcionar:

- CRUD de usuarios.
- Login tradicional, se decidido, e login com Google.
- CRUD de workspaces.
- CRUD de notas com `content` JSON.
- Sistema de feedback.

Qualquer experiencia de editor musical, cifra, rolagem, BPM ou interface fica fora deste planejamento de backend por enquanto.

## Entidades do MVP

| Entidade | Responsabilidade |
| --- | --- |
| Usuario | Identidade, dados basicos e autenticacao. |
| Conta Google | Vinculo externo para login com Google. |
| Workspace | Agrupamento de notas pertencente a um usuario. |
| Nota | `content` JSON salvo dentro de um workspace. |
| Feedback | Mensagem enviada pelo usuario sobre a aplicacao. |

## Requisitos do backend

| Codigo | Requisito | Prioridade | Observacao |
| --- | --- | --- | --- |
| BE001 | CRUD de usuarios | Essencial | Criar, listar/consultar, atualizar e remover usuarios. |
| BE002 | Autenticacao | Essencial | Permitir login e proteger rotas privadas. |
| BE003 | Login com Google | Essencial | Aceitar autenticacao Google e vincular/criar usuario. |
| BE004 | CRUD de workspaces | Essencial | Usuario gerencia seus proprios workspaces. |
| BE005 | CRUD de notas | Essencial | Usuario gerencia notas com `content` JSON dentro de seus workspaces. |
| BE006 | Feedback | Importante | Usuario envia opinioes, problemas e ideias. |

## MVP recomendado

1. Usuario se cadastra ou entra com Google.
2. Usuario autenticado cria, lista, edita e remove workspaces.
3. Usuario autenticado cria, lista, abre, edita e remove notas.
4. Usuario autenticado envia feedback.
5. API garante que um usuario nao acessa dados de outro usuario.

## Principios de API

- Toda entidade deve ter schemas Pydantic claros para entrada e saida.
- Rotas privadas devem depender de usuario autenticado.
- Services devem concentrar regras de negocio e acesso ao banco.
- Models devem compartilhar o mesmo `Base` definido em `app/database.py`.
- Erros devem usar `HTTPException` com status HTTP coerente.
