FROM python:3.12.8-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml ./

RUN uv pip install -r pyproject.toml --system

COPY . .

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]