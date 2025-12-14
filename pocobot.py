import discord
from discord.ext import commands
import os
import subprocess
import tempfile
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from io import BytesIO


# Carregar variáveis de ambiente
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


# Configurar intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


# Criar bot
bot = commands.Bot(command_prefix='!', intents=intents)


# ================== EXERCÍCIOS ==================
EXERCISES = {
    "m3_ex1": {
        "modulo": "Módulo 3",
        "titulo": "Até 25",
        "descricao": "Use um loop para exibir números até 25",
        "arquivo": "to25.py",
        "test": "print('Teste básico')",
        "order": 1,
        "dificuldade": "Básico"
    },
    "m3_ex2": {
        "modulo": "Módulo 3",
        "titulo": "Multiplication Table",
        "descricao": "Crie a tabuada de um número",
        "arquivo": "multiplication_table.py",
        "test": "print('Teste 2')",
        "order": 2,
        "dificuldade": "Básico"
    },
    # ... adicione mais 26 exercícios aqui
}


# Armazenar progresso dos usuários
USER_PROGRESS = {}


# ================== EVENTOS ==================


@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')
    print(f'📚 {len(EXERCISES)} exercícios carregados')
    print('🚀 Bot pronto para validar exercícios!')


# ================== FUNÇÕES ==================


def get_user_progress(user_id):
    if user_id not in USER_PROGRESS:
        USER_PROGRESS[user_id] = {"completed": []}
    return USER_PROGRESS[user_id]


def execute_test(code, test):
    """Executa código com segurança"""
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        result = subprocess.run(
            ['python', '-c', test],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(temp_file),
            timeout=5
        )
        
        os.unlink(temp_file)
        
        if result.returncode == 0:
            return True, "✅ Todos os testes passaram!"
        else:
            return False, f"❌ Erro: {result.stderr[:200]}"
    except subprocess.TimeoutExpired:
        return False, "⏱️ Timeout: Código levou muito tempo"
    except Exception as e:
        return False, f"❌ Erro: {str(e)[:100]}"


def generate_exercise_pdf(exercise_id, exercise_data):
    """Gera PDF do exercício"""
    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Título
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='#32b8c6',
        spaceAfter=20
    )
    
    elements.append(Paragraph(exercise_data['titulo'], title_style))
    elements.append(Spacer(1, 12))
    
    # Conteúdo
    elements.append(Paragraph(f"<b>Módulo:</b> {exercise_data['modulo']}", styles['Normal']))
    elements.append(Paragraph(f"<b>Nível:</b> {exercise_data['dificuldade']}", styles['Normal']))
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph(f"<b>Descrição:</b>", styles['Normal']))
    elements.append(Paragraph(exercise_data['descricao'], styles['Normal']))
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph(f"<b>Arquivo:</b> {exercise_data['arquivo']}", styles['Normal']))
    
    doc.build(elements)
    pdf_buffer.seek(0)
    return pdf_buffer


# ================== COMANDOS ==================


@bot.command(name='iniciar')
async def start_course(ctx):
    """Inicia o curso e cria canal privado"""
    user_id = ctx.author.id
    user_name = ctx.author.name
    progress = get_user_progress(user_id)
    
    try:
        # Criar categoria se não existir
        guild = ctx.guild
        category = None
        for cat in guild.categories:
            if cat.name == "📚 Cursos":
                category = cat
                break
        
        if not category:
            category = await guild.create_category("📚 Cursos")
        
        # Criar canal privado para o aluno
        channel_name = f"aluno-{user_name.lower().replace(' ', '-')}"
        
        # Verificar se canal já existe
        existing_channel = None
        for ch in guild.text_channels:
            if ch.name == channel_name:
                existing_channel = ch
                break
        
        if existing_channel:
            channel = existing_channel
            await ctx.send(f"✅ Você já tem um canal privado: {channel.mention}")
        else:
            # Criar nova permissão: só o aluno vê
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                ctx.author: discord.PermissionOverwrite(view_channel=True, send_messages=True),
                guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True)
            }
            
            channel = await guild.create_text_channel(
                channel_name,
                category=category,
                overwrites=overwrites
            )
            
            await ctx.send(f"✅ Seu canal privado foi criado: {channel.mention}")
            
            # Enviar mensagem de boas-vindas no canal privado
            embed = discord.Embed(
                title="🎓 Bem-vindo ao Curso de Python!",
                description="Este é seu canal privado para resolver exercícios",
                color=discord.Color.green()
            )
            embed.add_field(
                name="Comece agora!",
                value="Use `!enviar m3_ex1 arquivo.py` para submeter seu primeiro exercício\n\nAnexe o arquivo `.py` junto com o comando",
                inline=False
            )
            embed.add_field(
                name="Dicas:",
                value="- `!exercicios` - Lista todos os exercícios\n- `!progresso` - Seu progresso\n- `!comandos` - Todos os comandos",
                inline=False
            )
            
            await channel.send(embed=embed)
    
    except Exception as e:
        await ctx.send(f"❌ Erro ao criar canal: {str(e)}")


