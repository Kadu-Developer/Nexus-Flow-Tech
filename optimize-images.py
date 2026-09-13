#!/usr/bin/env python3
"""
Script de otimizacao de imagens para Nexus Flow Tech
Converte PNG/JPEG para WebP com compressao otimizada
"""

from PIL import Image
import os

def convert_to_webp(input_path, output_path, quality=80, method=6):
    img = Image.open(input_path)
    if img.mode in ('RGBA', 'P'):
        if img.mode == 'P' and 'transparency' in img.info:
            img = img.convert('RGBA')
    img.save(output_path, 'WEBP', quality=quality, method=method, lossless=False)
    return output_path

def main():
    files_to_optimize = [
        ('assets/nexus-flow-tech-logo.png', 'assets/nexus-flow-tech-logo.webp', 95),
        ('assets/jose-carlos.png', 'assets/jose-carlos.webp', 85),
        ('assets/marcel-wachowicz.jpeg', 'assets/marcel-wachowicz.webp', 85),
        ('assets/og-nexus-flow-tech.jpg', 'assets/og-nexus-flow-tech.webp', 85),
    ]

    segmentos = [
        'segmento-agronegocio', 'segmento-comercio', 'segmento-construcao-civil',
        'segmento-distribuicao', 'segmento-financeiro', 'segmento-industria',
        'segmento-logistica', 'segmento-prestacao-servicos', 'segmento-saude',
    ]

    for seg in segmentos:
        files_to_optimize.append(
            (f'assets/{seg}.png', f'assets/{seg}.webp', 80)
        )

    print("=" * 60)
    print("OTIMIZACAO DE IMAGENS - Nexus Flow Tech")
    print("=" * 60)
    print()

    total_before = 0
    total_after = 0

    for input_path, output_path, quality in files_to_optimize:
        if not os.path.exists(input_path):
            print(f"ERRO: Arquivo nao encontrado: {input_path}")
            continue

        size_before = os.path.getsize(input_path)

        try:
            convert_to_webp(input_path, output_path, quality=quality)
            size_after = os.path.getsize(output_path)
            reduction = (1 - size_after / size_before) * 100
            status = "+" if size_after < size_before else "!"
            print(
                f"{status} {os.path.basename(input_path):40} "
                f"{size_before/1024:6.1f}KB -> {size_after/1024:6.1f}KB "
                f"({reduction:+.0f}%)"
            )
            total_before += size_before
            total_after += size_after
        except Exception as e:
            print(f"ERRO convertendo {input_path}: {e}")

    print()
    print("=" * 60)
    print(f"RESUMO: {total_before/1024/1024:.2f}MB -> {total_after/1024/1024:.2f}MB")
    print(f"Economia total: {(1 - total_after/total_before)*100:.1f}%")
    print("=" * 60)

if __name__ == '__main__':
    main()
