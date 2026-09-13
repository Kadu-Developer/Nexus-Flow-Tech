# TDD — Technical Design Document (Nexus Flow Tech)

## 1. Arquitetura de Imagens

### Antes
```
assets/
  jose-carlos.png         (2.1MB PNG)
  marcel-wachowicz.jpeg   (275KB)
  segmento-*.png          (~1.8MB cada, 9 arquivos = ~17MB)
```

### Depois (Otimização Aplicada)
```
assets/
  jose-carlos.webp        (52KB, -97%)
  marcel-wachowicz.webp   (111KB, -60%)
  segmento-*.webp         (~100KB cada, ~94% redução)
  nexus-flow-tech-logo.webp (64KB, -65%)
  og-nexus-flow-tech.webp (41KB, -57%)
```

## 2. Implementação WebP com Fallback
```html
<picture>
  <source srcset="assets/segmento-industria.webp" type="image/webp">
  <img src="assets/segmento-industria.png" alt="..." width="1024" height="1024" loading="lazy" decoding="async">
</picture>
```

## 3. Lazy Loading
- `loading="lazy"` aplicado em todas as tags `<img>`
- `decoding="async"` para otimizar renderização

## 4. Meta Tags Atualizadas
- `og:image` → `.webp`
- `twitter:image` → `.webp`

## 5. Scripts de Automação
- `optimize-images.py`: Conversão PNG/JPEG → WebP via PIL
- `update-html.py`: Atualização HTML com `<picture>`, `lazy`, meta tags
