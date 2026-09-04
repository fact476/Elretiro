import urllib.request, os, json

os.makedirs("imgs", exist_ok=True)
log = []

def test(url, nombre=None):
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        size = len(data)
        result = f"OK   {size:8d}b  {url[:80]}"
        print(result)
        log.append(result)
        if nombre and size > 10000:
            with open(f"imgs/{nombre}", "wb") as f:
                f.write(data)
            print(f"  -> Guardado como imgs/{nombre}")
        return data if size > 10000 else None
    except Exception as e:
        result = f"FAIL          {url[:80]} [{str(e)[:40]}]"
        print(result)
        log.append(result)
        return None

print("=== TEST DE FUENTES DE IMAGEN ===")

# Test servicios libres de imagen
test("https://picsum.photos/800/500", "test_picsum.jpg")
test("https://loremflickr.com/800/500/colombia", "test_flickr.jpg")
test("https://random.imagecdn.app/800/500", "test_random.jpg")
test("https://placekitten.com/800/500", "test_kitten.jpg")
test("https://placebear.com/800/500", "test_bear.jpg")
test("https://baconmockup.com/800/500/", "test_bacon.jpg")
test("https://via.placeholder.com/800x500", "test_placeholder.jpg")

# Test Wikimedia
test("https://upload.wikimedia.org/wikipedia/commons/6/61/Parque_del_Retiro-Antioquia.jpg", "parque_wiki.jpg")
test("https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Parque_del_Retiro-Antioquia.jpg/640px-Parque_del_Retiro-Antioquia.jpg", "parque_wiki_thumb.jpg")

# Test Pixabay (sin key, CDN directo)
test("https://cdn.pixabay.com/photo/2016/01/09/18/27/journey-1130732_640.jpg", "test_pixabay.jpg")

# Test otras fuentes
test("https://source.unsplash.com/800x500/?mountains,green", "test_unsplash.jpg")
test("https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80", "test_unsplash2.jpg")

print("\n=== ARCHIVOS GUARDADOS ===")
for f in os.listdir("imgs"):
    size = os.path.getsize(f"imgs/{f}")
    print(f"  {f}: {size:,} bytes")

with open("diagnostico.txt", "w") as f:
    f.write("\n".join(log))

print("\nDiagnostico guardado en diagnostico.txt")
