# Projeto Miranha de P.A.

Pesquisa em materiais biomiméticos: avaliar e desenvolver um filamento sintético cientificamente plausível, inspirado na estrutura molecular e nas propriedades mecânicas da seda de aranha.

| Campo | Valor |
|---|---|
| Versão | 0.1.0 |
| Status | `concept_development`; estágio S1 (revisão de literatura) concluído em rascunho |
| Idioma | pt-BR · unidades SI |
| Especificação | [especificacao/projeto.json](especificacao/projeto.json) |

## Conclusões do S1 (resumo)

- **Fibra biomimética:** linha de pesquisa legítima. O desempenho do fio de ancoragem já foi reproduzido, mas só em laboratórios especializados com proteínas recombinantes **[D]**.
- **Dispositivo de pulso que forma e lança filamento:** especulativo **[E]**. A seda é *estirada*, não *ejetada*, e filamentos espessos não solidificam em voo **[T]**.
- ***Theraphosa blondi*:** não é uma boa referência. Não há dados mecânicos da sua seda, e a linhagem não tem o sistema de seda de alto desempenho das araneomorfas.
- **Próximo passo:** o experimento E1, uma caracterização estática, protegida e de baixa energia de fios comerciais, incluindo seda de *Bombyx mori*.

Detalhes e justificativas: [docs/S1_avaliacao_viabilidade.md](docs/S1_avaliacao_viabilidade.md).

## Estrutura

```
especificacao/projeto.json              Especificação original do projeto
docs/
  S1_avaliacao_viabilidade.md           Sumário executivo, viabilidade, estrutura molecular,
                                        materiais, formação, arquitetura, desempenho,
                                        mudanças recomendadas, plano S1–S5, custos, próximos passos
  bibliografia_anotada.md               Referências com DOI, anotação e status de verificação
  registro_de_riscos.md                 Riscos de segurança, científicos, regulatórios e de gestão
  protocolo_S3_bancada.md               Protocolo do experimento E1 (S3)
dados/
  matriz_materiais_preliminar.csv       Matriz S2 preliminar (valores, condições, tipo de dado, fonte)
  modelo_registro_ensaio_S3.csv         Modelo de registro de dados do E1
analises/
  ordens_de_grandeza.py                 Cálculos teóricos citados no S1 (sem dependências)
```

## Rótulos de evidência

| Rótulo | Significado |
|---|---|
| **[D]** | Demonstrado experimentalmente (publicação revisada por pares) |
| **[L]** | Suportado pela literatura, mas dependente de contexto |
| **[T]** | Teórico: cálculo de ordem de grandeza ou simulação |
| **[E]** | Especulativo |

## Política de segurança (resumo)

- Nenhum ensaio de suspensão humana nem de suporte do peso do corpo.
- Nenhum ensaio de queda nem de impacto com filamento experimental; esses ensaios ficam com laboratórios equipados.
- Nenhum lançador pressurizado improvisado.
- Nenhuma mistura de produtos químicos não identificados nem de formulações reativas perigosas.
- Amostras pequenas, fixações protegidas e ensaios estáticos controlados (no E1, cargas ≤ 50 N).
- Nenhum resultado do projeto deve ser apresentado como capacidade de suportar pessoas.

Detalhes: [docs/registro_de_riscos.md](docs/registro_de_riscos.md).

## Como reproduzir os cálculos

```bash
python3 analises/ordens_de_grandeza.py
```

Requer apenas Python 3. Os resultados são estimativas teóricas, com as hipóteses declaradas no próprio script, e não servem como critério de projeto.

## Arquivos CSV

Separador vírgula, decimal com ponto, UTF-8. No Excel em pt-BR, importar via *Dados → De texto/CSV* e escolher o separador vírgula.

## Limitações conhecidas

Os textos completos das referências não puderam ser abertos durante a elaboração do S1 (domínios bloqueados pela rede do ambiente). Os itens marcados "conferir" na bibliografia devem ser checados no original antes de qualquer uso externo.
