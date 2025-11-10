# Casos de Teste — Gerador de Frases 

> Dica: use `ci/validate.py` para checar os JSONs antes; e depois rode os prompts no GPT publicado.

## 1\) Interproximais sem termos radiculares (E3)

**Entrada (JSON, conforme schema `entrada_comandos`):**

```json
{
  "E": [3],
  "sequencia": [
    { "tipo": "F", "codigos": [2], "dentes": ["15", "25"] },
    { "tipo": "F", "codigos": [3], "dentes": ["14"] }
  ]
}
```

**Saída Esperada:**
Laudo de Radiografia(s) Interproximais.

Análise Diagnóstica:

  - Comando F [2] / 15 25: Cárie incipiente nos dentes 15 e 25.
  - Comando F [3] / 14: Desmineralização de esmalte no dente 14.

**Nota de Correção** (se houver):
Não aplicável. O exame E3 é compatível com os diagnósticos e os termos radiculares foram omitidos, mantendo a coerência.

**Sugestão e Recomendação**

```
- Na região interproximal do dente 15, identifica-se discreta radiolucidez restrita ao esmalte, sem comprometimento dentinário aparente. Achados compatíveis com cárie incipiente. Sugere-se avaliação clínica com transiluminação e controle preventivo; considerar selamento/infiltração conforme critério clínico.
- Na região interproximal do dente 25, identifica-se discreta radiolucidez restrita ao esmalte, sem comprometimento dentinário aparente. Achados compatíveis com cárie incipiente. Sugere-se avaliação clínica com transiluminação e controle preventivo; considerar selamento/infiltração conforme critério clínico.
- No dente 14, evidencia-se radiolucidez sutil em esmalte, de interpretação duvidosa (possível sombra/superposição). Achados sugestivos de desmineralização de esmalte.Recomenda-se avaliação clínica criteriosa e, se necessário, controle radiográfico interproximal seriado.
- Observa-se, de forma generalizada, cristas ósseas alveolares com morfologia compatível com a normalidade. A critério clínico, sugere-se avaliação periodontal complementar.
- Recomenda-se análise da adaptação marginal das restaurações presentes, com atenção especial às áreas interproximais.
- As lesões cariosas limitadas ao esmalte podem não ser evidentes na radiografia, até que aproximadamente 30% a 40% de desmineralização tenha ocorrido. Recomenda-se exame clínico detalhado de todas as superfícies oclusais e proximais para avaliação completa.
- Vários fenômenos morfológicos como sulcos e fissuras profundas, sobreposição de imagem (especialmente em proximais), efeito de burnout cervical, efeito de Mach band, e anomalias dentárias como depressões hipoplásicas ou concavidades por desgaste, podem ser confundidos com lesões cariosas ou mascarar outras alterações. A avaliação clínica cuidadosa das superfícies dentárias é fundamental.
- O exame radiográfico é complementar à avaliação clínica, sendo o Cirurgião-Dentista (CD) o profissional apto a emitir o diagnóstico definitivo e o plano de tratamento.
- Sugere-se acompanhamento clínico-radiográfico periódico dos achados descritos e registrados no odontograma.
- Em caso de dúvidas adicionais, recomenda-se contato com a clínica de radiologia responsável.
```

## 2\) Periapicais com achados mistos (E2)

**Entrada (JSON, conforme schema `entrada_comandos`):**

```json
{
  "E": [2],
  "sequencia": [
    { "tipo": "F", "codigos": [8, 23], "dentes": ["48"] },
    { "tipo": "F", "codigos": [7], "dentes": ["46", "47"] }
  ]
}
```

**Saída Esperada:**
Laudo de Radiografia(s) Periapicais.

Análise Diagnóstica:

  - Comando F [8, 23] / 48: Dente ausente e Alvéolo vazio (extração recente?) no dente 48.
  - Comando F [7] / 46 47: Restauração ou coroa metálica/plástica com aspecto de normalidade nos dentes 46 e 47.

**Nota de Correção** (se houver):
Não aplicável.

**Sugestão e Recomendação**

