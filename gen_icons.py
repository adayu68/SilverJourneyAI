"""生成 tabBar 白色图标（橙底白图）"""
import struct, zlib, os

def make_png(w, h, rgba_rows):
    def pack_chunk(tag, data):
        c = zlib.crc32(tag + data) & 0xffffffff
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', c)
    raw = b''
    for row in rgba_rows:
        raw += b'\x00' + bytes([v for px in row for v in px])
    compressed = zlib.compress(raw, 9)
    ihdr = struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0)
    return b'\x89PNG\r\n\x1a\n' + pack_chunk(b'IHDR', ihdr) + pack_chunk(b'IDAT', compressed) + pack_chunk(b'IEND', b'')

def fill(w, h, r, g, b, a=255):
    return [[(r,g,b,a)]*w for _ in range(h)]

def draw_rect(rows, x1, y1, x2, y2, r, g, b, a=255):
    for y in range(y1, min(y2, len(rows))):
        for x in range(x1, min(x2, len(rows[0]))):
            rows[y][x] = (r,g,b,a)

def draw_circle(rows, cx, cy, radius, r, g, b, a=255):
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            if (x-cx)**2 + (y-cy)**2 <= radius**2:
                rows[y][x] = (r,g,b,a)

W, H = 81, 81
OW, OW2 = 255, 255  # white
TR = (0,0,0,0)       # transparent

out = r"c:\Users\vivia\WorkBuddy\20260326012226\SilverJourneyAI\miniprogram\images"
os.makedirs(out, exist_ok=True)

# ── 普通态（白色半透明）和选中态（纯白）各一套 ──────────────────

def make_icon_home(alpha):
    rows = fill(W, H, 0, 0, 0, 0)
    # 屋顶三角
    for y in range(10, 38):
        w2 = int((y - 10) * 1.5)
        x1 = W//2 - w2; x2 = W//2 + w2
        for x in range(max(0,x1), min(W,x2)):
            rows[y][x] = (OW,OW,OW,alpha)
    # 房身
    draw_rect(rows, 18, 37, 63, 65, OW, OW, OW, alpha)
    # 门
    draw_rect(rows, 33, 50, 48, 65, OW, OW, OW, alpha)
    # 门洞（透明）
    draw_rect(rows, 35, 52, 46, 65, 0, 0, 0, 0)
    return rows

def make_icon_recommend(alpha):
    rows = fill(W, H, 0, 0, 0, 0)
    # 地图轮廓
    draw_rect(rows, 12, 18, 69, 62, OW, OW, OW, alpha)
    draw_rect(rows, 15, 21, 66, 59, 0, 0, 0, 0)
    # 图钉
    draw_circle(rows, W//2, 32, 9, OW, OW, OW, alpha)
    draw_circle(rows, W//2, 32, 5, 0, 0, 0, 0)
    for y in range(41, 55):
        rows[y][W//2] = (OW,OW,OW,alpha)
        if W//2+1 < W: rows[y][W//2+1] = (OW,OW,OW,alpha)
    return rows

def make_icon_itinerary(alpha):
    rows = fill(W, H, 0, 0, 0, 0)
    # 日历框
    draw_rect(rows, 14, 16, 67, 68, OW, OW, OW, alpha)
    draw_rect(rows, 17, 19, 64, 65, 0, 0, 0, 0)
    # 顶部横条（白）
    draw_rect(rows, 14, 16, 67, 30, OW, OW, OW, alpha)
    # 三行横线（白色线条模拟日历网格）
    for row_y in [36, 46, 56]:
        draw_rect(rows, 20, row_y, 61, row_y+3, OW, OW, OW, alpha)
    return rows

def make_icon_safety(alpha):
    rows = fill(W, H, 0, 0, 0, 0)
    # 盾牌外形
    for y in range(12, 65):
        frac = min(1.0, (y - 12) / 53.0)
        if frac < 0.5:
            hw = int(28 * frac / 0.5)
        else:
            hw = int(28 * (1 - frac) / 0.5)
        hw = max(hw, 6)
        x1 = W//2 - hw; x2 = W//2 + hw
        for x in range(x1, x2+1):
            if 0 <= x < W:
                rows[y][x] = (OW,OW,OW,alpha)
    # 心形（挖空）
    draw_circle(rows, W//2-7, 36, 7, 0, 0, 0, 0)
    draw_circle(rows, W//2+7, 36, 7, 0, 0, 0, 0)
    for y in range(36, 52):
        hw = int((52-y)*0.6)
        for x in range(W//2-hw, W//2+hw+1):
            if 0 <= x < W and 0 <= y < H:
                rows[y][x] = (0,0,0,0)
    return rows

icons = [
    ("home.png",          make_icon_home(160)),
    ("home_sel.png",      make_icon_home(255)),
    ("recommend.png",     make_icon_recommend(160)),
    ("recommend_sel.png", make_icon_recommend(255)),
    ("itinerary.png",     make_icon_itinerary(160)),
    ("itinerary_sel.png", make_icon_itinerary(255)),
    ("safety.png",        make_icon_safety(160)),
    ("safety_sel.png",    make_icon_safety(255)),
]

for fname, rows in icons:
    rgba_rows = [[(px[0],px[1],px[2]) for px in row] for row in rows]
    # 转为RGB only （PNG IHDR type=2）
    raw = b''
    import zlib, struct
    for row in rows:
        raw += b'\x00' + bytes([c for px in row for c in (px[0],px[1],px[2],px[3])])
    def pack_chunk(tag, data):
        c = zlib.crc32(tag + data) & 0xffffffff
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', c)
    ihdr = struct.pack('>IIBBBBB', W, H, 8, 6, 0, 0, 0)  # type=6 RGBA
    compressed = zlib.compress(raw, 9)
    png = b'\x89PNG\r\n\x1a\n' + pack_chunk(b'IHDR', ihdr) + pack_chunk(b'IDAT', compressed) + pack_chunk(b'IEND', b'')
    path = os.path.join(out, fname)
    with open(path, 'wb') as f:
        f.write(png)
    print(f"  生成: {fname} ({len(png)} bytes)")

print("全部图标生成完成!")
