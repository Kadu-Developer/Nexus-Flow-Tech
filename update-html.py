#!/usr/bin/env python3
"""
Atualiza HTMLs com WebP via <picture>, lazy loading, e meta tags corrigidas.
"""
import os, re

# Mapping: arquivo original -> arquivo WebP (para criar <picture>)
WEBP_MAP = {
    'assets/nexus-flow-tech-logo.png': 'assets/nexus-flow-tech-logo.webp',
    'assets/marcel-wachowicz.jpeg': 'assets/marcel-wachowicz.webp',
    'assets/jose-carlos.png': 'assets/jose-carlos.webp',
    'assets/og-nexus-flow-tech.jpg': 'assets/og-nexus-flow-tech.webp',
    'assets/segmento-agronegocio.png': 'assets/segmento-agronegocio.webp',
    'assets/segmento-comercio.png': 'assets/segmento-comercio.webp',
    'assets/segmento-construcao-civil.png': 'assets/segmento-construcao-civil.webp',
    'assets/segmento-distribuicao.png': 'assets/segmento-distribuicao.webp',
    'assets/segmento-financeiro.png': 'assets/segmento-financeiro.webp',
    'assets/segmento-industria.png': 'assets/segmento-industria.webp',
    'assets/segmento-logistica.png': 'assets/segmento-logistica.webp',
    'assets/segmento-prestacao-servicos.png': 'assets/segmento-prestacao-servicos.webp',
    'assets/segmento-saude.png': 'assets/segmento-saude.webp',
}

# Arquivos que ja sao WebP - so garantir lazy loading
ALREADY_WEBP = [
    'assets/patrik-rodrigues.webp',
    'assets/carlos-eduardo-ribeiro.webp',
]

def make_picture_tag(original_src, webp_src, attrs_str):
    """Cria tag <picture> com <source> e <img> fallback."""
    # Extrair atributos relevantes do img original
    alt_m = re.search(r'alt="([^"]*)"', attrs_str)
    width_m = re.search(r'width="(\d+)"', attrs_str)
    height_m = re.search(r'height="(\d+)"', attrs_str)
    loading_m = re.search(r'loading="([^"]*)"', attrs_str)
    class_m = re.search(r'class="([^"]*)"', attrs_str)

    alt = alt_m.group(1) if alt_m else ''
    width = width_m.group(1) if width_m else ''
    height = height_m.group(1) if height_m else ''
    loading = loading_m.group(1) if loading_m else 'lazy'
    cls = class_m.group(1) if class_m else ''

    img_attrs = []
    if width: img_attrs.append(f'width="{width}"')
    if height: img_attrs.append(f'height="{height}"')
    img_attrs.append(f'loading="{loading}"')
    if alt: img_attrs.append(f'alt="{alt}"')
    img_attrs.append('decoding="async"')
    if cls: img_attrs.append(f'class="{cls}"')
    attrs_joined = ' '.join(img_attrs)

    return (
        '<picture>\n'
        f'            <img src="{webp_src}" {attrs_joined} />\n'
        f'            <img src="{original_src}" {attrs_joined}>\n'
        '        </picture>'
    )

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # 1. Substituir <img src="...png"> e <img src="...jpeg"> por <picture> com WebP
    for orig_src, webp_src in WEBP_MAP.items():
        if orig_src.endswith('.png') or orig_src.endswith('.jpeg'):
            # Padrao: <img src="ORIG" ...>
            pattern = re.escape(orig_src)
            regex = re.compile(
                r'<img\s+src="' + pattern + r'"([^>]*)>',
                re.DOTALL
            )

            def repl(m):
                attrs = m.group(1)
                return make_picture_tag(orig_src, webp_src, attrs)

            new_content = regex.sub(repl, content)
            if new_content != content:
                content = new_content
                changed = True

    # 2. Para imagens que ja sao WebP, garantir loading="lazy"
    for webp_src in ALREADY_WEBP:
        pattern = re.compile(
            r'<img\s+src="' + re.escape(webp_src) + r'"((?!<img)[^>]*)>',
            re.DOTALL
        )
        def repl(m):
            attrs = m.group(1)
            if 'loading=' in attrs:
                return m.group(0)
            return f'<img src="{webp_src}"{attrs} loading="lazy">'
        new_content = pattern.sub(repl, content)
        if new_content != content:
            content = new_content
            changed = True

    # 3. Atualizar og:image e twitter:image meta tags para .webp
    for old_name, new_name in [('og-nexus-flow-tech.jpg', 'og-nexus-flow-tech.webp')]:
        content = re.sub(
            r'(og:image\s+content="https://nexusflowtech\.com\.br/assets/)' + re.escape(old_name) + r'(")',
            r'\g<1>' + new_name + r'\2',
            content
        )
        content = re.sub(
            r'(twitter:image\s+content="https://nexusflowtech\.com\.br/assets/)' + re.escape(old_name) + r'(")',
            r'\g<1>' + new_name + r'\2',
            content
        )

    # 4. Garantir loading="lazy" em QUALQUER <img> que nao tenha
    def ensure_lazy(content):
        def repl(m):
            tag = m.group(0)
            if 'loading=' in tag or 'data-src' in tag:
                return tag
            # Inserir antes do > final
            return tag[:-1] + ' loading="lazy">'
        return re.sub(r'<img\s+[^>]*?>', repl, content, flags=re.DOTALL)

    new_content = ensure_lazy(content)
    if new_content != content:
        content = new_content
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('OK  ' + filepath)
    else:
        print('SKIP ' + filepath)

def main():
    for fp in ['index.html', 'sobre.html', 'obrigado.html', 'politica-de-privacidade.html']:
        if os.path.exists(fp):
            process_file(fp)
        else:
            print('SKIP ' + fp + ' (nao encontrado)')

if __name__ == '__main__':
    main()
