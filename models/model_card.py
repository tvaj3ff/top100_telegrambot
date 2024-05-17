def get_card(data: dict) -> str:
    card = (f'{data['rank']}. <b>{data['title']}</b>\n'
            f'ОПИСАНИЕ:'
            f'\n{data['description']}\n'
            f'\nГод:{data['year']}\t\U00002B50{data['rating']}\n'
            f'{data['big_image']}')
    return card
