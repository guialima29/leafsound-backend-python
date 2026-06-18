# Roadmap Passo a Passo

## Fase 0 - Base tecnica

Objetivo: deixar o backend confiavel para evoluir.

- [x] Fazer todos os models usarem o mesmo `Base`.
- [x] Padronizar tipos de ID e FKs.
- [ ] Corrigir injecao de `db` em rotas de notes.
- [ ] Criar schemas ausentes.
- [ ] Definir estrategia de erro com `HTTPException`.
- [ ] Criar `.env.example`.
- [ ] Planejar migracoes com Alembic.

## Fase 1 - Usuarios e autenticacao

Objetivo: implementar CRUD de usuarios e base de autenticacao.

- [x] Criar modelo completo de usuario.
- [x] Criar CRUD de usuario.
- [x] Criar token local da API.
- [x] Criar dependencia de usuario autenticado.
- [x] Criar rota `/users/me`.

## Fase 2 - Login com Google

Objetivo: permitir entrada usando conta Google.

- [ ] Definir variaveis de ambiente do Google OAuth.
- [x] Validar token Google recebido do cliente.
- [x] Criar usuario automaticamente no primeiro login, se necessario.
- [x] Vincular `google_sub` ao usuario.
- [x] Retornar token local da API apos login Google.

## Fase 3 - Workspaces

Objetivo: permitir organizacao basica de notas.

- [x] Criar CRUD real de workspace.
- [x] Garantir que workspace pertence ao usuario.
- [x] Criar listagem ordenada.
- [x] Proteger todas as rotas por autenticacao.
- [x] Limitar usuario a no maximo 5 workspaces.

## Fase 4 - Notas

Objetivo: entregar CRUD completo de notas.

- [x] Criar CRUD completo de notas.
- [x] Adicionar update de titulo, favorito e `content`.
- [x] Manter `content` como JSON do Editor.js.
- [x] Proteger acesso por dono do workspace.

## Fase 5 - Feedback

Objetivo: coletar opinioes e ideias dos usuarios.

- [ ] Criar modulo `feedback`.
- [ ] Criar envio autenticado.
- [ ] Criar listagem do proprio usuario.
- [ ] Preparar status administrativo, se necessario.

## Fora do escopo atual

- Editor musical.
- Cifras e tablaturas como regras de backend.
- Metronomo, BPM e rolagem automatica.
