with open('index.html', 'r') as f:
    content = f.read()

old = "function setFolder(f,el){currentFolder=f;document.querySelectorAll('.folder-tab').forEach(t=>t.classList.remove('active'));el.classList.add('active');renderList();}"
new = "function setFolder(f,el){currentFolder=f;document.querySelectorAll('.folder-tab').forEach(t=>t.classList.remove('active'));el.classList.add('active');load();renderList();}"

content = content.replace(old, new)

with open('index.html', 'w') as f:
    f.write(content)

print("Done")
