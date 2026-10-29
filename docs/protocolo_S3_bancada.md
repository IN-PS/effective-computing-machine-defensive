# Protocolo S3 — Experimento E1: caracterização estática comparativa de fios comerciais finos

| Campo | Valor |
|---|---|
| Estágio | S3 (caracterização segura em bancada) |
| Versão / data | 0.1 — 29/10/2026 (rascunho; revisar antes do piloto) |
| Documento base | [S1_avaliacao_viabilidade.md](S1_avaliacao_viabilidade.md), Seções 10–12 |
| Riscos associados | [registro_de_riscos.md](registro_de_riscos.md): R01, R02, R03, R08–R12, R19 |
| Modelo de registro | [dados/modelo_registro_ensaio_S3.csv](../dados/modelo_registro_ensaio_S3.csv) |

## 1. Objetivo

Medir, nas mesmas condições e com um método de baixo custo e baixa energia:

- a **densidade linear** (tex), a **carga de ruptura** e a **resistência específica** (cN/tex);
- a **deformação na ruptura** e o **trabalho de ruptura por massa** (J/g);
- a **fluência** em 30 % e 50 % da carga média de ruptura;
- a **repetibilidade** (CV) e o **modo de falha**;

de um painel de cinco fios comerciais, incluindo seda de *Bombyx mori* como referência biológica acessível. Os resultados alimentam a matriz S2 e validam o método antes de qualquer fibra experimental.

**Hipóteses** (ver S1, Seção 11):

- **H1:** ordem de resistência específica: UHMWPE > para-aramida > náilon ≈ poliéster > seda.
- **H2:** seda e náilon apresentam maior deformação na ruptura e maior trabalho de ruptura por massa do que UHMWPE e para-aramida.
- **H3:** CV ≤ 10 % na carga de ruptura do náilon de referência.
- **H4:** a 50 % da carga média de ruptura, a fluência em 1 h é maior no UHMWPE e no náilon do que na para-aramida.

## 2. Escopo

**Dentro do escopo:** ensaios estáticos de tração em corpos de prova curtos (~100 mm úteis), com carga crescente aplicada por adição controlada de água, dentro de uma fixação protegida.

**Fora do escopo:** qualquer ensaio com pessoas, ensaios de queda ou impacto, cargas acima de 50 N, reagentes químicos e qualquer dispositivo de lançamento.

**Limitação metodológica:** o carregamento estático incremental **não equivale** aos ensaios normalizados de tração a taxa constante (ASTM D3822/D3822M para fibras isoladas; ASTM D2256 / ISO 2062 para fios). Os resultados valem para **comparação interna**. Valores normalizados devem ser obtidos em máquina universal, via laboratório parceiro.

## 3. Limites de segurança obrigatórios

| # | Limite | Valor | Justificativa |
|---|---|---|---|
| L1 | Carga de ruptura declarada de cada material | **≤ 50 N** (~5,1 kg) | Energia elástica armazenada ≲ 1 J por corpo de prova [T]: ~0,15 J para náilon de 15 N (script, bloco 5); ~0,9 J no pior caso (50 N, 25 % de deformação, 150 mm livres, aproximação linear) |
| L2 | Massa total pendurada | ≤ 5,5 kg | Cobre L1 com margem |
| L3 | Distância do fundo do recipiente à bandeja acolchoada | **≤ 3 cm** | Queda do recipiente < 2 J; sem risco para mãos ou pés |
| L4 | Proteção | Óculos de proteção (EN 166 / ANSI Z87.1) **sempre**; anteparo de policarbonato entre o corpo de prova e o operador | Chicoteamento da fibra ao romper |
| L5 | Zona de carga | Nenhuma parte do corpo sob o recipiente; água adicionada por funil e tubo a partir de fora do anteparo | Evita esmagamento |
| L6 | Manuseio de UHMWPE e para-aramida | Nunca enrolar nos dedos; usar luvas anticorte ao tensionar à mão; cortar com tesoura adequada, sem tensão | Fios finos de alta resistência cortam a pele |
| L7 | Ensaios longos (fluência) | Sinalizar o posto; manter o anteparo; não deixar recipientes carregados ao alcance de terceiros | Evita contato acidental |

**Critérios de interrupção:** a carga passa de 50 N sem ruptura; a fixação ou o pórtico se desloca; o anteparo é removido; alguém entra na zona de carga. Nesses casos, **parar, descarregar com cuidado (retirar água pelo tubo) e registrar**.

