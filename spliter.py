# splitter.py

# Baca file input berisi daftar domain
with open('list.txt', 'r') as infile:
    lines = infile.readlines()

# Proses setiap baris dan ubah formatnya
converted = []
for line in lines:
    parts = line.strip().split(':')
    if len(parts) == 3:
        domain, user, password = parts
        new_format = f"{domain}|{user}|{password}"
        converted.append(new_format)

# Simpan hasil ke file output
with open('output.txt', 'w') as outfile:
    outfile.write('\n'.join(converted))

print("✅ Konversi selesai! Hasil disimpan di output.txt")
