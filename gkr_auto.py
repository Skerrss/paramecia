
import requests
from tabulate import tabulate
import time

# Ganti dengan API key kamu dari https://serpapi.com
SERPAPI_KEY = "MASUKKAN_KEY_KITA"

# Estimasi volume dari Google Suggest (masih pake metode nakal)
def estimate_volume_google(keyword):
    try:
        url = f"https://www.google.com/complete/search?client=firefox&q={keyword}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        suggestions = data[1]
        score = len(suggestions) * 10 + sum(len(s) for s in suggestions) // 10
        return score if score > 0 else 10
    except:
        return 10

# Ambil jumlah allintitle dari SerpAPI
def get_allintitle_serpapi(keyword):
    try:
        params = {
            "q": f'allintitle:"{keyword}"',
            "api_key": SERPAPI_KEY,
            "engine": "google"
        }
        response = requests.get("https://serpapi.com/search", params=params, timeout=15)
        data = response.json()
        result_count = data.get("search_information", {}).get("total_results", 0)
        return result_count
    except Exception as e:
        print(f"⚠️ Gagal ambil allintitle dari SerpAPI: {e}")
        return 0

def categorize_gkr(gkr):
    if gkr <= 0.25:
        return "🔥 Wajib Digas!"
    elif gkr <= 0.75:
        return "🟢 Layak Perjuangan"
    elif gkr <= 1.0:
        return "⚠️ Medium Kompetisi"
    else:
        return "🚫 Berat Bos!"

def main():
    print("\n💻 GKR Checker x SerpAPI Edition 🧠\n")
    try:
        n = int(input("Masukkan jumlah keyword: "))
    except ValueError:
        print("Input tidak valid.")
        return

    result = []
    for i in range(n):
        print(f"\n➡️ Keyword #{i+1}")
        kw = input("Masukkan keyword: ").strip()
        print("⏳ Ambil estimasi volume & allintitle (SerpAPI)...")
        volume = estimate_volume_google(kw)
        allintitle = get_allintitle_serpapi(kw)
        print(f"📊 Volume Estimasi: {volume} | Allintitle: {allintitle}")
        gkr = allintitle / volume if volume else 999
        kategori = categorize_gkr(gkr)
        result.append([kw, volume, allintitle, f"{gkr:.2f}", kategori])
        time.sleep(1)

    print("\n📈 Hasil GKR Checker:")
    print(tabulate(result, headers=["Keyword", "Estimasi Volume", "Allintitle", "GKR", "Kategori"], tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()
