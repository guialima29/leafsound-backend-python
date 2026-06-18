# LeafSound Backend Planning

Esta pasta guarda o planejamento vivo do backend do LeafSound. O escopo atual do backend e objetivo e direto: CRUD de usuarios, CRUD de workspaces, CRUD de notas com `content` JSON, sistema de feedback e login com Google.

## Como usar

- Leia `00-visao-produto.md` para lembrar o recorte do produto que cabe ao backend.
- Use `01-backend-atual.md` como diagnostico tecnico do codigo existente.
- Siga os arquivos de modulo para implementar em etapas pequenas e verificaveis.
- Atualize os checklists conforme as decisoes de API e banco mudarem.

## Ordem sugerida

1. Corrigir a base SQLAlchemy/FastAPI descrita em `01-backend-atual.md`.
2. Fechar usuarios e autenticacao em `02-modulo-usuarios.md`.
3. Implementar CRUD real de workspaces em `03-modulo-workspaces.md`.
4. Implementar CRUD real de notas em `04-modulo-notas.md`.
5. Adicionar feedback em `05-modulo-feedback.md`.
6. Seguir o roteiro incremental em `06-roadmap-passos.md`.

## Modulos principais

- Usuarios: cadastro, listagem, leitura, atualizacao, remocao e autenticacao.
- Google Login: autenticacao externa vinculada ao usuario.
- Workspaces: organizacao das notas por usuario.
- Notas: CRUD de anotacoes salvas dentro de workspaces, com apenas `content` JSON como dado editavel.
- Feedback: canal para opinioes, problemas e ideias.

## Fora do escopo do backend neste momento

- Editor musical, cifras, tablaturas e renderizacao.
- Rolagem automatica, metronomo, BPM e ferramentas de som.
- Implementacao de telas e componentes de interface.
