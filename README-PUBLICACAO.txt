NEXUS FLOW TECH — PUBLICAÇÃO

1. Envie todos os arquivos e a pasta assets para a raiz pública da hospedagem.
2. O formulário usa envio HTML nativo pelo FormSubmit. Ele funciona no celular sem abrir aplicativo de e-mail.
3. Na primeira submissão após a publicação, o FormSubmit enviará uma mensagem de ativação para marcel@nexusflowtech.com.br. Abra essa mensagem e confirme o formulário.
4. O envio deve ser testado com o site publicado em http:// ou https://. Ele não funciona corretamente ao abrir o HTML diretamente pelo gerenciador de arquivos.
5. Confirme se o domínio final é https://nexusflowtech.com.br. Caso seja outro, atualize canonical, Open Graph, sitemap.xml e robots.txt.
6. Antes da publicação definitiva, complete razão social, CNPJ/CPF e endereço na Política de Privacidade.

7. Esta versão usa menu mobile nativo (<details>), sem depender de JavaScript.
8. Após substituir os arquivos na hospedagem, limpe o cache do site/CDN e teste em aba anônima.


CORREÇÃO MOBILE DE CAMADAS E CLIQUES
- O header permanece fixed e não é mais sobrescrito por uma regra genérica.
- O menu mobile fica fora do stacking context do header e usa botão nativo com aria-expanded.
- Pseudo-elementos decorativos não recebem eventos de toque.
- CTAs têm área mínima de 44x44 px e scroll-padding para compensar o header fixo.
- Os IDs #contato, #como-funciona, #desafios, #mercados e #beneficios foram validados.
