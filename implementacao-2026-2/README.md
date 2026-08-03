# TODO Quality Lab — aulas 1 e 2

Template executável da disciplina **Testes, Métricas e Qualidade de Software — 2026/2**.

Este laboratório preserva a aplicação TODO da trilha baseada em *Test-Driven Development with Python*, atualizada para o fluxo com PyTest, GitHub Classroom e GitHub Actions.

## Preparação

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py manage.py migrate
pytest
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
pytest
```

## Executar a aplicação

```bash
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/`.

## Qualidade

```bash
pytest
pytest --cov=lists --cov-branch --cov-report=term-missing
ruff check .
ruff format --check .
```

## Fluxo das aulas 1 e 2

1. Execute a suíte e interprete os testes.
2. Crie uma issue para um novo comportamento.
3. Escreva primeiro o teste que falha.
4. Faça um commit `test:`.
5. Implemente o mínimo necessário e faça um commit `feat:`.
6. Refatore, faça um commit `refactor:` e abra um pull request.

O professor pode introduzir falhas ou testes adicionais no GitHub Classroom. Não altere os workflows ou testes para contornar a avaliação.