## 4. Painel de materiais

| Código | Material | Especificação de compra | Papel no ensaio |
|---|---|---|---|
| P1 | Náilon (poliamida), monofilamento | Linha fina, ~0,10–0,15 mm, carga declarada ≤ ~30 N | **Referência do método** (H3) |
| P2 | Poliéster (PET), multifilamento | Linha de costura fina | Sintético comum |
| P3 | Seda de *Bombyx mori* 100 %, filamento contínuo | Linha de seda de filamento (não usar seda fiada de fibras curtas) | Referência biológica |
| P4 | UHMWPE, multifilamento trançado | A linha mais fina disponível, com carga declarada ≤ ~40 N | Alta resistência, baixa extensibilidade, fluência |
| P5 | Para-aramida, multifilamento | Linha de costura fina | Alta resistência, alta rigidez |

Registrar, para cada material: fabricante, produto, lote, diâmetro ou tex declarado, carga declarada **e as condições em que foi declarada**. Rótulos de linhas de pesca nem sempre seguem norma **[L]**; trate-os como indicativos.

**Quantidade por material:** cerca de 15 corpos de prova de 350 mm, 5 segmentos para a medida de tex e 6 corpos de prova de fluência, ou seja, ~15 m. Comprar ≥ 25 m.

**Se a carga declarada for desconhecida:** fazer um único piloto com incrementos de 1 N. Se passar de 50 N sem romper, **excluir** o material ou trocá-lo por uma versão mais fina.

## 5. Equipamento

- Pórtico rígido (madeira ou perfil de alumínio) fixado à bancada.
- Duas garras tipo cabrestante: cilindros lisos com Ø ≥ 10 mm (cavilha ou tubo).
- Gancho e recipiente plástico de carga (garrafa de 5 L com alça), com funil e tubo de silicone.
- Bandeja com espuma (≥ 3 cm de espessura) sob o recipiente.
- Anteparo de policarbonato e óculos de proteção.
- Balança analítica de 0,1 mg (tex) e balança de 0–5 kg com resolução de 1 g (carga).
- Termo-higrômetro com registro.
- Câmera em tripé, régua de aço como escala no plano da fibra e boa iluminação difusa.
- Caneta de tinta permanente de ponta fina; bandeirolas de fita leve para o UHMWPE (a tinta adere mal).
- Software: Fiji/ImageJ ou Tracker (gratuitos); planilha ou Python para a análise.

Faixas de custo: S1, Seção 12.

## 6. Montagem

```
        ┌──────────── pórtico rígido ────────────┐
        │                                          │
        │   (O) garra superior (cabrestante, ≥3 voltas + grampo)
        │    |
        │    •  marca A ─┐
        │    |           │ L0 = 100,0 mm   ← régua de aço no mesmo plano
        │    •  marca B ─┘
        │    |
        │   (O) garra inferior (cabrestante) → gancho
        │    |
        │  [recipiente]  ← água adicionada por funil/tubo de fora do anteparo
        │  ≤ 3 cm
        │  ▓▓▓▓ bandeja com espuma ▓▓▓▓
        └──────────────────────────────────────────┘
   [anteparo de policarbonato]   [câmera em tripé, perpendicular ao plano]
```

1. **Cabrestante:** a fibra dá ≥ 3 voltas no cilindro antes de ser presa. O atrito distribui a carga e reduz as rupturas na garra.
2. **Comprimento livre** entre as garras de ~150 mm, com as marcas A e B a 100,0 mm uma da outra, no centro.
3. **Câmera** perpendicular ao plano, com resolução ≥ 10 px/mm no campo que inclui as duas marcas e a régua.
4. **Bandeja** posicionada de forma que, sob carga máxima e com o alongamento máximo esperado, o recipiente fique a ≤ 3 cm dela. Reajustar para cada material: a seda e o náilon alongam ~20–30 mm a mais que o UHMWPE.

## 7. Preparação

### 7.1 Condicionamento

- Manter as amostras ≥ 24 h no ambiente de ensaio. A atmosfera padrão têxtil de referência é a da ISO 139 (20 °C, 65 % UR; conferir a norma). Sem câmara climática, **registrar** T e UR no início e no fim de cada ensaio. No nível 1, usar uma caixa com solução saturada de NaCl (~75 % UR, ASTM E104).
- Distribuir os ensaios dos diferentes materiais **em ordem aleatória**, para não confundir uma deriva ambiental com efeito do material.

