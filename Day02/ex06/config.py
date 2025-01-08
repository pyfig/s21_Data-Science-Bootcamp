num_of_steps = 5

report_template = """Report

We have made {total} observations from tossing a coin: {tails} of them were tails and {heads} of
them were heads. The probabilities are {tail_fraction:.2f}% and {head_fraction:.2f}%, respectively. Our
forecast is that in the next {steps} observations we will have: {predictions}.
"""

log_file = "analytics.log"


token_bot = "CЮДА ТОКЕН"
token_chat_id = "CЮДА ЧАТ ID"

telegram_webhook_url = f"https://api.telegram.org/bot{token_bot}/sendMessage"
telegram_chat_id = token_chat_id

# get token bot for Bot = @BotFather
# get chat_id for Bot = @get_id_bot