```
- Na região do dente 48, não se observa elemento dentário presente. Contudo, identifica-se alvéolo vazio com lâmina dura evidente. Achados compatíveis com dente ausente e sugestivos de alvéolo vazio, provavelmente em processo de cicatrização pós-extração recente. Recomenda-se proservação para cicatrização óssea e avaliação clínica para planejamento reabilitador, se indicado.
- No dente 46, observa-se material restaurador radiopaco com contornos regulares e adaptação aparente em sua coroa. Achados compatíveis com restauração ou coroa com aspecto de normalidade. Sugere-se proservação clínica periódica.
- No dente 47, observa-se material restaurador radiopaco com contornos regulares e adaptação aparente em sua coroa. Achados compatíveis com restauração ou coroa com aspecto de normalidade. Sugere-se proservação clínica periódica.
- Observa-se, de forma generalizada, cristas ósseas alveolares com morfologia compatível com a normalidade. A critério clínico, sugere-se avaliação periodontal complementar.
- Recomenda-se análise da adaptação marginal das restaurações presentes, com atenção especial às áreas interproximais.
- As lesões cariosas limitadas ao esmalte podem não ser evidentes na radiografia, até que aproximadamente 30% a 40% de desmineralização tenha ocorrido. Recomenda-se exame clínico detalhado de todas as superfícies oclusais e proximais para avaliação completa.
- Vários fenômenos morfológicos como sulcos e fissuras profundas, sobreposição de imagem (especialmente em proximais), efeito de burnout cervical, efeito de Mach band, e anomalias dentárias como depressões hipoplásicas ou concavidades por desgaste, podem ser confundidos com lesões cariosas ou mascarar outras alterações. A avaliação clínica cuidadosa das superfícies dentárias é fundamental.
- O exame radiográfico é complementar à avaliação clínica, sendo o Cirurgião-Dentista (CD) o profissional apto a emitir o diagnóstico definitivo e o plano de tratamento.
- Sugere-se acompanhamento clínico-radiográfico periódico dos achados descritos e registrados no odontograma.
- Em caso de dúvidas adicionais, recomenda-se contato com a clínica de radiologia responsável.
```

## 3\) Panorâmica com múltiplos dentes (E1)

**Entrada (JSON, conforme schema `entrada_comandos`):**

```json
{
  "E": [1],
  "sequencia": [
    { "tipo": "F", "codigos": [24, 22], "dentes": ["33", "34", "35", "43", "44", "45"] }
  ]
}
```

**Saída Esperada:**
Laudo de Radiografia(s) Panorâmica.

Análise Diagnóstica:

  - Comando F [24, 22] / 33 34 35 43 44 45: Presença de aparelho ortodôntico fixo envolvendo os dentes 33, 34, 35, 43, 44 e 45, associado a arredondamento apical das raízes desses elementos.

**Nota de Correção** (se houver):
Não aplicável.

**Sugestão e Recomendação**

```
- Observa-se aparelho ortodôntico fixo abrangendo os dentes 33, 34, 35, 43, 44 e 45, com arredondamento apical discreto das raízes, achado compatível com remodelação fisiológica induzida por movimentação ortodôntica. Não há evidências de reabsorções patológicas associadas. Recomenda-se acompanhamento clínico-radiográfico durante o tratamento ortodôntico.
- Observa-se, de forma generalizada, cristas ósseas alveolares com morfologia compatível com a normalidade. A critério clínico, sugere-se avaliação periodontal complementar.
- Recomenda-se análise da adaptação marginal das restaurações presentes, com atenção especial às áreas interproximais.
- As lesões cariosas limitadas ao esmalte podem não ser evidentes na radiografia, até que aproximadamente 30% a 40% de desmineralização tenha ocorrido. Recomenda-se exame clínico detalhado de todas as superfícies oclusais e proximais para avaliação completa.
- Vários fenômenos morfológicos como sulcos e fissuras profundas, sobreposição de imagem (especialmente em proximais), efeito de burnout cervical, efeito de Mach band, e anomalias dentárias como depressões hipoplásicas ou concavidades por desgaste, podem ser confundidos com lesões cariosas ou mascarar outras alterações. A avaliação clínica cuidadosa das superfícies dentárias é fundamental.
- O exame radiográfico é complementar à avaliação clínica, sendo o Cirurgião-Dentista (CD) o profissional apto a emitir o diagnóstico definitivo e o plano de tratamento.
- Sugere-se acompanhamento clínico-radiográfico periódico dos achados descritos e registrados no odontograma.
- Em caso de dúvidas adicionais, recomenda-se contato com a clínica de radiologia responsável.
```

## 4\) Periapicais com Endodontia (E2)