### 7.2 Densidade linear (tex)

1. Retirar 5 segmentos de pontos diferentes do carretel.
2. Cortar cada um com comprimento conhecido (1,000 m ± 1 mm, sem tensão, sobre escala). Se a massa de 1 m for < 10 mg, usar segmentos maiores (ex.: 5 m), para manter a incerteza relativa da pesagem ≲ 1–2 %.
3. Pesar (0,1 mg). **tex = massa (mg) ÷ comprimento (m).**
4. Registrar a média e o CV. O tex médio do lote é usado nos cálculos.

### 7.3 Corpos de prova

Cortar ~350 mm, manuseando pelas extremidades. Descartar trechos dobrados ou danificados.

## 8. Procedimento E1-a: carregamento incremental até a ruptura

1. Registrar o código do ensaio, material, lote, data e hora, T e UR.
2. Montar o corpo de prova (Seção 6). **Pré-carga** = gancho + recipiente vazio (~0,2–0,5 N), suficiente para retificar a fibra e ≤ ~2 % da carga de ruptura esperada.
3. Medir L0 entre as marcas sob pré-carga. Foto de referência (t = 0).
4. **Incrementos:** adicionar água em passos de ~5 % da carga de ruptura esperada (ex.: para 15 N, ~75 mL ≈ 0,74 N), em ~5 s cada. Acima de ~80 % da carga esperada, reduzir os passos para ~2,5 %.
5. **Patamar:** manter 30 s após cada incremento e fotografar ao final.
6. Repetir até a ruptura. Registrar se ela ocorreu durante a adição ou durante o patamar.
7. Após a ruptura, **pesar o recipiente com a água** (1 g). Carga de ruptura: F_rup = m_total · g, com m_total = gancho + recipiente + água.
8. Classificar o local da ruptura: **V** (válida, no comprimento útil), **G** (na garra ou a até 5 mm dela; inválida para a resistência, mas registrada) ou **S** (escorregamento). Classificar o modo: limpo, fibrilado, progressivo (filamentos rompendo em sequência) ou outro. Fotografar as extremidades.
9. Continuar até obter **n ≥ 10 ensaios válidos** por material. Registrar o total, incluindo os inválidos.

## 9. Procedimento E1-b: fluência

- **Materiais:** P1, P4 e P5 (prioritários); P3 se houver tempo.
- **Cargas:** 30 % e 50 % da carga média de ruptura obtida no E1-a. Aplicar em ~10 s, adicionando água de forma contínua e sem impacto.
- **Leituras (fotos):** 10 s, 1 min, 10 min e 1 h (opcional: 24 h).
- **n = 3** por material e carga.
- **Resultado:** ε(t), e fluência = ε(t) − ε(10 s). Se houver ruptura retardada, registrar o tempo até ela.
- Valem os mesmos limites de segurança, mais o L7.

## 10. Procedimento E1-c (opcional): úmido × condicionado

- **Materiais:** P1 e P3, que respondem à umidade.
- Imergir o corpo de prova em água destilada por 10 min, montar e ensaiar imediatamente (E1-a). Comparar com os resultados condicionados.
- Manter os equipamentos elétricos longe da água.
- **Interpretação:** a seda pode supercontrair. Medir também L0 após a imersão e antes da carga.

## 11. Análise de dados

| Grandeza | Cálculo | Unidade |
|---|---|---|
| Deformação | ε = (L − L0) / L0, com L medido entre as marcas na foto do fim de cada patamar | — |
| Carga | F = m_total · g | N |
| Resistência específica | τ = F_rup / T, com T em tex | N/tex (relatar em cN/tex) |
| Tensão equivalente | σ = τ · ρ, com ρ da ficha técnica ou da literatura, **declarada como hipótese** | GPa |
| Trabalho de ruptura | W = Σ ½ (F_i + F_{i+1}) · (ΔL_{i+1} − ΔL_i), regra do trapézio sobre os patamares | J |
| Trabalho de ruptura por massa | w = W / (T · L0), com T em kg/m (tex × 10⁻⁶) e L0 em m; dividir por 1000 para J/g | J/g |
| Tenacidade equivalente | w [J/g] × ρ [g/cm³] | MJ/m³ |

**Estatística:** média, desvio padrão, CV e IC 95 % (t de Student), com n de válidos e total. Comparar materiais por ANOVA de um fator ou Kruskal–Wallis, conforme a distribuição. Com n ≥ 10, ajustar uma distribuição de Weibull à F_rup é opcional nesta etapa.

