#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_strict_mode.py — Otto Radiologia Odontológica
------------------------------------------------------
Versão: 3.0 (Modo Estrito Literal)
Data: 03/11/2025

Função:
Valida todos os arquivos normativos do Otto, garantindo integridade e coerência
entre `diagnosticos.json`, `frases.json` e `regras_coerencia_exame.json`.

Pilares:
- Nenhuma inferência ou preenchimento automático.
- Respeito literal ao conteúdo dos arquivos anexados.
- Checagem clínica e estrutural completa.

Saída esperada:
Mensagens claras de conformidade e erros, prontos para uso em auditoria.
"""

import json
from pathlib import Path
from collections import Counter

# =====================================================
# 🧩 CONFIGURAÇÕES GERAIS
# =====================================================
ARQUIVOS = {
    "diagnosticos": Path("/mnt/data/diagnosticos.json"),
    "frases": Path("/mnt/data/frases.json"),
    "regras": Path("/mnt/data/regras_coerencia_exame.json")
}

FAIXA_ESPERADA = set(range(1, 109))  # Códigos 1–108
STRICT_MODE = True                   # Nenhuma inferência
EXIBIR_DETALHES = True               # Mostrar logs detalhados


# =====================================================
# 📖 FUNÇÕES AUXILIARES
# =====================================================
def ler_json_literal(path: Path):
    """Leitura literal (sem inferência)"""
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def log(msg: str, tipo="info"):
    """Formato de log padronizado"""
    prefixos = {
        "ok": "✅ ",
        "warn": "⚠️ ",
        "erro": "❌ ",
        "info": "🔍 "
    }
    print(f"{prefixos.get(tipo, '')}{msg}")


# =====================================================
# 🔬 VALIDAÇÃO DE DIAGNÓSTICOS
# =====================================================
def validar_diagnosticos(diagnosticos):
    log("Iniciando validação literal de diagnosticos.json...\n")

    codigos = [d.get("codigo") for d in diagnosticos if isinstance(d.get("codigo"), int)]
    nomes = [d.get("nome") for d in diagnosticos]
    total = len(codigos)
    log(f"Total de diagnósticos encontrados: {total}", "info")

    # Faixa esperada
    presentes = set(codigos)
    faltando = sorted(FAIXA_ESPERADA - presentes)
    extras = sorted(presentes - FAIXA_ESPERADA)

    if faltando:
        log(f"Códigos ausentes: {faltando}", "warn")
    if extras:
        log(f"Códigos fora da faixa 1–108: {extras}", "warn")
    if not faltando and not extras:
        log("Todos os códigos estão na faixa 1–108.", "ok")

    # Duplicados
    duplicados = [item for item, count in Counter(codigos).items() if count > 1]
    if duplicados:
        log(f"Códigos duplicados detectados: {duplicados}", "warn")
    else:
        log("Nenhum código duplicado.", "ok")

    # Campos obrigatórios
    faltantes = [d["codigo"] for d in diagnosticos if not d.get("nome") or not d.get("definicao")]
    if faltantes:
        log(f"Diagnósticos com campos ausentes (nome/definição): {faltantes}", "warn")
    else:
        log("Todos os diagnósticos possuem nome e definição.", "ok")

    # Marcados como inválidos
    for d in diagnosticos:
        nome = d.get("nome", "").lower()
        if "inválido" in nome or "duplicado" in nome:
            log(f"Código {d['codigo']} marcado como inválido ou duplicado: '{d['nome']}'", "warn")

    log("Validação de diagnosticos.json concluída.\n", "info")
    return set(codigos)


# =====================================================
# 🧠 VALIDAÇÃO DE FRASES
# =====================================================
def validar_frases(frases, codigos_validos):
    log("Iniciando validação de frases.json...\n")
    erros = []
    total_itens = len(frases.get("itens", []))
    log(f"Itens de frases encontrados: {total_itens}", "info")

    for item in frases.get("itens", []):
        for codigo in item.get("codigos", []):
            if codigo not in codigos_validos:
                erros.append(codigo)

    if erros:
        log(f"Códigos inexistentes em frases.json: {sorted(set(erros))}", "erro")
    else:
        log("Todos os códigos em frases.json são válidos e presentes em diagnosticos.json.", "ok")

    log("Validação de frases.json concluída.\n", "info")


# =====================================================
# 🩺 VALIDAÇÃO DE REGRAS DE COERÊNCIA
# =====================================================
def validar_regras(regras):
    log("Iniciando validação de regras_coerencia_exame.json...\n")

    exames_esperados = {"E1", "E2", "E3", "E4"}
    encontrados = set(regras.keys()) & exames_esperados
    faltando = exames_esperados - encontrados

    if faltando:
        log(f"Regras ausentes para exames: {faltando}", "warn")
    else:
        log("Todas as regras E1–E4 estão presentes.", "ok")

    for exame, dados in regras.items():
        if exame in exames_esperados:
            if "bloquear_termos" not in dados:
                log(f"Campo 'bloquear_termos' ausente em {exame}", "warn")
            else:
                if EXIBIR_DETALHES:
                    log(f"{exame}: bloqueia {len(dados['bloquear_termos'])} termos.", "info")

    log("Validação de regras_coerencia_exame.json concluída.\n", "info")


# =====================================================
# 🧾 EXECUÇÃO PRINCIPAL
# =====================================================
def main():
    print("\n========== 🧩 VALIDAÇÃO MODO ESTRITO LITERAL ==========\n")

    diagnosticos = ler_json_literal(ARQUIVOS["diagnosticos"])
    frases = ler_json_literal(ARQUIVOS["frases"])
    regras = ler_json_literal(ARQUIVOS["regras"])

    codigos_validos = validar_diagnosticos(diagnosticos)
    validar_frases(frases, codigos_validos)
    validar_regras(regras)

    print("🎯 Validação Estrita Literal finalizada com sucesso.\n")


if __name__ == "__main__":
    main()
