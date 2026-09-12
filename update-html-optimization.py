#!/usr/bin/env python3
"""
Script de otimizacao de HTML para Nexus Flow Tech
Adiciona WebP, lazy loading e atributos de responsividade
"""

import re
import os

def build_picture_tag(src_webp, src_original, attrs, alt_text, width_val, height_val, loading_val):
    """Build a picture tag with WebP and fallback img."""
    attrs_list = []
    if width_val:
        attrs_list.append(f'width="{width_val}"')
    if height_val:
        attrs_list.append(f'height="{height_val}"')
    if loading_val:
        attrs_list.append(f'loading="{loading_val}"')
    if alt_text:
        attrs_list.append(f'alt="{alt_text}"')
    attrs_list.append(' decoding="async"')

    img_inner = '<img src="' + src_webp + '" ' + ' '.join(attrs_list) + ' />'
    # Preservar class no img interno do picture
    if class_attr:
        img_inner = img_inner.replace('<img src=', '<img class="' + class_attr.group(1) + '" src=')
    fallback_attrs = list(attrs_list)
    fallback_img = (
        '<img src="' + src_original + '" ' +
        ' '.join(fallback_attrs) + '>'
    )

    return (
        '<picture>' + '\n' +
        '            ' + img_inner + '\n' +
        '            ' + fallback_img + '\n' +
        '        </picture>'
    )

def optimize_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Mapeamento de src para versoes WebP
    webp_mappings = {
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

    for old_src, new_src in webp_mappings.items():
        pattern = r'<img\s+src="' + re.escape(old_src) + r'"([^>]*)>'

        def replace_fn(match):
            attrs_str = match.group(1)

            width = re.search(r'width="(\d+)"', attrs_str)
            height = re.search(r'height="(\d+)"', attrs_str)
            loading = re.search(r'loading="([^"]+)"', attrs_str)
            alt = re.search(r'alt="([^"]*)"', attrs_str)
            class_attr = re.search(r'class="([^"]*)"', attrs_str)

            w_val = width.group(1) if width else ''
            h_val = height.group(1) if height else ''
            l_val = loading.group(1) if loading else 'lazy'
            a_val = alt.group(1) if alt else ''

            # Se a imagem original nao e WebP, criar picture com fallback
            if not old_src.endswith('.webp'):
                return build_picture_tag(
                    new_src, old_src, attrs_str, a_val, w_val, h_val, l_val
                )
            else:
                # Ja e WebP, garantir loading lazy
                if not loading:
                    attrs_str += ' loading="lazy"'
                return f'<img src="{new_src}" {attrs_str}>'

        content = re.sub(pattern, replace_fn, content)

    # Atualizar og:image e twitter:image para WebP
    content = re.sub(
        r'(og:image\s+content=")[^"]+(")',
        r'\1assets/og-nexus-flow-tech.webp\2',
        content
    )
    content = re.sub(
        r'(twitter:image\s+content=")[^"]+(")',
        r'\1assets/og-nexus-flow-tech.webp\2',
        content
    )

    # Garantir loading="lazy" em todas as <img> sem ele
    img_pattern = r'<img\s+[^>]*?>'

    def ensure_lazy(match):
        img_tag = match.group(0)
        if 'loading=' in img_tag:
            return img_tag
        # Inserir antes do fechamento >
        return img_tag[:-1] + ' loading="lazy">'

    content = re.sub(img_pattern, ensure_lazy, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print('OK  ' + file_path + ' - otimizado')

def main():
    html_files = [
        'index.html',
        'sobre.html',
        'obrigado.html',
        'politica-de-privacidade.html',
    ]

    print("=" * 60)
    print("OTIMIZACAO HTML - WebP + Lazy Loading")
    print("=" * 60)
    print()

    for fp in html_files:
        if os.path.exists(fp):
            print('Processando ' + fp + '...')
            try:
                optimize_html_file(fp)
            except Exception as e:
                print('ERRO em ' + fp + ': ' + str(e))
        else:
            print('AVISO: Arquivo nao encontrado: ' + fp)

    print()
    print("=" * 60)
    print("Otimizacao HTML concluida!")
    print("=" * 60)

if __name__ == '__main__':
    main()