@bot.command(name='enviar')
async def submit_exercise(ctx):
    """Submete um exercício"""
    if not ctx.message.attachments:
        await ctx.send("❌ Anexe um arquivo .py!")
        return
    
    args = ctx.message.content.split()
    if len(args) < 2:
        await ctx.send("❌ Use: `!enviar m3_ex1`")
        return
    
    ex_id = args[1]
    
    if ex_id not in EXERCISES:
        await ctx.send(f"❌ Exercício '{ex_id}' não encontrado!")
        return
    
    exercise = EXERCISES[ex_id]
    user_id = ctx.author.id
    progress = get_user_progress(user_id)
    
    # Verificar se desbloqueado
    is_locked = exercise['order'] > 1 and not any(
        EXERCISES[e]['order'] == exercise['order'] - 1 
        for e in progress['completed']
    )
    
    if is_locked:
        await ctx.send(f"🔒 Complete o exercício anterior primeiro!")
        return
    
    # Download do arquivo
    attachment = ctx.message.attachments[0]
    code = await attachment.read()
    code = code.decode('utf-8')
    
    # Testar
    success, message = execute_test(code, exercise['test'])
    
    embed = discord.Embed(
        title=exercise['titulo'],
        color=discord.Color.green() if success else discord.Color.red()
    )
    embed.add_field(name="Resultado", value=message, inline=False)
    
    if success:
        if ex_id not in progress['completed']:
            progress['completed'].append(ex_id)
        
        embed.add_field(
            name="🎉 Parabéns!",
            value="Próximo exercício liberado!",
            inline=False
        )
        
        # Enviar próximo em DM
        try:
            dm = await ctx.author.create_dm()
            await dm.send(f"✅ Exercício {ex_id} completo! Próximo liberado.")
        except:
            pass
    
    await ctx.send(embed=embed)


@bot.command(name='progresso')
async def show_progress(ctx):
    """Mostra progresso do usuário"""
    user_id = ctx.author.id
    progress = get_user_progress(user_id)
    completed = len(progress['completed'])
    total = len(EXERCISES)
    percentage = int(completed / total * 100) if total > 0 else 0
    
    embed = discord.Embed(
        title="📊 Seu Progresso",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Exercícios Completos",
        value=f"{completed}/{total} ({percentage}%)",
        inline=False
    )
    
    if completed == total:
        embed.add_field(
            name="🏆 Parabéns!",
            value="Você completou o curso inteiro!",
            inline=False
        )
    
    await ctx.send(embed=embed)


@bot.command(name='comandos')
async def help_command(ctx):
    """Mostra comandos disponíveis"""
    embed = discord.Embed(
        title="📚 Comandos Disponíveis",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="!iniciar",
        value="Cria seu canal privado (use uma vez)",
        inline=False
    )
    embed.add_field(
        name="!enviar <ex_id> <arquivo.py>",
        value="Submete um exercício para validação",
        inline=False
    )
    embed.add_field(
        name="!progresso",
        value="Mostra seu progresso no curso",
        inline=False
    )
    embed.add_field(
        name="!exercicios",
        value="Lista todos os exercícios",
        inline=False
    )
    embed.add_field(
        name="!comandos",
        value="Mostra esta mensagem",
        inline=False
    )
    
    await ctx.send(embed=embed)


@bot.command(name='exercicios')
async def list_exercises(ctx):
    """Lista todos os exercícios"""
    embed = discord.Embed(
        title="📚 Todos os Exercícios",
        color=discord.Color.blue()
    )
    
    current_module = None
    for ex_id, data in sorted(EXERCISES.items(), key=lambda x: x[1]['order']):
        if current_module != data['modulo']:
            current_module = data['modulo']
            embed.add_field(name="", value=f"**{current_module}**", inline=False)
        
        embed.add_field(
            name=f"{data['order']}. {data['titulo']}",
            value=f"{data['descricao']}\n*Nível: {data['dificuldade']}*",
            inline=False
        )
    
    await ctx.send(embed=embed)


# ================== EXECUTAR ==================


if __name__ == '__main__':
    if not TOKEN:
        print("❌ ERRO: Token não encontrado em .env")
        print("Crie um arquivo .env com: DISCORD_TOKEN=seu_token_aqui")
    else:
        print("🚀 Iniciando bot...")
        bot.run(TOKEN)