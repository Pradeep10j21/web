import re
import os

# List of HTML files to process
html_files = [
    r'c:\Users\hp\Desktop\webs\_\index.html',
    r'c:\Users\hp\Desktop\webs\_services\index.html',
    r'c:\Users\hp\Desktop\webs\_about-us_about-us\index.html',
    r'c:\Users\hp\Desktop\webs\_contact-us_contact-us-3\index.html',
    r'c:\Users\hp\Desktop\webs\_services_ai-strategy\index.html',
    r'c:\Users\hp\Desktop\webs\_services_business-consulting\index.html',
    r'c:\Users\hp\Desktop\webs\_services_data-insights\index.html',
]

# Pattern to match the dropdown section
# This matches from the opening div with nav_dropdown class to the closing </div></div></nav>
pattern = r'<div[^>]*class="[^"]*nav_dropdown[^"]*"[^>]*>.*?</div>\s*</div>\s*</nav>'

for file_path in html_files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if "More Links" exists in the file
        if 'More Links' not in content:
            print(f"Skipping {file_path} - no 'More Links' found")
            continue
        
        # Remove the dropdown section
        original_length = len(content)
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        if len(content) != original_length:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Successfully removed dropdown from {file_path}")
        else:
            print(f"No changes made to {file_path}")
    else:
        print(f"File not found: {file_path}")

print("Done!")
