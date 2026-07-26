# Prioridade 1 — Conversão da Homepage Nexus Flow Tech Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Melhorar a conversão da homepage da Nexus Flow Tech refinando a oferta de pré-diagnóstico, qualificando melhor os leads, ajustando CTAs e inserindo blocos de comparação/convencimento sem alterar o posicionamento central do site.

**Architecture:** A implementação deve ser incremental na landing page atual, preservando a identidade visual e estrutura existente. O foco é adicionar/ajustar seções de copy, CTAs e campos de formulário, mantendo HTML estático progressivo e funcionando sem JavaScript obrigatório.

**Tech Stack:** Site estático em HTML/CSS/JS hospedado na Vercel, formulário via FormSubmit, assets locais em `assets/`, âncoras internas e páginas auxiliares `sobre.html`, `politica-de-privacidade.html`, `obrigado.html`.

---

## Contexto verificado

Análise realizada no site publicado em `https://nexusflowtech.com.br/`.

Observações relevantes:

- A homepage já possui boa estrutura geral: hero, dores, soluções, abordagem, mercados, benefícios, diferenciais, depoimentos, CTA final, formulário e footer.
- O CTA principal atual é `Solicitar Pré-Diagnóstico Gratuito`.
- O formulário atual envia para `https://formsubmit.co/marcel@nexusflowtech.com.br` via `POST`.
- Campos atuais do formulário:
  - `nome` obrigatório.
  - `email` obrigatório.
  - `empresa` obrigatório.
  - `mensagem` obrigatório.
  - `consentimento_privacidade` obrigatório.
- Campos ocultos atuais:
  - `_subject`
  - `_template`
  - `_captcha=false`
  - `_next=https://nexusflowtech.com.br/obrigado.html`
  - `_autoresponse`
  - `_honey`
- Página `obrigado.html` existe e retorna HTTP 200.
- Console limpo durante navegação: sem erros JS observados.

## Escopo desta spec

Prioridade 1 da auditoria: **Conversão**.

Esta spec cobre:

1. Explicar melhor o que é o pré-diagnóstico gratuito.
2. Adicionar campo de WhatsApp no formulário.
3. Adicionar campo de principal dor/necessidade.
4. Ajustar CTA secundário `Ver Demonstração` para texto mais honesto e claro.
5. Criar seção `Antes e Depois` para tangibilizar valor.
6. Inserir CTA contextual no meio da página.
7. Atualizar validações e mensagens sem quebrar envio via FormSubmit.

Fora do escopo desta prioridade:

- Otimização de imagens/performance.
- Headers de segurança.
- GA4/GTM/Clarity.
- Páginas SEO por serviço/segmento.
- Redesign completo.
- Backend próprio para leads.

---

## Requisitos funcionais

### RF01 — Explicar o pré-diagnóstico gratuito

Adicionar uma seção ou bloco próximo ao primeiro CTA/formulário explicando claramente o que o visitante recebe ao solicitar o pré-diagnóstico.

Conteúdo mínimo:

- Mapeamento rápido dos processos manuais.
- Identificação de gargalos e retrabalho.
- Sugestões iniciais de automação, integração ou dashboard.
- Estimativa qualitativa de impacto: tempo, controle e redução de falhas.
- Próximos passos recomendados.

Copy sugerida:

```text
O que você recebe no pré-diagnóstico gratuito

Em uma análise inicial, identificamos onde sua operação perde tempo, quais processos podem ser automatizados e quais dados precisam estar conectados para apoiar decisões mais rápidas.

Você recebe:
- Um mapeamento rápido dos principais gargalos.
- Sugestões de automação, integração ou dashboard.
- Uma visão inicial de impacto esperado.
- Próximos passos para transformar a operação com segurança.
```

### RF02 — Adicionar campo WhatsApp

Adicionar campo no formulário:

- Label: `WhatsApp profissional`
- Nome técnico: `whatsapp`
- Tipo: `tel`
- Placeholder: `(11) 99999-9999`
- Obrigatoriedade: recomendado como obrigatório para conversão consultiva, mas pode ser opcional se a preferência for menor fricção.

Decisão recomendada: **obrigatório**.

Racional:

- O negócio é B2B consultivo.
- No Brasil, WhatsApp tende a converter melhor que email.
- A própria página já usa WhatsApp como canal principal no botão flutuante.

