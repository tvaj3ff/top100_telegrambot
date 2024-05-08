def get_card(data: dict) -> str:
    card = (f'{data['rank']}. <b>{data['title']}</b>\n'
            f'\n{data['description']}\n'
            f'\n{data['year']}    \U00002B50{data['rating']}\n'
            f'{data['big_image']}')
    return card
