import json
import re
from pathlib import Path

MD_FILE = "100_exercicios_python.md"
OUTPUT_JSON = "exercises.json"


def detect_validation(instructions):
    joined = " ".join(instructions).lower()

    validation = {}

    # ================= INPUT =================
    if "digite" in joined or "input" in joined:
        validation["type"] = "ast"
        validation["must_use"] = ["input"]

    # ================= PRINT / OUTPUT =================
    if "exiba" in joined or "mostre" in joined or "imprima" in joined:
        if validation.get("type") == "ast":
            validation.setdefault("must_use", []).append("print")
        else:
            validation["type"] = "ast"
            validation["must_use"] = ["print"]

    # ================= FUNÇÕES =================
    if "função" in joined or "defina uma função" in joined:
        validation["type"] = "ast"
        validation["must_use"] = ["def"]

    # ================= CLASSES =================
    if "classe" in joined:
        validation["type"] = "ast"
        validation["must_use"] = ["class"]

    # ================= LOOPS =================
    if "for " in joined:
        validation["type"] = "ast"
        validation["must_use"] = validation.get("must_use", []) + ["for"]

    if "while" in joined:
        validation["type"] = "ast"
        validation["must_use"] = validation.get("must_use", []) + ["while"]

    if "não use while" in joined:
        validation["forbidden"] = ["while"]

    # ================= CONDICIONAIS =================
    if "se " in joined or "if " in joined:
        validation["type"] = "ast"
        validation["must_use"] = validation.get("must_use", []) + ["if"]

    # ================= SAÍDA ESPERADA =================
    expected_output = []
    for line in instructions:
        if line.startswith("?>"):
            continue
        if line.strip().startswith("Olá") or line.strip().startswith("Resultado"):
            expected_output.append(line.strip())

    if expected_output:
        validation = {
            "type": "output",
            "expected": expected_output
        }

    # ================= FALLBACK =================
    if not validation:
        validation = {
            "type": "static"
        }

    return validation


def parse_md(md_text):
    exercises = {}

    # Divide por blocos de exercício
    blocks = re.split(r"\n##+\s*Exercício", md_text)

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        lines = [l.strip() for l in block.splitlines() if l.strip()]

        # Número do exercício
        match = re.search(r"(\d+)", lines[0])
        if not match:
            continue

        number = int(match.group(1))
        ex_id = f"ex{number:02d}"

        titulo = lines[0].replace("—", "-").strip()

        instrucoes = []
        arquivo = f"{ex_id}.py"

        for line in lines[1:]:
            instrucoes.append(line)

            if line.lower().startswith("arquivos para entregar"):
                parts = line.split(":")
                if len(parts) > 1 and parts[1].strip().lower() != "none":
                    arquivo = parts[1].strip()

        exercises[ex_id] = {
            "order": number,
            "modulo": "Módulo 0 - Primeiros Passos",
            "titulo": titulo,
            "descricao": "",
            "instrucoes": instrucoes,
            "arquivo": arquivo,
            "dificuldade": "Básico",
            "validation": detect_validation(instrucoes)
        }

    return exercises


def main():
    md_path = Path(MD_FILE)

    if not md_path.exists():
        print(f"❌ Arquivo {MD_FILE} não encontrado")
        return

    md_text = md_path.read_text(encoding="utf-8")
    exercises = parse_md(md_text)

    # Ordena por order
    exercises = dict(sorted(exercises.items(), key=lambda x: x[1]["order"]))

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(exercises, f, indent=2, ensure_ascii=False)

    print(f"✅ {len(exercises)} exercícios gerados em {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