HTML sugerido:

```html
<label for="whatsapp">WhatsApp profissional *</label>
<input
  id="whatsapp"
  name="whatsapp"
  type="tel"
  placeholder="(11) 99999-9999"
  autocomplete="tel"
  required
/>
```

### RF03 — Adicionar campo de principal necessidade

Adicionar um `<select>` para qualificar o lead.

- Label: `Qual é sua principal necessidade?`
- Nome técnico: `principal_necessidade`
- Obrigatório: sim.

Opções recomendadas:

```html
<option value="">Selecione uma opção</option>
<option value="automatizar_tarefas_manuais">Automatizar tarefas manuais</option>
<option value="integrar_sistemas">Integrar sistemas</option>
<option value="criar_dashboard_power_bi">Criar dashboard / Power BI</option>
<option value="organizar_dados_planilhas">Organizar dados e planilhas</option>
<option value="aplicar_ia_operacao">Aplicar IA na operação</option>
<option value="reduzir_retrabalho">Reduzir retrabalho</option>
<option value="ainda_nao_sei">Ainda não sei exatamente</option>
</select>
```

### RF04 — Ajustar CTA secundário do hero

O CTA atual `Ver Demonstração` direciona para `#como-funciona`, mas não há uma demo real. Isso pode gerar expectativa errada.

Alterar para uma opção mais fiel:

- Preferência 1: `Ver como funciona`
- Preferência 2: `Entender a abordagem`
- Preferência 3: `Conhecer o processo`

Recomendado: **Ver como funciona**.

### RF05 — Criar seção `Antes e Depois`

Adicionar uma seção após `Sua empresa ainda enfrenta estes problemas?` ou após `Como ajudamos sua empresa`.

Objetivo: mostrar transformação de forma concreta.

Título sugerido:

```text
Antes e depois da automação
```

Subtítulo sugerido:

```text
A Nexus Flow Tech transforma processos manuais e dados espalhados em fluxos conectados, indicadores confiáveis e decisões mais rápidas.
```

Estrutura sugerida:

```text
Antes
- Dados espalhados em planilhas.
- Atualização manual de informações.
- Retrabalho entre áreas.
- Falta de indicadores confiáveis.
- Decisões lentas e reativas.

Depois
- Dados centralizados e integrados.
- Fluxos automatizados.
- Menos tarefas repetitivas.
- Dashboards em tempo real.
- Decisões baseadas em indicadores.
```

CTA dentro da seção:

```text
Quero identificar oportunidades na minha empresa
```

Destino: `#contato`.

### RF06 — Inserir CTA contextual no meio da página

Adicionar CTA após a seção `Como ajudamos sua empresa` ou após `Como funciona nossa abordagem`.

Copy sugerida:

```text
Quer saber quais desses gargalos existem na sua operação?
Solicite um pré-diagnóstico gratuito e receba uma análise inicial das oportunidades de automação, integração e indicadores para sua empresa.
```

Botão:

```text
Mapear meus gargalos agora
```

Destino: `#contato`.

### RF07 — Melhorar texto do CTA principal em pontos estratégicos

Manter a frase `Pré-Diagnóstico Gratuito` onde ela funciona, mas testar variações em CTAs de meio/final de página.

Variações recomendadas:

- `Quero descobrir onde posso automatizar`
- `Mapear gargalos da minha empresa`
- `Receber análise gratuita da operação`
- `Falar com um especialista`

Regra:

- Header pode manter `Solicitar Pré-Diagnóstico Gratuito`.
- Hero pode usar `Solicitar um pré-diagnóstico`.
- Meio de página deve usar CTA mais orientado à dor: `Mapear meus gargalos agora`.
- Seção Antes/Depois deve usar CTA orientado à transformação: `Quero identificar oportunidades na minha empresa`.

---

## Requisitos não funcionais

### RNF01 — Sem quebra do envio atual

O formulário deve continuar enviando para FormSubmit com os campos novos incluídos no payload.

### RNF02 — Sem dependência obrigatória de JavaScript

A página deve continuar funcional mesmo se JS falhar:

- Links de CTA devem funcionar com âncoras HTML.
- Formulário deve usar validação HTML nativa.
- Campos novos devem funcionar com `required`, `type`, `name` e `label` corretos.

