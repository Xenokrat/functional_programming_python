# 3.1
@curry(2)
def tag(tag_name: str, tag_val: str) -> str:
    return f"<{tag_name}>{tag_val}</{tag_name}>"

bold = tag('b')
italic = tag('i')

# 3.2
@curry(3)
def tag(tag_name: str, attr: dict[str, str], tag_val: str) -> str:
    attrs_str = ' '.join([f"{k}=\"{val}\"" for k, val in attr.items()])
    return f"<{tag_name} {attrs_str}>{tag_val}</{tag_name}>"

print(tag('li', {'class': 'list-group', 'id': '1'}, 'item 23'))  # <li class="list-group" id="1">item 23</li>