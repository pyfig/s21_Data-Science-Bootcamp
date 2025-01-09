num_of_steps = 5

report_template = """Report

We have made {total} observations from tossing a coin: {tails} of them were tails and {heads} of
them were heads. The probabilities are {tail_fraction:.2f}% and {head_fraction:.2f}%, respectively. Our
forecast is that in the next {steps} observations we will have: {predictions}.
"""

log_file = "analytics.log"

# get token bot for Bot = @BotFather
token_bot = "Токен бота"
# get chat_id for Bot = @get_id_bot
token_chat_id = "ID чата"

telegram_webhook_url = f"https://api.telegram.org/bot{token_bot}/sendMessage"