### RNF03 — Acessibilidade

Todos os novos campos devem ter:

- `<label for="...">` associado a `id`.
- Nome visível e compreensível.
- Estado obrigatório indicado visualmente e via `required`.

Novos CTAs devem ter texto descritivo, evitando botões genéricos como `Clique aqui`.

### RNF04 — Consistência visual

Novas seções devem reutilizar classes e padrões existentes sempre que possível:

- Cards já existentes.
- Botões `.btn-primary` e `.btn-secondary`.
- Tags de seção/eyebrow se já existirem.
- Espaçamentos padrão de `section`.

### RNF05 — Mobile-first

A seção `Antes e Depois` deve funcionar bem em telas pequenas:

- Em desktop: duas colunas lado a lado.
- Em mobile: colunas empilhadas.
- Sem overflow horizontal.

---

## Arquivos provavelmente alterados

A confirmar após inspeção do repositório real.

Com base no HTML publicado, os prováveis arquivos são:

- `index.html` — copy, CTAs, novas seções e novos campos do formulário.
- Arquivo CSS embutido no `index.html` ou stylesheet equivalente — estilos da seção Antes/Depois e novos campos.
- Opcional: `obrigado.html` — caso deseje ajustar mensagem de sucesso com expectativa de prazo e próximo passo.

Se o projeto estiver estruturado com componentes, mapear equivalentes:

- Hero component.
- CTA component.
- Form/Contact component.
- Section components.
- Styles global/componentizados.

---

## Critérios de aceite

### CA01 — CTA secundário corrigido

Dado que o usuário acessa a homepage, quando visualiza o hero, então o CTA secundário deve exibir `Ver como funciona` ou texto equivalente, e deve apontar para `#como-funciona`.

### CA02 — Bloco do pré-diagnóstico visível

Dado que o usuário rola a página até a área de conversão, então deve encontrar uma explicação clara do que recebe no pré-diagnóstico gratuito.

### CA03 — Formulário qualifica lead

Dado que o usuário visualiza o formulário, então deve ver os campos:

- Nome.
- Email.
- WhatsApp profissional.
- Empresa.
- Principal necessidade.
- O que quer automatizar / mensagem.
- Consentimento de privacidade.

### CA04 — Formulário mantém envio

Dado que o usuário preenche todos os campos obrigatórios e aceita a política, quando envia o formulário, então o navegador deve submeter para FormSubmit e redirecionar para `https://nexusflowtech.com.br/obrigado.html` após sucesso.

Observação: em ambiente de teste, não enviar lead real para o email de produção sem confirmação. Validar HTML, payload e action; se fizer teste real, usar dados claramente marcados como teste.

### CA05 — Seção Antes/Depois implementada

Dado que o usuário navega pela homepage, então deve encontrar uma seção comparando o cenário antes e depois da automação, com CTA para `#contato`.

### CA06 — CTA contextual implementado

Dado que o usuário termina de ler a seção de soluções ou abordagem, então deve encontrar um CTA contextual convidando a mapear gargalos.

### CA07 — Sem regressões de console

Após carregar a página e interagir com CTAs/slider/form validation, o console do navegador não deve apresentar erros JavaScript.

---

## Plano de implementação

### Task 1: Localizar estrutura do projeto

**Objective:** Identificar os arquivos reais da homepage, CSS e formulário.

**Files:**
- Inspect: repo root.
- Inspect: `index.html` ou equivalente.
- Inspect: arquivos/componentes relacionados a Hero, Contact/Form e seções da homepage.

**Step 1: Inspecionar árvore do projeto**

Run:

```bash
find . -maxdepth 3 -type f | sort | sed 's#^./##' | head -200
```

Expected: lista de arquivos do projeto, incluindo `index.html` ou estrutura de framework.

**Step 2: Localizar textos atuais**

Run:

```bash
grep -R "Ver Demonstração\|Solicitar Pré-Diagnóstico\|diagnosticForm\|O que você quer automatizar" -n . --exclude-dir=node_modules --exclude-dir=.git
```

Expected: caminhos exatos dos arquivos a alterar.

**Step 3: Registrar arquivos reais**

Atualizar esta spec ou uma issue com os caminhos reais encontrados, se forem diferentes dos previstos.

---

### Task 2: Ajustar CTA secundário do hero

