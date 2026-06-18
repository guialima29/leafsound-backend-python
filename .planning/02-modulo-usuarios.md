# Modulo Usuarios

## Objetivo

Permitir CRUD de usuarios e autenticacao com Google. Este modulo e a base para proteger workspaces, notas e feedback.

## Estado atual

- Existe `app/users/model.py` com `User`.
- `app/users/router.py` possui rotas mockadas de registro e login.
- `app/users/schema.py` e `app/users/services.py` estao vazios.
- Nao ha persistencia real nas rotas de usuario.
- Nao ha login com Google.

## Modelo sugerido

Campos iniciais:

- `user_id`: UUID, chave primaria.
- `user_name`: nome do usuario.
- `user_email`: email unico.
- `avatar_url`: URL da foto do perfil retornada pelo Google.
- `google_sub`: identificador unico do usuario no Google.
- `created_at`: data de criacao.
- `updated_at`: data de ultima atualizacao.

## Schemas sugeridos

- `UserRead`: id, nome, email e avatar.
- `UserUpdate`: nome editavel.
- `GoogleLoginRequest`: token Google recebido do cliente.
- `TokenResponse`: access token local da API.

## Rotas sugeridas

| Metodo | Caminho | Acao |
| --- | --- | --- |
| GET | `/users/me` | Retornar usuario autenticado. |
| PATCH | `/users/me` | Atualizar usuario autenticado. |
| DELETE | `/users/me` | Remover usuario autenticado. |
| POST | `/auth/google` | Login com Google. |

## Regras

- Email deve ser unico.
- Dados sensiveis nunca devem aparecer em respostas.
- Rotas privadas devem depender do usuario autenticado.
- Login com Google deve validar token do Google antes de criar ou autenticar usuario.
- Ao autenticar com Google, buscar usuario por `google_sub` ou email.
- A foto do usuario deve ser salva como URL em `avatar_url`.

## Checklist de implementacao

- [x] Importar `Base` de `app/database.py` no model.
- [x] Definir campos reais do usuario.
- [x] Criar schemas Pydantic.
- [x] Criar service de CRUD de usuario.
- [x] Criar estrategia de token local da API.
- [x] Criar dependencia de usuario autenticado.
- [x] Implementar login com Google.
- [ ] Proteger rotas futuras de workspaces, notas e feedback.

## Implementado agora

- `POST /auth/google`: valida token Google, cria ou atualiza usuario e retorna token local da API.
- `GET /users/me`: retorna o usuario autenticado.
- `PATCH /users/me`: atualiza o nome do usuario autenticado.
- `DELETE /users/me`: remove o usuario autenticado.
- `avatar_url`: salva a URL da foto do perfil retornada pelo Google.

## Criterios de aceite

- Usuario pode ser criado pelo login Google, consultado, atualizado e removido.
- Login com Google valida token externo e retorna token da API.
- Rotas privadas identificam o usuario autenticado.
- Dados sensiveis nao sao retornados pela API.
