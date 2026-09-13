# SDD — Software Design Document (Nexus Flow Tech)

## 1. Visão Geral
Site estático em HTML/CSS/JS hospedado na Vercel com design system próprio (`Nexus-Flow-Tech-Design-System`).

## 2. Componentes Principais
- Header fixo com nav
- Hero com CTA
- Seções de conteúdo (Dores, Soluções, Mercados, Benefícios)
- Equipe com fotos
- Formulário via FormSubmit
- Footer

## 3. Stack Tecnológica
- HTML5 estático
- CSS inline + tokens (`:root`)
- JS mínimo (menu mobile, scroll)
- Assets locais (`assets/`)
- Formulário externo (FormSubmit)

## 4. Padrões de Design
- Design system: `Nexus-Flow-Tech-Design-System`
- Fontes: Montserrat, Hanken Grotesk, Geist Mono
- Tokens CSS: `--primary`, `--orange`, `--surface`, etc.

## 5. Otimizações Implementadas
- **WebP**: Conversão de PNG/JPEG para WebP (19MB → 1.1MB, 94% redução)
- **Lazy loading**: `loading="lazy"` em todas as imagens
- **Responsive images**: `<picture>` com `<source srcset>` para WebP + fallback PNG
- **Compressão**: Images comprimidas via `PIL` (quality 80-95)

## 6. Arquivos Chave
- `index.html`, `sobre.html`, `obrigado.html`, `politica-de-privacidade.html`
- `assets/` (imagens, logos, ícones)
- `Nexus-Flow-Tech-Design-System/` (componentes React + tokens)