**Entrada (JSON, conforme schema `entrada_comandos`):**

```json
{
  "E": [2],
  "sequencia": [
    { "tipo": "F", "codigos": [9, 12], "dentes": ["11"] },
    { "tipo": "F", "codigos": [10, 12], "dentes": ["36"] }
  ]
}
```

**Saída Esperada:**
Laudo de Radiografia(s) Periapicais.

Análise Diagnóstica:

  - Comando F [9, 12] / 11: Conduto obturado adequadamente e rarefação óssea periapical difusa no dente 11.
  - Comando F [10, 12] / 36: Conduto parcialmente obturado associado a rarefação óssea periapical difusa no dente 36.

**Nota de Correção** (se houver):
Não aplicável.

**Sugestão e Recomendação**

```
- No dente 11, observa-se conduto obturado até 1–2 mm do ápice radicular, com material condensado lateralmente e rarefação óssea periapical difusa de limites imprecisos. Achados compatíveis com processo inflamatório crônico residual de origem endodôntica. Recomenda-se acompanhamento clínico-radiográfico periódico e controle endodôntico.
- No dente 36, identifica-se conduto parcialmente obturado, com material obturador distante do ápice e rarefação óssea periapical difusa sem limites definidos. Achados compatíveis com abscesso periapical associado a tratamento endodôntico incompleto. Recomenda-se reavaliação endodôntica e eventual retratamento, conforme correlação clínica.
- Observa-se, de forma generalizada, cristas ósseas alveolares com morfologia compatível com a normalidade. A critério clínico, sugere-se avaliação periodontal complementar.
- Recomenda-se análise da adaptação marginal das restaurações presentes, com atenção especial às áreas interproximais.
- As lesões cariosas limitadas ao esmalte podem não ser evidentes na radiografia, até que aproximadamente 30% a 40% de desmineralização tenha ocorrido. Recomenda-se exame clínico detalhado de todas as superfícies oclusais e proximais para avaliação completa.
- Vários fenômenos morfológicos como sulcos e fissuras profundas, sobreposição de imagem (especialmente em proximais), efeito de burnout cervical, efeito de Mach band, e anomalias dentárias como depressões hipoplásicas ou concavidades por desgaste, podem ser confundidos com lesões cariosas ou mascarar outras alterações. A avaliação clínica cuidadosa das superfícies dentárias é fundamental.
- O exame radiográfico é complementar à avaliação clínica, sendo o Cirurgião-Dentista (CD) o profissional apto a emitir o diagnóstico definitivo e o plano de tratamento.
- Sugere-se acompanhamento clínico-radiográfico periódico dos achados descritos e registrados no odontograma.
- Em caso de dúvidas adicionais, recomenda-se contato com a clínica de radiologia responsável.
```

## 5\) Interproximais com dente impactado (E3)

**Entrada (JSON, conforme schema `entrada_comandos`):**

```json
{
  "E": [3],
  "sequencia": [
    { "tipo": "F", "codigos": [53], "dentes": ["48"] }
  ]
}
```

**Saída Esperada:**
Laudo de Radiografia(s) Interproximais.

Análise Diagnóstica:

  - Comando F [53, 43] / 48: Dente 48 retido/impactado, posicionado aquém do plano oclusal, apresentando infra-oclusão relativa.

**Nota de Correção** (se houver):
A radiografia Interproximal (E3) possui limitação para a completa visualização de dentes impactados no terço radicular/apical. O laudo é restrito aos aspectos coronários e cervicais visíveis. Achados compatíveis com inclusão e infra-oclusão do terceiro molar inferior direito (48), sem sinais de alterações ósseas associadas. Sugere-se complementação panorâmica ou tomográfica para definição de conduta cirúrgica.

**Sugestão e Recomendação**

