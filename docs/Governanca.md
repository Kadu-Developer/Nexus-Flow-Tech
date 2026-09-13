# Governança — Projeto Nexus Flow Tech

## 1. Padrões de Código
- **HTML**: Semântico, com `alt`, `width`, `height`, `loading`, `decoding`
- **CSS**: Tokens CSS (`:root`) para consistência
- **JS**: Mínimo obrigatório (menu mobile, scroll event)

## 2. Requisitos de Performance (Implementados)
- [X] **WebP**: Conversão automática de PNG/JPEG → WebP
- [X] **Lazy Loading**: `loading="lazy"` em todas as imagens
- [X] **Responsive Images**: `<picture>` com `<source>` para WebP + fallback PNG
- [X] **Compressão**: Quality 80% para fotos, 95% para logos
- [X] **Atributos de Responsividade**: `width`, `height`, `decoding="async"`

## 3. Requisitos de Acessibilidade
- `alt` descritivo em todas as imagens
- `aria-label` em botões de navegação
- `loading="lazy"` sem quebrar acessibilidade

## 4. Padrões de Ativos (`assets/`)
- Nomenclatura: `segmento-[nome].png` / `.webp`
- Tamanho de referência: 1024×1024 para segmentos
- Favicon em múltiplos tamanhos (16×16, 32×32, 192×192, 512×512)

## 5. Scripts de Automação
- `optimize-images.py`: Conversão de imagens (PIL/WebP)
- `update-html.py`: Atualização de HTML com WebP, lazy loading, meta tags

## 6. Regras do CLAUDE.md (Global)
- Sempre ler arquivo antes de editar (`Read` antes de `Edit`)
- Confirmar comandos destrutivos
- Usar caminhos absolutos para `Read`/`Write`/`Edit`
- Não inventar nomes de ferramentas (usar nomes exatos em maiúsculas)
- Não usar `Glob`/`Grep` diretamente — usar `Bash` com `find`/`grep`
- Sempre confirmar comandos destrutivos (`rm`, `del`, `format`)
- Usar `Task` para subagentes quando necessário
- Usar `EnterPlanMode` para tarefas complexas