**Objective:** Corrigir expectativa do CTA secundário para refletir que ele leva à seção de abordagem, não a uma demo real.

**Files:**
- Modify: arquivo da homepage contendo `Ver Demonstração`.

**Step 1: Alterar texto**

Substituir:

```html
Ver Demonstração
```

Por:

```html
Ver como funciona
```

Preservar destino `#como-funciona`.

**Step 2: Verificar ocorrência duplicada**

Run:

```bash
grep -R "Ver Demonstração" -n . --exclude-dir=node_modules --exclude-dir=.git || true
grep -R "Ver como funciona" -n . --exclude-dir=node_modules --exclude-dir=.git
```

Expected: nenhuma ocorrência de `Ver Demonstração`; pelo menos uma ocorrência de `Ver como funciona`.

---

### Task 3: Adicionar bloco explicativo do pré-diagnóstico

**Objective:** Tornar claro o valor entregue antes do usuário enviar contato.

**Files:**
- Modify: `index.html` ou componente da área de contato/conversão.
- Modify: CSS correspondente, se necessário.

**Step 1: Inserir bloco de conteúdo antes do formulário ou antes do CTA final**

HTML base sugerido:

```html
<section class="diagnostic-explainer reveal" aria-labelledby="diagnostic-title">
  <div class="section-tag">
    <span></span>
    Diagnóstico gratuito
  </div>
  <h2 id="diagnostic-title">O que você recebe no pré-diagnóstico gratuito</h2>
  <p>
    Em uma análise inicial, identificamos onde sua operação perde tempo, quais processos podem ser automatizados
    e quais dados precisam estar conectados para apoiar decisões mais rápidas.
  </p>
  <div class="diagnostic-grid">
    <article>
      <h3>Mapeamento de gargalos</h3>
      <p>Identificação dos processos manuais, retrabalhos e pontos de perda de produtividade.</p>
    </article>
    <article>
      <h3>Oportunidades de automação</h3>
      <p>Sugestões iniciais de automação, integração de sistemas, dashboards ou IA aplicada.</p>
    </article>
    <article>
      <h3>Próximos passos</h3>
      <p>Uma visão prática do que pode ser feito primeiro para gerar impacto com segurança.</p>
    </article>
  </div>
</section>
```

**Step 2: Reutilizar estilos existentes**

Preferir classes de cards já existentes. Se necessário, criar apenas classes mínimas:

```css
.diagnostic-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
}

@media (max-width: 768px) {
  .diagnostic-grid {
    grid-template-columns: 1fr;
  }
}
```

**Step 3: Verificar âncoras e layout**

Abrir homepage local e confirmar que o bloco aparece antes do formulário ou em ponto de decisão natural.

---

### Task 4: Adicionar seção Antes e Depois

**Objective:** Tangibilizar a transformação operacional prometida pelo site.

**Files:**
- Modify: `index.html` ou componente de seções.
- Modify: CSS correspondente.

**Step 1: Inserir seção após dores ou soluções**

HTML base sugerido:

```html
<section id="antes-depois" class="before-after reveal" aria-labelledby="before-after-title">
  <div class="section-tag">
    <span></span>
    Antes e depois
  </div>
  <h2 id="before-after-title">Antes e depois da automação</h2>
  <p>
    Transformamos processos manuais e dados espalhados em fluxos conectados, indicadores confiáveis
    e decisões mais rápidas.
  </p>

  <div class="before-after-grid">
    <article class="before-card">
      <h3>Antes</h3>
      <ul>
        <li>Dados espalhados em planilhas.</li>
        <li>Atualização manual de informações.</li>
        <li>Retrabalho entre áreas.</li>
        <li>Falta de indicadores confiáveis.</li>
        <li>Decisões lentas e reativas.</li>
      </ul>
    </article>

    <article class="after-card">
      <h3>Depois</h3>
      <ul>
        <li>Dados centralizados e integrados.</li>
        <li>Fluxos automatizados.</li>
        <li>Menos tarefas repetitivas.</li>
        <li>Dashboards em tempo real.</li>
        <li>Decisões baseadas em indicadores.</li>
      </ul>
    </article>
  </div>

  <a class="btn-primary" href="#contato">Quero identificar oportunidades na minha empresa →</a>
</section>
```

**Step 2: Estilizar responsivo**

CSS base sugerido:

```css
.before-after-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 24px;
  margin: 40px 0;
}

.before-card,
.after-card {
  border-radius: 24px;
  padding: 32px;
  background: #fff;
  box-shadow: 0 16px 40px rgba(12, 34, 59, 0.08);
}

.before-card h3,
.after-card h3 {
  margin-bottom: 16px;
}

.before-card ul,
.after-card ul {
  display: grid;
  gap: 12px;
  padding-left: 20px;
}

@media (max-width: 768px) {
  .before-after-grid {
    grid-template-columns: 1fr;
  }
}
```

Ajustar cores para tokens CSS existentes do projeto, se houver.

---

### Task 5: Inserir CTA contextual no meio da página

**Objective:** Capturar usuários convencidos antes do final da página.

**Files:**
- Modify: `index.html` ou componente após soluções/abordagem.

**Step 1: Adicionar bloco CTA**

HTML sugerido:

```html
<section class="mid-cta reveal" aria-label="Chamada para mapear gargalos">
  <div class="mid-cta-content">
    <h2>Quer saber quais desses gargalos existem na sua operação?</h2>
    <p>
      Solicite um pré-diagnóstico gratuito e receba uma análise inicial das oportunidades de automação,
      integração e indicadores para sua empresa.
    </p>
    <a class="btn-primary" href="#contato">Mapear meus gargalos agora →</a>
  </div>
</section>
```

**Step 2: Reutilizar estilo de CTA final**

Se já existir uma seção de CTA final, reaproveitar a classe dela para evitar CSS duplicado. Só criar `.mid-cta` se necessário.

---

### Task 6: Atualizar formulário com WhatsApp e principal necessidade

**Objective:** Qualificar melhor os leads e facilitar contato comercial.

**Files:**
- Modify: formulário em `index.html` ou componente equivalente.

**Step 1: Adicionar campo WhatsApp após email**

HTML:

```html
<label for="whatsapp">WhatsApp profissional *</label>
<input
  id="whatsapp"
  name="whatsapp"
  type="tel"
  placeholder="(11) 99999-9999"
  autocomplete="tel"
  required
/>
```

**Step 2: Adicionar select de principal necessidade antes da mensagem**

HTML:

```html
<label for="principal_necessidade">Qual é sua principal necessidade? *</label>
<select id="principal_necessidade" name="principal_necessidade" required>
  <option value="">Selecione uma opção</option>
  <option value="automatizar_tarefas_manuais">Automatizar tarefas manuais</option>
  <option value="integrar_sistemas">Integrar sistemas</option>
  <option value="criar_dashboard_power_bi">Criar dashboard / Power BI</option>
  <option value="organizar_dados_planilhas">Organizar dados e planilhas</option>
  <option value="aplicar_ia_operacao">Aplicar IA na operação</option>
  <option value="reduzir_retrabalho">Reduzir retrabalho</option>
  <option value="ainda_nao_sei">Ainda não sei exatamente</option>
</select>
```

**Step 3: Ajustar estilos do select**

Garantir que `select` receba o mesmo estilo visual de `input` e `textarea`.

Exemplo:

```css
.form-group input,
.form-group textarea,
.form-group select {
  /* estilos já existentes */
}
```

Ajustar para os nomes reais das classes do projeto.

**Step 4: Verificar payload FormSubmit**

Campos com `name` devem ser enviados automaticamente pelo FormSubmit.

Não remover campos ocultos existentes.

---

### Task 7: Ajustar microcopy do formulário

**Objective:** Reduzir fricção e aumentar confiança antes do envio.

**Files:**
- Modify: área de formulário.

**Step 1: Adicionar texto curto acima do formulário**

Copy sugerida:

```text
Preencha os dados abaixo e conte rapidamente qual processo, sistema ou rotina mais trava sua operação. Nossa equipe retorna com uma análise inicial e próximos passos recomendados.
```

**Step 2: Ajustar placeholder da mensagem**

Atual:

```text
Descreva o processo, sistema ou dor principal
```

Sugestão:

```text
Ex.: usamos planilhas para controlar pedidos e perdemos tempo atualizando relatórios manualmente
```

---

### Task 8: Validar localmente

**Objective:** Garantir que alterações não quebraram navegação, layout e formulário.

**Files:**
- Test: homepage local.

