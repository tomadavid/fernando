from telegram.ext import Application, CommandHandler, MessageHandler, filters

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key="API_KEY",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

BOT_TOKEN = "TOKEN"

async def handle_message(update, context):
    prompt = update.message.text

    messages = [
        {
            "role": "system",
            "content": """És o Fernando Pessoa. Tens de dar respostas muito curtas, mas expondo a tua pessoa e génio criativo.
            Segue um papel de confidente que dá conselhos, baseando nas vivências e personalidade de pessoas.
            Evita usar muito os termos Heterónimo e Ortónimo pois isso são termos de quem analisa as obras de pessoa, e não dele próprio."""
        },
        {
            "role": "user",
            "content": f"""{prompt}"""
        },
    ]
    response = llm.invoke(messages)
    # Send a reply back to the user
    await update.message.reply_text(response.content)

async def start(update, context):
    await update.message.reply_text("Hello! I'm your bot.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
