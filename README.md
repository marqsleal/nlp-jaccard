# JACCARD NLP - Jaccard Index
_Projeto para fins acadêmicos criando uma implementação manual do Índice de Jaccard na linguagem Python._

## Dependências 

Para instalar as dependências do projeto, execute:

```bash
pip install -r requirements.txt
```

## Instalação 

1. Clone o repositório:

```bash
git clone https://github.com/marqsleal/nlp-jaccard.git
```

2. Execute o arquivo `test.py`:

```bash
python3 test.py
```
## Índice de Jaccard

O Índice de Jaccard mede a similaridade entre dois conjuntos. Ele é calculado dividindo o tamanho da interseção dos conjuntos pelo tamanho da união deles.

Em NLP, é possível utilizar o Índice de Jaccard para comparar a similaridade entre dois textos, considerando palavras ou n-grams (sequências de n palavras consecutivas). Isso pode ser útil para tarefas como detecção de plágio ou análise de duplicatas de textos.

## Código:

```python
def jaccard_index(token1: str, token2: str, printIndex=False) -> float:

    token1 = unidecode(token1.lower())
    token2 = unidecode(token2.lower())

    words_token1 = set(token1.split()) 
    words_token2 = set(token2.split())

    intersection = words_token1.intersection(words_token2)

    union = words_token1.union(words_token2)

    index = float(len(intersection)) / len(union)

    return index
```

- Utilizando `set()` pois permite um acesso rápido, guardando os itens em uma coleção de elementos únicos e não-ordenados;
- Utilizando `unidecode` para normalização;

## **BONUS**: Jaccard com SQL

Considerando:
```sql
CREATE TABLE A (
    word VARCHAR(100)
);

CREATE TABLE B (
    word VARCHAR(100)
);
```

### Interseção (A ∩ B): O número de palavras que aparecem em ambas as tabelas:

```sql
SELECT COUNT(DISTINCT A.word) AS intersection_count
FROM A
INNER JOIN B
ON A.word = B.word;
```

### União (A ∪ B): O número total de palavras únicas em ambas as tabelas:

```sql
SELECT COUNT(DISTINCT word) AS union_count
FROM (
    SELECT word FROM A
    UNION
    SELECT word FROM B
) AS union_table;
```

### Jaccard Index: Calculando a razão entre a interseção e a união:

```sql
WITH Intersect AS (
    SELECT COUNT(DISTINCT A.word) AS intersection_count
    FROM A
    INNER JOIN B
    ON A.word = B.word
),
UnionSet AS (
    SELECT COUNT(DISTINCT word) AS union_count
    FROM (
        SELECT word FROM A
        UNION
        SELECT word FROM B
    ) AS union_table
)
SELECT
    (SELECT intersection_count FROM Intersect) / (SELECT union_count FROM UnionSet) AS jaccard_index;
```