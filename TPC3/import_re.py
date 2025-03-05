import re

def markdown_to_html(markdown_text):
    lines = markdown_text.split('\n')
    html_lines = []
    
    list_items = []
    in_list = False
    
    for line in lines:
        if not line.strip():
            if in_list:
                html_list = "<ol>\n"
                for item in list_items:
                    html_list += f"<li>{item}</li>\n"
                html_list += "</ol>"
                html_lines.append(html_list)
                list_items = []
                in_list = False
            html_lines.append("")
            continue
        
        header_match = re.match(r'^(#{1,3})\s+(.+)$', line)
        if header_match:
            level = len(header_match.group(1))
            text = header_match.group(2)
            html_lines.append(f"<h{level}>{text}</h{level}>")
            continue
        
        list_match = re.match(r'^\s*(\d+)\.\s+(.+)$', line)
        if list_match:
            if not in_list:
                in_list = True
            item_text = list_match.group(2)
            
            item_text = process_inline_formatting(item_text)
            list_items.append(item_text)
            continue
        
        if in_list:
            html_list = "<ol>\n"
            for item in list_items:
                html_list += f"<li>{item}</li>\n"
            html_list += "</ol>"
            html_lines.append(html_list)
            list_items = []
            in_list = False
        
        processed_line = process_inline_formatting(line)
        html_lines.append(processed_line)
    
    if in_list:
        html_list = "<ol>\n"
        for item in list_items:
            html_list += f"<li>{item}</li>\n"
        html_list += "</ol>"
        html_lines.append(html_list)
    
    return '\n'.join(html_lines)

def process_inline_formatting(text):
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', text)
    return text

if __name__ == "__main__":
    example = """# Exemplo
    
Este é um **exemplo** ...

*Este é um exemplo* ...

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt)

![Imagem de uma paisagem](https://images.pexels.com/photos/414171/pexels-photo-414171.jpeg) ..."""
    
    html_output = markdown_to_html(example)
    print(html_output)

