# Registro de riscos — Projeto Miranha de P.A.

| Campo | Valor |
|---|---|
| Versão / data | 0.1 — 29/10/2026 |
| Escopo | Estágios S1–S5 e conceito de longo prazo |
| Revisão | Ao fim de cada estágio e antes de qualquer novo procedimento experimental |

**Escalas.** Probabilidade (P) e impacto (I): B = baixo, M = médio, A = alto, C = crítico (impacto à integridade física ou risco irreversível). **Nível:** combinação de P e I. Riscos com impacto C são tratados como prioritários mesmo com probabilidade baixa.

**Categorias:** SEG (segurança física), CIE (científico/metodológico), TEC (técnico), REG (regulatório/ético), GES (gestão/custo).

## Riscos

| ID | Risco | Cat. | P | I | Nível | Mitigação | Indicador / gatilho | Estágio |
|---|---|---|---|---|---|---|---|---|
| R01 | Lesão ocular por chicoteamento da fibra ou do fragmento na ruptura | SEG | M | A | **Alto** | Óculos EN 166 / ANSI Z87.1 sempre; anteparo de policarbonato; cargas ≤ 50 N (energia ≲ 1 J por corpo de prova) | Qualquer ensaio sem anteparo ou óculos interrompe a sessão | S3, S4 |
| R02 | Queda do recipiente de carga sobre mãos ou pés | SEG | B | M | Médio | Bandeja acolchoada a ≤ 3 cm; massa ≤ 5,5 kg; água adicionada de fora da zona de carga | Folga > 3 cm na carga máxima | S3 |
| R03 | Corte na pele por fios finos de alta resistência (UHMWPE, aramida) sob tensão | SEG | M | M | Médio | Nunca enrolar nos dedos; luvas anticorte ao tensionar; cortar sem tensão | Incidente ou quase-incidente registrado | S3, S4-A |
| R04 | Extrapolar resultados estáticos para capacidade de suportar pessoas | SEG / CIE | A | C | **Crítico** | Política escrita (S1, Seção 8.3); avisos em todos os relatórios; proibição de ensaios com pessoas; ensaios dinâmicos só em laboratório credenciado | Qualquer menção a "aguenta uma pessoa" em comunicação do projeto | Todos |
| R05 | Construção improvisada de lançador pressurizado, pirotécnico ou com mola de alta energia | SEG | M | C | **Crítico** | Fora do escopo e proibido pelas restrições do projeto; revisão de segurança obrigatória antes de qualquer subsistema de projeção | Proposta de projeção ou de armazenamento de energia | S4 em diante |
| R06 | Exposição a solventes ou reagentes perigosos em tentativas de fiação (HFIP, H₂SO₄ concentrado, isocianatos, LiBr concentrado, monômeros acrílicos) | SEG | M | A | **Alto** | Bancada restrita a alginato e CaCl₂ de grau alimentício; demais rotas só em laboratório parceiro, com FDS/FISPQ, capela e EPI | Proposta de reagente fora da lista aprovada | S4 |
| R07 | Irritação cutânea, ocular ou respiratória por cerdas urticantes de *T. blondi* ou de suas sedas | SEG | B | M | Baixo | Sem animais vivos e sem manuseio de sedas de tarântulas; espécie tratada só pela literatura | Qualquer proposta de aquisição de animal ou de material biológico | S1–S2 |
| R08 | Erro na seção transversal leva a resistência (GPa) incorreta | CIE | A | M | **Alto** | Métrica primária em cN/tex, por pesagem; densidade declarada como hipótese; MEV via parceiro se necessário | Divergência > 20 % entre GPa calculado e literatura | S3 |
| R09 | Variabilidade alta (CV 10–50 % em sedas) mascara as diferenças entre materiais | CIE | A | M | **Alto** | n ≥ 10 válidos; ordem aleatória; IC 95 %; condicionamento | CV acima do critério de aceitação | S3 |
| R10 | Efeito não controlado de umidade e temperatura | CIE | A | M | **Alto** | Registro em todos os ensaios; condicionamento; E1-c (úmido × condicionado); caixa com sal saturado (nível 1) | Variação de UR > 15 pontos percentuais dentro de uma série | S3 |
| R11 | Rupturas na garra invalidam os dados | CIE | A | B | Médio | Garras tipo cabrestante; classificação V/G/S; revisão se G > 20 % | G > 20 % | S3 |
| R12 | Fluência durante os patamares distorce as curvas | CIE | M | M | Médio | Tempo de patamar fixo e relatado; subensaio E1-b quantifica a fluência | Deformação crescente visível dentro de um patamar | S3 |
| R13 | Trabalho com OGM (espidroínas recombinantes) sem CQB / CTNBio (Lei nº 11.105/2005) | REG | B | A | Médio | Somente via instituição credenciada | Proposta de expressão de proteína | S4-C |
| R14 | Acesso a patrimônio genético nativo sem cadastro no SisGen (Lei nº 13.123/2015) | REG | B | M | Baixo | Consulta institucional antes de usar sequências ou amostras de espécies nativas | Uso de sequência de espécie brasileira | S2, S4-C |
| R15 | Custo e prazo de fibras proteicas subestimados | GES | A | M | **Alto** | Parceria; marcos com decisão de continuar ou parar; prioridade para fibras comerciais | Orçamento de S4-C > teto definido | S4 |
| R16 | Viés de fontes (comunicados de imprensa, resumos de congresso, fichas comerciais) | CIE | M | M | Médio | Rótulos de evidência; conferir os textos completos; coluna `verificacao` na matriz | Valor citado sem fonte primária | S1–S2 |
| R17 | Expectativa de produto (o "lançador") dirigindo decisões científicas | GES / SEG | M | A | **Alto** | Critérios de decisão escritos; revisão em S5; separar trilha científica e conceito | Decisão sem dado medido que a sustente | Todos |
| R18 | Degradação ou contaminação microbiana de soluções de alginato ou proteína armazenadas | TEC | M | B | Baixo | Preparar na hora; refrigerar; descartar após prazo definido no protocolo de S4-B | Turvação, odor, mudança de viscosidade | S4-B |
| R19 | Pinçamento de dedos em fixações e grampos | SEG | B | B | Baixo | Montar sem carga; ferramentas adequadas | Incidente | S3 |
| R20 | Descarte inadequado de resíduos (soluções salinas, géis) | REG | B | B | Baixo | Seguir as regras locais de descarte; volumes pequenos | — | S4-B |
| R21 | Choque elétrico por equipamento próximo à água (E1-c, S4-B) | SEG | B | A | Médio | Equipamentos afastados da área molhada; tomadas com DR; sem eletrofiação | Água próxima de equipamento energizado | S3, S4 |
| R22 | Domínios de revistas bloqueados impedem conferir as fontes (situação desta revisão) | CIE | A | B | Médio | Liberar os domínios na rede do ambiente ou usar a biblioteca institucional; itens "conferir" listados | Item citado externamente ainda com status "conferir" | S1 |

## Riscos de maior nível (ordem de tratamento)

1. **R04:** extrapolação para suporte humano (crítico)
2. **R05:** lançador improvisado (crítico)
3. **R01, R06:** lesão ocular; reagentes perigosos
4. **R08, R09, R10:** confiabilidade das medições
5. **R15, R17:** custo e expectativa de produto

## Histórico

| Versão | Data | Alteração |
|---|---|---|
| 0.1 | 29/10/2026 | Criação, com a avaliação S1 |
