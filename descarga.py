import urllib.request, os

os.makedirs("imgs", exist_ok=True)

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"

# Fotos reales de Unsplash y Pixabay
# Cada foto fue seleccionada por su tema relevante para El Retiro
fotos = [
    # panoramica - paisaje montañas verdes Colombia/Antioquia
    ("panoramica.jpg", [
        "https://images.unsplash.com/photo-1589909202802-8f4aadce1849?w=900&q=85",  # montañas verdes Colombia
        "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=900&q=85",    # paisaje andino
        "https://cdn.pixabay.com/photo/2017/01/20/00/30/medellin-1993836_960_720.jpg",
    ]),
    # parque - plaza colonial Colombia
    ("parque.jpg", [
        "https://images.unsplash.com/photo-1585464231875-d9ef1f5ad396?w=900&q=85",  # plaza colonial Colombia
        "https://images.unsplash.com/photo-1518638150340-f706e86654de?w=900&q=85",  # iglesia colonial
        "https://cdn.pixabay.com/photo/2016/08/20/06/04/colombia-1605086_960_720.jpg",
    ]),
    # iglesia - iglesia colonial blanca
    ("iglesia.jpg", [
        "https://images.unsplash.com/photo-1518638150340-f706e86654de?w=900&q=85",
        "https://images.unsplash.com/photo-1548013146-72479768bada?w=900&q=85",
        "https://loremflickr.com/900/600/church,colonial,colombia",
    ]),
    # represa - lago embalse montañas
    ("represa.jpg", [
        "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=900&q=85",  # lago montañas
        "https://images.unsplash.com/photo-1501854140801-50d01698950b?w=900&q=85",  # vista aérea lago
        "https://cdn.pixabay.com/photo/2016/11/14/04/45/lake-1822660_960_720.jpg",
    ]),
    # salto - cascada tropical
    ("salto.jpg", [
        "https://images.unsplash.com/photo-1482192505345-5852cc2d7038?w=900&q=85",  # cascada selva
        "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=900&q=85",  # cascada tropical
        "https://cdn.pixabay.com/photo/2015/12/01/20/28/waterfall-1072605_960_720.jpg",
    ]),
    # bosque - reserva natural andina
    ("bosque.jpg", [
        "https://images.unsplash.com/photo-1448375240586-882707db888b?w=900&q=85",  # bosque verde
        "https://images.unsplash.com/photo-1497436072909-60f360e1d4b1?w=900&q=85",  # bosque niebla
        "https://cdn.pixabay.com/photo/2015/12/01/20/28/green-1072828_960_720.jpg",
    ]),
    # muebles - taller carpintería madera
    ("muebles.jpg", [
        "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=900&q=85",     # muebles sala
        "https://images.unsplash.com/photo-1506439773649-6e0eb8cfb237?w=900&q=85",  # carpintería madera
        "https://cdn.pixabay.com/photo/2017/08/02/00/49/people-2568954_960_720.jpg",
    ]),
    # aguacate - cultivo aguacate hass
    ("aguacate.jpg", [
        "https://images.unsplash.com/photo-1601039641847-7857b994d704?w=900&q=85",  # aguacates árbol
        "https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?w=900&q=85",  # aguacates cosecha
        "https://cdn.pixabay.com/photo/2016/03/05/19/02/abstract-1238247_960_720.jpg",
    ]),
    # fiestas - festival nocturno Colombia
    ("fiestas.jpg", [
        "https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=900&q=85",  # festival luces
        "https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=900&q=85",  # concierto noche
        "https://loremflickr.com/900/600/festival,colombia,night",
    ]),
    # javiera - museo colonial estatua
    ("javiera.jpg", [
        "https://images.unsplash.com/photo-1564399580075-79b879e4f7a2?w=900&q=85",  # museo colonial
        "https://images.unsplash.com/photo-1554907984-15263bfd63bd?w=900&q=85",    # estatua bronce
        "https://loremflickr.com/900/600/museum,statue,colombia",
    ]),
    # banda - banda musical municipio
    ("banda.jpg", [
        "https://images.unsplash.com/photo-1465847899084-d164df4dedc6?w=900&q=85",  # banda musical
        "https://images.unsplash.com/photo-1524368535928-5b5e00ddc76b?w=900&q=85",  # orquesta parque
        "https://loremflickr.com/900/600/brass,band,music,colombia",
    ]),
    # escudo - heráldica
    ("escudo_bg.jpg", [
        "https://images.unsplash.com/photo-1588392382834-a891154bca4d?w=600&q=85",
        "https://loremflickr.com/600/600/colombia,antioquia",
    ]),
]

ok = 0
for nombre, urls in fotos:
    print(f"Descargando {nombre}...")
    descargado = False
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=25) as r:
                data = r.read()
            if len(data) > 15000:
                with open(f"imgs/{nombre}", "wb") as f:
                    f.write(data)
                print(f"  OK: {nombre} ({len(data):,} bytes)")
                ok += 1
                descargado = True
                break
            else:
                print(f"  Muy pequeña ({len(data)}b), intentando otra...")
        except Exception as e:
            print(f"  Error: {str(e)[:60]}")
    if not descargado:
        print(f"  FALLO: {nombre}")

print(f"\n=== {ok}/{len(fotos)} fotos descargadas ===")
import subprocess
subprocess.run(["ls", "-lh", "imgs/"])