```
- Na região do dente 48, observa-se imagem parcial com apenas a porção coronária do elemento, com ausência de irrupção na cavidade oral. Achados compatíveis com dente impactado em infra-oclusão. Recomenda-se exame panorâmico ou tomografia de feixe cônico (TCFC) para avaliação tridimensional da posição, relação com o canal mandibular e estruturas adjacentes.
- Observa-se, de forma generalizada, cristas ósseas alveolares com morfologia compatível com a normalidade. A critério clínico, sugere-se avaliação periodontal complementar.
- Recomenda-se análise da adaptação marginal das restaurações presentes, com atenção especial às áreas interproximais.
- As lesões cariosas limitadas ao esmalte podem não ser evidentes na radiografia, até que aproximadamente 30% a 40% de desmineralização tenha ocorrido. Recomenda-se exame clínico detalhado de todas as superfícies oclusais e proximais para avaliação completa.
- Vários fenômenos morfológicos como sulcos e fissuras profundas, sobreposição de imagem (especialmente em proximais), efeito de burnout cervical, efeito de Mach band, e anomalias dentárias como depressões hipoplásicas ou concavidades por desgaste, podem ser confundidos com lesões cariosas ou mascarar outras alterações. A avaliação clínica cuidadosa das superfícies dentárias é fundamental.
- O exame radiográfico é complementar à avaliação clínica, sendo o Cirurgião-Dentista (CD) o profissional apto a emitir o diagnóstico definitivo e o plano de tratamento.
- Sugere-se acompanhamento clínico-radiográfico periódico dos achados descritos e registrados no odontograma.
- Em caso de dúvidas adicionais, recomenda-se contato com a clínica de radiologia responsável.
```

## 6\) Erro de Código (Ausente)

**Entrada (JSON, conforme schema `entrada_comandos`):**

```json
{
  "E": [2],
  "sequencia": [
    { "tipo": "F", "codigos": [999], "dentes": ["11"] }
  ]
}
```

**Saída Esperada:**
Código 999 não encontrado. Verifique o manual de diagnósticos.

## 7\) E2 Exame periapical com nota adicional geral

**Entrada com Nota:**

```json
{
  "E": [2],
  "sequencia": [
    { "tipo": "F", "codigos": [83, 67], "dentes": ["36"], "notas": ["perda severa"] }
  ]
}
```

**Saída Esperada:**
Laudo de Radiografia(s) Periapicais.

Análise Diagnóstica:

  - Comando F [83, 67] / 36 [perda severa]: Lesão de furca com perda severa ee Perda óssea alveolar vertical severa no dente 36.

**Nota de Correção** (se houver):
Não aplicável.

**Sugestão e Recomendação**

```
- No dente 36, observa-se perda óssea alveolar vertical avançada, estendendo-se além do terço médio radicular e atingindo a região de furca com perda óssea severa. Achados compatíveis com defeito ósseo angular e lesão de furca avançados. Recomenda-se avaliação periodontal especializada e planejamento cirúrgico/protético.
- A avaliação radicular para detalhes finos é plenamente suportada neste exame.
- Recomenda-se análise da adaptação marginal das restaurações presentes, com atenção especial às áreas interproximais.
- As lesões cariosas limitadas ao esmalte podem não ser evidentes na radiografia, até que aproximadamente 30% a 40% de desmineralização tenha ocorrido. Recomenda-se exame clínico detalhado de todas as superfícies oclusais e proximais para avaliação completa.
- Vários fenômenos morfológicos como sulcos e fissuras profundas, sobreposição de imagem (especialmente em proximais), efeito de burnout cervical, efeito de Mach band, e anomalias dentárias como depressões hipoplásicas ou concavidades por desgaste, podem ser confundidos com lesões cariosas ou mascarar outras alterações. A avaliação clínica cuidadosa das superfícies dentárias é fundamental.
- O exame radiográfico é complementar à avaliação clínica, sendo o Cirurgião-Dentista (CD) o profissional apto a emitir o diagnóstico definitivo e o plano de tratamento.
- Sugere-se acompanhamento clínico-radiográfico periódico dos achados descritos e registrados no odontograma.
- Em caso de dúvidas adicionais, recomenda-se contato com a clínica de radiologia responsável.
```

## 8\) E1 Exame panorâmico com Frase 
**Entrada FRASE:**

```json
{
  "E": [1],
  "sequencia": [
    { "tipo": "FRASE", "texto": "PACIENTE COMPLETAMENTE EDÊNTULO" }
  ]
}
```

**Saída Esperada:**
Laudo de Radiografia(s) Panorâmica.

Análise Diagnóstica:

  - Comando FRASE PACIENTE COMPLETAMENTE EDÊNTULO.

**Nota de Correção** (se houver):
Não aplicável.

**Sugestão e Recomendação**

