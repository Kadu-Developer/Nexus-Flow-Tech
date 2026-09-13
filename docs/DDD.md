# DDD — Domain-Driven Design (Nexus Flow Tech)

## 1. Domínios Principais

### 1.1 Domínio de Apresentação (Presentation)
- **Responsabilidade**: Renderização visual do site
- **Entidades**: Hero, Sections, Header, Footer, Cards
- **Bounded Context**: HTML estático com CSS inline

### 1.2 Domínio de Conteúdo (Content)
- **Responsabilidade**: Texto, imagens, textos das seções
- **Entidades**: Article, Section, Image, Form
- **Bounded Context**: Arquivos `.html` e diretório `assets/`

### 1.3 Domínio de Design System (Design System)
- **Responsabilidade**: Componentes reutilizáveis, tokens, estilos
- **Entidades**: BrandLogo, FeatureCard, GlowButton, SectionHeader
- **Bounded Context**: `Nexus-Flow-Tech-Design-System/`

### 1.4 Domínio de Otimização (Optimization)
- **Responsabilidade**: Compressão de imagens, performance
- **Entidades**: ImageOptimizer, WebPConverter, LazyLoader
- **Bounded Context**: Scripts `optimize-images.py`, `update-html.py`

## 2. Mapa de Contextos

| Contexto | Limite | Interação |
|---|---|---|
| Apresentação | HTML/CSS | Consome Design System |
| Conteúdo | HTML/Assets | Produz páginas finais |
| Design System | Componentes React | Fornece padrões visuais |
| Otimização | Scripts Python | Atua sobre Assets e HTML |

## 3. Entidades de Domínio
- **Site**: Conjunto de páginas estáticas
- **Page**: `index.html` (homepage), `sobre.html`, etc.
- **Image**: Arquivo visual (logo, foto, ícone de segmento)
- **Section**: Bloco de conteúdo (Mercados, Benefícios, Equipe)
- **Form**: Formulário de contato via FormSubmit
