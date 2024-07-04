


def render_items(list):
    rendered_list = '\n'.join(f'{item}' for item in list)
    print(f'Rendered {len(list)} items.')
    print(rendered_list)


list_a = ['how', 'are', 'you', 'today']

render_items(list_a)