```
- Na arcada maxilar e mandibular, observa-se ausência total de elementos dentários. Achados compatíveis com edentulismo total. Recomenda-se avaliação protética detalhada para planejamento de reabilitação oral.
- O exame radiográfico é complementar à avaliação clínica, sendo o Cirurgião-Dentista (CD) o profissional apto a emitir o diagnóstico definitivo e o plano de tratamento. 
- Em caso de dúvidas adicionais, recomenda-se contato com a clínica de radiologia responsável. 
```

## 9\) E2 Exame Periapical com Nota específica para um diagnóstico (E2)
**Entrada (JSON):**
```json
{
  "E": [2],
  "sequencia": [
    { 
      "tipo": "F",
      "codigos": [9, 10, 79, 7],
      "dentes": ["26"],
      "notas": [
        "9 [[raiz mesial e raiz distal]]",
        "10 [[raiz palatina]]",
        "79 [[raiz palatina]]"
      ]
    }
  ]
}
```

**Análise Diagnóstica:**
  - Comando F [9 [[raiz mesial e raiz distal]], 10 [[raiz palatina]], 79 [[raiz palatina]], 7] / 26: Condutos obturados nas raízes mesial e distal; conduto parcialmente obturado e núcleo intrarradicular na raiz palatina; restauração coronária normal.

**Nota de Correção:**  
Não aplicável.

**Sugestão e Recomendação:**
```
- No dente 26, observam-se diferentes condições radiculares, nas raízes mesial e distal, material obturador radicular bem condensado lateralmente, atingindo cerca de 1–2 mm do ápice, compatível com condutos obturados adequadamente; na raiz palatina, o material obturador apresenta condensação irregular e aquém do ápice radicular, com presença de núcleo intrarradicular. A coroa associada exibe material restaurador radiopaco de contornos regulares e adaptação marginal aparente. Achados compatíveis com tratamento endodôntico satisfatório nas raízes mesial e distal e obturação incompleta e núcleo intraradicular de fixação na raiz palatina, em elemento restaurado com aspecto de normalidade. Recomenda-se proservação endodôntica periódica das raízes mesial e distal e avaliação especializada da raiz palatina.
- Observa-se, de forma generalizada, cristas ósseas alveolares com morfologia compatível com a normalidade. A critério clínico, sugere-se avaliação periodontal complementar.
- Recomenda-se análise da adaptação marginal das restaurações presentes, com atenção especial às áreas interproximais.
- As lesões cariosas limitadas ao esmalte podem não ser evidentes na radiografia, até que aproximadamente 30% a 40% de desmineralização tenha ocorrido. Recomenda-se exame clínico detalhado de todas as superfícies oclusais e proximais para avaliação completa.
- Vários fenômenos morfológicos como sulcos e fissuras profundas, sobreposição de imagem (especialmente em proximais), efeito de burnout cervical, efeito de Mach band, e anomalias dentárias como depressões hipoplásicas ou concavidades por desgaste, podem ser confundidos com lesões cariosas ou mascarar outras alterações. A avaliação clínica cuidadosa das superfícies dentárias é fundamental.
- O exame radiográfico é complementar à avaliação clínica, sendo o Cirurgião-Dentista (CD) o profissional apto a emitir o diagnóstico definitivo e o plano de tratamento.
- Sugere-se acompanhamento clínico-radiográfico periódico dos achados descritos e registrados no odontograma.
- Em caso de dúvidas adicionais, recomenda-se contato com a clínica de radiologia responsável.
```

---

## 10\)  Nota específica para um dente (E2)

**Entrada (JSON):**
```json
{
  "E": [2],
  "sequencia": [
    {
      "tipo": "F",
      "codigos": [7],
      "dentes": ["21", "22"],
      "notas": [
        "21 [[incisal]]",
        "22 [[face mesial]]"
      ]
    }
  ]
}
```

**Análise Diagnóstica:**
  - Comando F [7] / 21 [[incisal]] 22 [[face mesial]]: Materiais restauradores radiopacos bem adaptados localizados na face incisal do 21 e na face mesial do 22.

**Nota de Correção:**  
Não aplicável.

**Sugestão e Recomendação:**
```
- Nos dentes 21 e 22, observam-se materiais restauradores radiopacos, sendo que no 21, a restauração localiza-se na face incisal, com contornos regulares e adaptação marginal aparente, e no 22, o material restaurador estende-se à face mesial, igualmente bem delimitado e contínuo com a estrutura dentária. Achados compatíveis com restaurações em aspecto de normalidade. Sugere-se proservação clínica periódica e eventual ajuste estético-funcional.
```