# Modulo Feedback

## Objetivo

Criar um canal para usuarios enviarem opinioes, problemas, elogios e ideias. Este modulo atende ao RF009 do PDF e ajuda a evoluir o LeafSound com base em uso real.

## Estado atual

- Nao existe modulo `feedback` no backend.
- Nao existem modelo, schema, service ou rota para feedback.

## Modelo sugerido

Campos iniciais:

- `feedback_id`: id do feedback.
- `user_id`: usuario que enviou, opcional se feedback anonimo for permitido.
- `category`: `bug`, `idea`, `like`, `dislike`, `other`.
- `message`: texto do feedback.
- `rating`: nota opcional de 1 a 5.
- `status`: `new`, `reviewed`, `planned`, `closed`.
- `created_at`: data de envio.

Campos futuros:

- `workspace_id`: contexto opcional.
- `note_id`: contexto opcional.
- `admin_response`: resposta interna ou publica.

## Schemas sugeridos

- `FeedbackCreate`: categoria, mensagem e nota opcional.
- `FeedbackRead`: dados do feedback enviado.
- `FeedbackAdminUpdate`: status e resposta administrativa.

## Rotas sugeridas

| Metodo | Caminho | Acao |
| --- | --- | --- |
| POST | `/feedback` | Enviar feedback. |
| GET | `/feedback/me` | Listar feedbacks do usuario. |
| GET | `/feedback` | Listar todos, futuro admin. |
| PATCH | `/feedback/{feedback_id}` | Atualizar status, futuro admin. |

## Regras

- Mensagem deve ter tamanho minimo e maximo.
- Categoria deve ser controlada por enum.
- Feedback pode exigir login no MVP para reduzir spam.
- Listagem geral deve ser apenas administrativa futuramente.

## Checklist de implementacao

- [ ] Criar pacote `app/feedback`.
- [ ] Criar model com FK opcional para usuario.
- [ ] Criar schemas.
- [ ] Criar service de envio.
- [ ] Registrar router em `app/main.py`.
- [ ] Criar listagem do proprio usuario.
- [ ] Planejar controle admin depois.

## Criterios de aceite

- Usuario autenticado envia feedback.
- Feedback fica salvo no banco.
- Usuario consegue listar os feedbacks que enviou.
- Dados retornados nao expõem informacoes de outros usuarios.

