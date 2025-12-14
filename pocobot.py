import discord
from discord.ext import commands
import os
import json
import subprocess
import tempfile
import sys
import ast
from dotenv import load_dotenv

# ================== ENV ==================

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# ================== INTENTS ==================

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ================== EXERCÍCIOS ==================


def load_exercises():
    try:
        with open("exercises.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"📚 {len(data)} exercícios carregados")
        return data
    except Exception as e:
        print(f"❌ Erro ao carregar exercises.json: {e}")
        return {}


EXERCISES = load_exercises()

# ================== PROGRESSO ==================

PROGRESS_FILE = "progress.json"


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_progress():
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(USER_PROGRESS, f, indent=2, ensure_ascii=False)


USER_PROGRESS = load_progress()


def get_user_progress(user_id):
    uid = str(user_id)
    if uid not in USER_PROGRESS:
        USER_PROGRESS[uid] = {"completed": []}
        save_progress()
    return USER_PROGRESS[uid]


# ================== UTIL ==================


def get_next_exercise(progress):
    if not progress["completed"]:
        return min(EXERCISES.items(), key=lambda x: x[1]["order"])

    last_completed = max(progress["completed"], key=lambda e: EXERCISES[e]["order"])
    next_order = EXERCISES[last_completed]["order"] + 1

    for ex_id, ex in EXERCISES.items():
        if ex["order"] == next_order:
            return ex_id, ex

    return None, None


def format_instructions(instructions):
    if not instructions:
        return "—"

    header, steps, footer = [], [], []

    for line in instructions:
        line = line.strip()

        if line.lower().startswith("exercício"):
            header.append(f"• **{line}**")
        elif ":" in line and not line.startswith("-"):
            key, value = line.split(":", 1)
            header.append(f"• **{key.strip()}:** `{value.strip()}`")
        elif line.startswith("-"):
            steps.append(line.replace("-", "").strip())
        elif line == "---":
            continue
        else:
            footer.append(line)

    text = ""
    if header:
        text += "\n".join(header) + "\n\n"

    if steps:
        text += "**Passos:**\n"
        for i, step in enumerate(steps, 1):
            text += f"{i}. {step}\n"
        text += "\n"

    if footer:
        text += "> " + " ".join(footer)

    return text.strip()


async def send_exercise(channel, ex_id, exercise):
    embed = discord.Embed(
        title=f"📘 Exercício {exercise['order']} — {exercise['titulo']}",
        color=discord.Color.blurple(),
    )

    embed.add_field(
        name="📝 Descrição",
        value=exercise.get("descricao", "—"),
        inline=False,
    )

    instructions_text = format_instructions(exercise.get("instrucoes"))

    if len(instructions_text) > 1000:
        parts = [
            instructions_text[i : i + 1000]
            for i in range(0, len(instructions_text), 1000)
        ]
        for i, part in enumerate(parts, 1):
            embed.add_field(
                name=f"📋 Instruções ({i})",
                value=part,
                inline=False,
            )
    else:
        embed.add_field(
            name="📋 Instruções",
            value=instructions_text,
            inline=False,
        )

    embed.add_field(
        name="📄 Arquivo esperado",
        value=f"`{exercise['arquivo']}`",
        inline=False,
    )

    embed.add_field(
        name="📤 Envio",
        value=f"Use `!enviar {ex_id}` e anexe o arquivo `.py`",
        inline=False,
    )

    await channel.send(embed=embed)


# ================== VALIDAÇÃO ==================

class CodeValidator(ast.NodeVisitor):
    def __init__(self, rules):
        self.rules = rules

        self.used_names = set()
        self.imports = set()
        self.functions = {}
        self.classes = set()
        self.has_if = False
        self.has_loop = False
        self.errors = []

    # --------- VISITORS ---------

    def visit_Name(self, node):
        self.used_names.add(node.id)
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.add(alias.name.split(".")[0])
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module:
            self.imports.add(node.module.split(".")[0])
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.functions[node.name] = {
            "args": len(node.args.args),
            "has_return": any(isinstance(n, ast.Return) for n in ast.walk(node))
        }
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.classes.add(node.name)
        self.generic_visit(node)

    def visit_If(self, node):
        self.has_if = True
        self.generic_visit(node)

    def visit_For(self, node):
        self.has_loop = True
        self.generic_visit(node)

    def visit_While(self, node):
        self.has_loop = True
        self.generic_visit(node)

    # --------- FINAL VALIDATION ---------

    def validate(self):
        rules = self.rules

        #  Proibidos
        for item in rules.get("forbidden", []):
            if item in self.used_names or item in self.imports:
                self.errors.append(f"Uso proibido detectado: `{item}`")

        #  Obrigatórios
        for item in rules.get("must_use", []):
            if item not in self.used_names:
                self.errors.append(f"Você deve usar `{item}`")

        #  Funções obrigatórias
        for fn in rules.get("functions_required", []):
            name = fn["name"]

            if name not in self.functions:
                self.errors.append(f"Função `{name}` não encontrada")
                continue

            if "args" in fn:
                if self.functions[name]["args"] != fn["args"]:
                    self.errors.append(
                        f"Função `{name}` deve ter {fn['args']} parâmetros"
                    )

            if fn.get("must_return") and not self.functions[name]["has_return"]:
                self.errors.append(f"Função `{name}` deve retornar um valor")

        #  Classes obrigatórias
        for cls in rules.get("class_required", []):
            if cls not in self.classes:
                self.errors.append(f"Classe `{cls}` não encontrada")

        # 🔁 Estrutura
        if rules.get("require_if") and not self.has_if:
            self.errors.append("Você deve usar pelo menos um `if`")

        if rules.get("require_loop") and not self.has_loop:
            self.errors.append("Você deve usar um laço (`for` ou `while`)")

        return self.errors


def validate_ast(code: str, rules: dict):
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return False, f"❌ Erro de sintaxe: {e}"

    must_use = rules.get("must_use", [])

    found = set()

    class Visitor(ast.NodeVisitor):
        def visit_Call(self, node):
            if isinstance(node.func, ast.Name):
                found.add(node.func.id)
            self.generic_visit(node)

    Visitor().visit(tree)

    for required in must_use:
        if required not in found:
            return False, f"❌ O código deve usar `{required}()`"

    return True, "✅ Estrutura do código validada!"


def validate_code(code: str, exercise: dict):
    validation = exercise.get("validation", {})
    vtype = validation.get("type", "none")

    # 🔒 AST VALIDATION
    if vtype == "ast":
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            return False, f"❌ Erro de sintaxe: {e}"

        validator = CodeValidator(validation)
        validator.visit(tree)
        errors = validator.validate()

        if errors:
            return False, "❌ Problemas encontrados:\n" + "\n".join(
                f"• {e}" for e in errors
            )

        return True, "✅ Estrutura do código está correta!"

    # 🔹 Cria arquivo temporário
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as temp:
        temp.write(code)
        temp_path = temp.name

    try:
        result = subprocess.run(
            [sys.executable, temp_path],
            capture_output=True,
            text=True,
            timeout=5,
        )
    except subprocess.TimeoutExpired:
        return False, "⏱️ O código demorou muito para executar."
    finally:
        os.unlink(temp_path)

    if result.returncode != 0:
        return False, f"❌ Erro ao executar:\n```\n{result.stderr[:1500]}\n```"

    output = result.stdout.strip()

    # 🔹 Output validation
    if vtype == "output":
        expected = validation.get("expected", [])
        for item in expected:
            if item not in output:
                return False, f"❌ Saída esperada não encontrada: `{item}`"
        return True, "✅ Saída correta!"

    # 🔹 Apenas execução
    if vtype == "static":
        return True, "✅ Código executou sem erros!"

    return True, "✅ Exercício recebido!"


# ================== EVENTOS ==================


@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")
    print("🚀 Bot pronto para o curso!")


# ================== COMANDOS ==================


@bot.command(name="iniciar")
async def start_course(ctx):
    user = ctx.author
    guild = ctx.guild

    category = discord.utils.get(guild.categories, name="📚 Cursos")
    if not category:
        category = await guild.create_category("📚 Cursos")

    channel_name = f"aluno-{user.name.lower().replace(' ', '-')}"
    channel = discord.utils.get(guild.text_channels, name=channel_name)

    if channel:
        await ctx.send(f"✅ Você já possui um canal: {channel.mention}")
        return

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
        guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True),
    }

    channel = await guild.create_text_channel(
        channel_name,
        category=category,
        overwrites=overwrites,
    )

    await channel.send(
        embed=discord.Embed(
            title="🎓 Curso de Python — Bem-vindo!",
            description="Resolva os exercícios em ordem.",
            color=discord.Color.green(),
        )
    )

    await ctx.send(f"✅ Canal criado: {channel.mention}")

    progress = get_user_progress(user.id)
    ex_id, exercise = get_next_exercise(progress)
    if ex_id:
        await send_exercise(channel, ex_id, exercise)


