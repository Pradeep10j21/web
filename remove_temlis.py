import re

files = [
    '_services_ai-strategy/index.html',
    '_services_business-consulting/index.html',
    '_services_data-insights/index.html'
]

for file_path in files:
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the temlis component
    content = re.sub(r'<div class="new-base--t-card">.*?</div></div>', '', content, flags=re.DOTALL)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Done: {file_path}")