**Fontes de incerteza (estimativas a confirmar no piloto):**

| Fonte | Ordem de grandeza | Observação |
|---|---|---|
| Pesagem de tex | 0,1 mg ÷ massa do segmento | ≲ 1–2 % se a massa for ≥ 10 mg |
| L0 | ±0,2 mm em 100 mm (±0,2 %) | Depende da nitidez das marcas |
| Deslocamento por vídeo | ±1 px (~±0,1 mm a 10 px/mm), ou ±0,1 % de deformação | Marginal para UHMWPE e aramida (ε_rup de 2–4 %); adequado para náilon e seda |
| Carga | ±1 g na pesagem, mais **até um incremento** de carga na ruptura | O incremento domina; por isso os passos menores perto da ruptura |
| Fluência durante os patamares | Sistemática | A deformação "estática" inclui 30 s de fluência; relatar o tempo de patamar |

## 12. Critérios de aceitação do método (propostos)

- CV de F_rup do P1 (náilon) **≤ 10 %**.
- Média de F_rup do P1 a ±15 % da carga declarada, **somente se** a ficha técnica informar condições comparáveis. Caso contrário, vale apenas o critério de CV.
- Rupturas na garra (G) **≤ 20 %** dos ensaios de cada material. Acima disso, revisar o diâmetro do cabrestante e o número de voltas.

Se os critérios não forem atendidos, revisar o método antes de ensaiar qualquer material novo.

## 13. Registro de dados

Usar [dados/modelo_registro_ensaio_S3.csv](../dados/modelo_registro_ensaio_S3.csv), com uma linha por foto ou patamar. Dicionário de campos:

| Campo | Conteúdo |
|---|---|
| `ensaio_id` | Identificador único (ex.: E1a-P1-001) |
| `subensaio` | E1a, E1b ou E1c |
| `data_hora` | ISO 8601 |
| `operador` | Iniciais |
| `material` | P1 a P5 |
| `lote` | Lote do fabricante |
| `temperatura_C`, `umidade_relativa_pct` | Leitura do termo-higrômetro |
| `tex_lote` | tex médio do lote (Seção 7.2) |
| `L0_mm` | Distância entre as marcas sob pré-carga |
| `patamar` | Índice do patamar (0 = pré-carga) |
| `tempo_s` | Tempo desde o início do ensaio |
| `massa_total_g` | Gancho + recipiente + água (a cada patamar, estimada pelo volume adicionado; na ruptura, pesada) |
| `L_mm` | Distância entre as marcas medida na foto |
| `evento` | patamar, ruptura ou leitura_fluencia |
| `local_ruptura` | V, G ou S (só na linha de ruptura) |
| `modo_ruptura` | limpo, fibrilado, progressivo ou outro |
| `foto` | Nome do arquivo |
| `observacoes` | Texto livre |

Os dados brutos (fotos e CSV) devem ser versionados no repositório, ou em armazenamento referenciado por ele, **antes** da análise.

## 14. Lista de verificação antes de cada sessão

- [ ] Óculos de proteção para todos os presentes
- [ ] Anteparo instalado; bandeja a ≤ 3 cm do recipiente na condição de carga máxima
- [ ] Material com carga declarada ≤ 50 N (ou piloto feito)
- [ ] Termo-higrômetro registrando
- [ ] Câmera, escala e iluminação verificadas (px/mm anotado)
- [ ] Ordem aleatória dos ensaios definida

## 15. O que **não** fazer

- Não suspender pessoas nem partes do corpo, nem simular esse uso.
- Não deixar cair massas nem fazer ensaios de impacto.
- Não ultrapassar 50 N nem trocar o recipiente por massas metálicas maiores.
- Não usar reagentes químicos neste experimento.
- Não improvisar dispositivos de lançamento ou pressurizados.
- Não extrapolar os resultados para capacidade de suporte humano (S1, Seção 8.3).

## 16. Produtos esperados

1. Tabela por material: tex, F_rup, τ, ε_rup, w, com média, DP, CV, IC 95 % e n válidos/total.
2. Curvas carga–deformação, uma por corpo de prova, com a média por material.
3. Curvas de fluência ε(t).
4. Fotografias e classificação dos modos de falha.
5. Matriz S2 atualizada com `tipo_dado = medido_proprio` e as condições registradas.
6. Decisão sobre S4 (S4-A ou S4-B) registrada no relatório S5 parcial.