@bot.command(name="enviar")
async def submit_exercise(ctx):
    if not ctx.message.attachments:
        await ctx.send("❌ Anexe um arquivo `.py`")
        return

    ex_id = ctx.message.content.split()[1]

    if ex_id not in EXERCISES:
        await ctx.send("❌ Exercício não encontrado")
        return

    exercise = EXERCISES[ex_id]
    progress = get_user_progress(ctx.author.id)

    if exercise["order"] > 1:
        prev = exercise["order"] - 1
        if not any(EXERCISES[e]["order"] == prev for e in progress["completed"]):
            await ctx.send("🔒 Complete o exercício anterior primeiro")
            return

    attachment = ctx.message.attachments[0]
    code = (await attachment.read()).decode("utf-8")

    success, feedback = validate_code(code, exercise)

    if not success:
        await ctx.send(feedback)
        return

    progress["completed"].append(ex_id)
    save_progress()

    await ctx.send(feedback)

    next_ex_id, next_ex = get_next_exercise(progress)
    if next_ex_id:
        await send_exercise(ctx.channel, next_ex)
    else:
        await ctx.send("🏆 Parabéns! Você concluiu todo o curso!")


# ================== START ==================

if __name__ == "__main__":
    if not TOKEN:
        print("❌ Token não encontrado no .env")
    else:
        print("🚀 Iniciando bot...")
        bot.run(TOKEN)
