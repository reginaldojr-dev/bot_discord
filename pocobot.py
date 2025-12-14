import discord
from discord.ext import commands
import os
import json
import subprocess
import tempfile
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from io import BytesIO

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
        print(f"📚 {len(data)} exercícios carregados do JSON")
        return data
    except Exception as e:
        print(f"❌ Erro ao carregar exercícios: {e}")
        return {}

EXERCISES = load_exercises()

# ================== PROGRESSO ==================

USER_PROGRESS = {}

def get_user_progress(user_id):
    if user_id not in USER_PROGRESS:
        USER_PROGRESS[user_id] = {"completed": []}
    return USER_PROGRESS[user_id]

# ================== UTIL ==================

def get_next_exercise(progress):
    if not progress["completed"]:
        return min(EXERCISES.items(), key=lambda x: x[1]["order"])

    last_completed = max(
        progress["completed"],
        key=lambda e: EXERCISES[e]["order"]
    )

    next_order = EXERCISES[last_completed]["order"] + 1

    for ex_id, ex in EXERCISES.items():
        if ex["order"] == next_order:
            return ex_id, ex

    return None, None

async def send_exercise(channel, ex_id, exercise):
    embed = discord.Embed(
        title=f"📘 Exercício {exercise['order']}",
        color=discord.Color.blurple()
    )

    embed.add_field(
        name=exercise["titulo"],
        value=exercise["descricao"],
        inline=False
    )

    embed.add_field(
        name="📄 Arquivo esperado",
        value=f"`{exercise['arquivo']}`",
        inline=False
    )

    embed.add_field(
        name="📤 Como enviar",
        value=f"Use `!enviar {ex_id}` e anexe o arquivo `.py`",
        inline=False
    )

    await channel.send(embed=embed)

# ================== EVENTOS ==================

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")
    print("🚀 Bot pronto para validar exercícios!")

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
        await ctx.send(f"✅ Você já tem um canal: {channel.mention}")
        return

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
        guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True)
    }

    channel = await guild.create_text_channel(
        channel_name,
        category=category,
        overwrites=overwrites
    )

    embed = discord.Embed(
        title="🎓 Bem-vindo ao Curso de Python!",
        description="Este é seu canal privado para exercícios.",
        color=discord.Color.green()
    )

    embed.add_field(
        name="📘 Fluxo do curso",
        value="Resolva os exercícios em ordem. O próximo será liberado automaticamente.",
        inline=False
    )

    await channel.send(embed=embed)
    await ctx.send(f"✅ Canal criado: {channel.mention}")

    # 👉 ENVIA PRIMEIRO EXERCÍCIO
    progress = get_user_progress(user.id)
    ex_id, exercise = get_next_exercise(progress)
    if ex_id:
        await send_exercise(channel, ex_id, exercise)

@bot.command(name="enviar")
async def submit_exercise(ctx):
    if not ctx.message.attachments:
        await ctx.send("❌ Anexe um arquivo `.py`")
        return

    args = ctx.message.content.split()
    if len(args) < 2:
        await ctx.send("❌ Use: `!enviar ex01`")
        return

    ex_id = args[1]

    if ex_id not in EXERCISES:
        await ctx.send("❌ Exercício não encontrado")
        return

    exercise = EXERCISES[ex_id]
    progress = get_user_progress(ctx.author.id)

    is_locked = exercise["order"] > 1 and not any(
        EXERCISES[e]["order"] == exercise["order"] - 1
        for e in progress["completed"]
    )

    if is_locked:
        await ctx.send("🔒 Complete o exercício anterior primeiro")
        return

    attachment = ctx.message.attachments[0]
    code = (await attachment.read()).decode("utf-8")

    success, result = execute_test(code, exercise["test"])

    embed = discord.Embed(
        title=exercise["titulo"],
        color=discord.Color.green() if success else discord.Color.red()
    )
    embed.add_field(name="Resultado", value=result, inline=False)

    if success and ex_id not in progress["completed"]:
        progress["completed"].append(ex_id)
        embed.add_field(name="🎉 Parabéns!", value="Exercício concluído!", inline=False)
        await ctx.send(embed=embed)

        # 👉 ENVIA PRÓXIMO EXERCÍCIO
        next_ex_id, next_ex = get_next_exercise(progress)
        if next_ex_id:
            await send_exercise(ctx.channel, next_ex_id, next_ex)
        else:
            await ctx.send("🏆 Parabéns! Você concluiu todos os exercícios!")
        return

    await ctx.send(embed=embed)

@bot.command(name="progresso")
async def show_progress(ctx):
    progress = get_user_progress(ctx.author.id)
    total = len(EXERCISES)
    completed = len(progress["completed"])
    percent = int((completed / total) * 100) if total else 0

    embed = discord.Embed(title="📊 Seu Progresso", color=discord.Color.blue())
    embed.add_field(
        name="Concluídos",
        value=f"{completed}/{total} ({percent}%)",
        inline=False
    )

    await ctx.send(embed=embed)

@bot.command(name="exercicios")
async def list_exercises(ctx):
    embed = discord.Embed(title="📚 Exercícios", color=discord.Color.blue())

    current_module = None
    for _, ex in sorted(EXERCISES.items(), key=lambda x: x[1]["order"]):
        if current_module != ex["modulo"]:
            current_module = ex["modulo"]
            embed.add_field(name="⠀", value=f"**{current_module}**", inline=False)

        embed.add_field(
            name=f"{ex['order']}. {ex['titulo']}",
            value=f"{ex['descricao']}\n*Nível: {ex['dificuldade']}*",
            inline=False
        )

    await ctx.send(embed=embed)

# ================== START ==================

if __name__ == "__main__":
    if not TOKEN:
        print("❌ Token não encontrado no .env")
    else:
        print("🚀 Iniciando bot...")
        bot.run(TOKEN)