**Step 1: Rodar servidor local conforme stack do projeto**

Se for HTML estático:

```bash
python3 -m http.server 4173
```

Se for Vite/Node:

```bash
npm install
npm run dev
```

Se houver script específico no `package.json`, usar o script existente.

**Step 2: Validar no navegador**

Checklist:

- Hero carrega corretamente.
- CTA secundário aponta para `#como-funciona`.
- Seção Antes/Depois aparece e fica responsiva.
- CTA contextual aponta para `#contato`.
- Formulário possui campos novos.
- Validação HTML bloqueia envio sem campos obrigatórios.
- Checkbox de privacidade continua obrigatório.
- Console sem erros.

**Step 3: Validar busca textual**

Run:

```bash
grep -R "Ver Demonstração" -n . --exclude-dir=node_modules --exclude-dir=.git || true
grep -R "whatsapp\|principal_necessidade\|Antes e depois da automação\|Mapear meus gargalos" -n . --exclude-dir=node_modules --exclude-dir=.git
```

Expected:

- `Ver Demonstração` não aparece mais.
- Novos textos/campos aparecem nos arquivos corretos.

---

## Testes recomendados

### Teste manual 1 — Validação de formulário vazio

1. Abrir homepage.
2. Ir para `#contato`.
3. Clicar em enviar sem preencher.
4. Resultado esperado: navegador bloqueia envio e destaca campos obrigatórios.

### Teste manual 2 — Campos novos obrigatórios

1. Preencher nome, email, empresa e mensagem.
2. Deixar WhatsApp vazio.
3. Marcar consentimento.
4. Enviar.
5. Resultado esperado: navegador bloqueia por WhatsApp obrigatório.

Depois:

1. Preencher WhatsApp.
2. Deixar principal necessidade em `Selecione uma opção`.
3. Enviar.
4. Resultado esperado: navegador bloqueia por select obrigatório.

### Teste manual 3 — CTAs

Validar que todos apontam corretamente:

- Header: `#contato`.
- Hero principal: `#contato`.
- Hero secundário: `#como-funciona`.
- CTA contextual: `#contato`.
- CTA Antes/Depois: `#contato`.
- CTA final: `#contato`.

### Teste manual 4 — Mobile

Em viewport mobile:

- Hero não deve ter overflow horizontal.
- Antes/Depois deve empilhar cards.
- Formulário deve ficar legível.
- Select deve ocupar largura correta.
- Botões devem ser fáceis de tocar.

---

## Riscos e decisões

### Risco 1 — Formulário com campos demais reduzir conversão

Adicionar WhatsApp e principal necessidade aumenta qualificação, mas também adiciona fricção.

Mitigação:

- Manter apenas dois campos novos.
- Usar labels claros.
- Evitar pedir dados sensíveis ou complexos.

### Risco 2 — WhatsApp obrigatório pode afastar alguns leads

Decisão recomendada: obrigatório, pois venda consultiva no Brasil depende muito de contato rápido.

Alternativa:

- Tornar WhatsApp opcional e medir conversão depois com analytics.

### Risco 3 — Seção nova alongar demais a homepage

Mitigação:

- Antes/Depois deve ser visual, curto e escaneável.
- Não criar parágrafos longos.
- Usar bullets e CTA claro.

### Risco 4 — Duplicar estilos

Mitigação:

- Reutilizar classes existentes sempre que possível.
- Só criar CSS novo quando não houver padrão existente.

---

## Verificação pós-deploy

Após publicar:

1. Acessar `https://nexusflowtech.com.br/`.
2. Limpar cache ou usar janela anônima.
3. Validar hero e CTAs.
4. Validar seção Antes/Depois.
5. Validar formulário e campos novos.
6. Verificar console do navegador.
7. Validar que `obrigado.html` continua abrindo.
8. Fazer teste controlado de formulário somente se autorizado, usando dados marcados como teste.

---

## Resultado esperado

Após esta prioridade, a homepage deve deixar mais claro:

- por que o visitante deve solicitar contato;
- o que ele recebe no pré-diagnóstico;
- quais problemas podem ser mapeados;
- como a operação muda antes/depois;
- como a Nexus Flow Tech pode retornar com uma análise útil.

A melhoria esperada é aumento de cliques em CTA e maior qualidade dos leads enviados pelo formulário.
