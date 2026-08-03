# Subdivisão das aulas práticas — 12 aulas

As seis aulas extensas da trilha baseada no livro serão tratadas como **módulos**. Cada módulo foi dividido em duas aulas práticas, totalizando 12 encontros com progressão contínua, checkpoints no Git e avaliação automática.

## Organização comum

- preparação por aula invertida no Moodle;
- síntese teórica e diagnóstico inicial;
- demonstração curta do professor;
- laboratório de 90 a 120 minutos;
- pelo menos um `commit` de checkpoint;
- `push` para execução automática dos testes;
- fechamento com análise das evidências;
- aprofundamento individual para itens não concluídos em sala.

## Módulo 1 — Qualidade, TDD e Git

### Aula 1 — Ambiente, qualidade e primeiro teste vermelho

- Aceitar a atividade individual no GitHub Classroom.
- Clonar o repositório com GitHub Desktop ou Git.
- Revisar qualidade, níveis de teste e ciclo TDD.
- Preparar o ambiente e executar a suíte inicial.
- Criar o primeiro teste funcional com falha esperada.
- Checkpoint: `test: registra primeiro cenário funcional`.
- Autograding: ambiente, descoberta e execução dos testes.

### Aula 2 — Verde mínimo, refatoração e pull request

- Implementar somente o necessário para o teste passar.
- Criar testes unitários para o comportamento central.
- Refatorar mantendo a suíte verde.
- Abrir pull request e registrar evidências.
- Checkpoints: `feat: implementa comportamento mínimo` e `refactor: melhora solução`.
- Autograding: casos básicos, regressão e qualidade estática inicial.

## Módulo 2 — Projeto de testes, interação e persistência

### Aula 3 — Técnicas de projeto e interação do usuário

- Aplicar particionamento de equivalência e valores-limite.
- Criar testes parametrizados.
- Atualizar testes web para localizadores atuais.
- Substituir esperas fixas por condições explícitas.
- Checkpoint: `test: adiciona partições, limites e interação`.
- Autograding: casos-limite e fluxo principal da interface.

### Aula 4 — Banco de dados, isolamento e regressão

- Preparar fixtures e dados isolados.
- Evitar contaminação do banco de desenvolvimento.
- Identificar e reproduzir uma regressão.
- Registrar o defeito em issue.
- Checkpoint: `test: isola persistência e cobre regressão`.
- Autograding: persistência, isolamento e regressão.

## Módulo 3 — Integração, API e test doubles

### Aula 5 — Contratos e testes de integração

- Mapear dependências e fronteiras da aplicação.
- Definir contrato, entradas, saídas e códigos HTTP.
- Criar coleção de API no Postman ou equivalente.
- Separar testes unitários e de integração por marcadores.
- Checkpoint: `test: adiciona integração da API`.
- Autograding: rotas, persistência e respostas HTTP.

### Aula 6 — Doubles, mocks e testabilidade

- Comparar fake, stub, mock e spy.
- Isolar serviço externo ou dependência instável.
- Testar autenticação sem Gmail nem credenciais reais.
- Justificar a escolha do test double.
- Checkpoint: `test: isola dependência externa`.
- Autograding: comportamento isolado e tratamento de falhas.

## Módulo 4 — Métricas e refatoração

### Aula 7 — Cobertura e baseline de qualidade

- Medir cobertura de instruções e branches.
- Executar análise estática.
- Identificar código crítico sem testes relevantes.
- Registrar baseline e limitações das métricas.
- Checkpoint: `chore: registra baseline de qualidade`.
- Autograding: cobertura mínima e análise estática.

### Aula 8 — Refatoração orientada por risco

- Priorizar melhorias com base em risco.
- Selecionar um smell ou dívida técnica.
- Refatorar com a suíte protegendo o comportamento.
- Comparar métricas antes e depois.
- Checkpoint: `refactor: reduz dívida técnica selecionada`.
- Avaliação: relatório crítico e pipeline aprovado.

## Módulo 5 — Integração contínua e automação

### Aula 9 — GitHub Actions e gates de qualidade

- Ler e interpretar o workflow existente.
- Automatizar instalação, testes e cobertura.
- Acrescentar análise estática e limite de qualidade.
- Investigar deliberadamente uma falha de pipeline.
- Checkpoint: `ci: adiciona pipeline e gates de qualidade`.
- Autograding: execução completa do pipeline.

### Aula 10 — Automação de API e interface

- Automatizar um fluxo crítico com Playwright, Selenium ou Postman.
- Separar verificações rápidas e lentas.
- Reduzir flakiness e melhorar diagnóstico.
- Realizar revisão por pares.
- Checkpoint: `test: automatiza fluxo crítico`.
- Avaliação: automação, estabilidade e pull request revisado.

## Módulo 6 — IA e Projeto Integrador

### Aula 11 — IA aplicada à elaboração de testes

- Usar IA para propor casos de borda.
- Classificar sugestões válidas, redundantes e incorretas.
- Implementar somente casos tecnicamente validados.
- Registrar ferramenta, finalidade, prompts e validações.
- Checkpoints: `docs: registra análise crítica da IA` e `test: implementa casos validados`.
- Avaliação: qualidade da validação, não quantidade de conteúdo gerado.

### Aula 12 — Consolidação, release e retrospectiva

- Consolidar testes, métricas, documentação e pipeline.
- Revisar evidências do Projeto Integrador.
- Criar release final.
- Apresentar limitações, resultados e retrospectiva.
- Checkpoint: `release: consolida projeto integrador`.
- Avaliação: produto, qualidade técnica, colaboração e domínio individual.

## Distribuição entre tipos de atividade

- Aulas 1 a 4: prioritariamente individuais.
- Aulas 5 e 6: individual ou dupla.
- Aulas 7 e 8: individual, com discussão coletiva das métricas.
- Aulas 9 e 10: equipes de 3 a 5 estudantes.
- Aulas 11 e 12: equipes do Projeto Integrador, com evidência individual.
- As equipes e os repositórios permanecem separados entre 4A e 4B.

## Estratégia no GitHub Classroom

- Um repositório progressivo pode abranger as duas aulas de cada módulo.
- Atividades que geram nota isolada devem ser publicadas separadamente.
- O autograding deve usar vários critérios e evitar avaliação “tudo ou nada”.
- Alterações em testes e workflows devem ser sinalizadas para revisão do professor.
- A nota automática deve ser complementada por autoria, análise crítica e colaboração.

