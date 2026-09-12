# Nexus Flow Tech

Transformação Digital Inteligente — Automação de Processos, Integração de Sistemas, IA e Dashboards em Tempo Real.

## Sobre

A Nexus Flow Tech transforma processos manuais em operações inteligentes utilizando Inteligência Artificial, Automação de Processos (RPA), Integração de Sistemas e Dashboards em Tempo Real.

- Site: https://nexusflowtech.com.br
- Contato: marcel@nexusflowtech.com.br
- WhatsApp: (11) 98960-1000

## Estrutura

- `index.html` — Home com hero, soluções (automação, IA, dashboards), mercados (indústria, agronegócio, logística, etc.), depoimentos, formulário de contato
- `sobre.html` — Liderança (Marcel Wachowicz, Patrik Rodrigues, Carlos Eduardo, José Carlos)
- `obrigado.html` — Confirmação de envio de pedido
- `politica-de-privacidade.html` — LGPD / privacidade
- `assets/` — WebP otimizados (~93-97% menores que PNG/JPEG originais), logo, segmentações por mercado

## Otimização de Imagens

Todas as imagens foram convertidas para WebP com qualidade 80-95, lazy loading (`loading="lazy"`) e decodificação assíncrona (`decoding="async"`). Os `<img>` originais foram preservados como fallback dentro de `<picture>` para compatibilidade com navegadores antigos.

Script de otimização: `update-html-optimization.py` (preserva atributo `class` ao criar `<picture>`).

## Licença

MIT — ver `LICENSE`.

## Segurança

Política de divulgação responsável: `SECURITY.md`. Nenhum dado sensível é armazenado no repositório.
