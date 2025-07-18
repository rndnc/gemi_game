import pyxel

# 色の定義
BLACK = 0
DARK_BROWN = 6
WHITE = 7

# Pyxelを初期化 (描画はしないので display_scale=0)
# ヘッドレスモードで実行するために必要
pyxel.init(16, 16, display_scale=0)

# アセットファイルをロード
try:
    pyxel.load("assets.pyxres")
except Exception as e:
    print(f"Error loading assets.pyxres: {e}")
    print("Please ensure 'assets.pyxres' is in the same directory.")
    exit()

# クマの画像（Image 0）を取得
img = pyxel.image(0)

# スプライトの位置とサイズ
SPRITE_X, SPRITE_Y = 0, 0
SPRITE_W, SPRITE_H = 16, 16

# --- 1. 元のピクセルデータを読み込む ---
original_data = []
for y in range(SPRITE_H):
    row = []
    for x in range(SPRITE_W):
        row.append(img.pget(SPRITE_X + x, SPRITE_Y + y))
    original_data.append(row)

# --- 2. 新しいピクセルデータを作成（まず黒で初期化） ---
new_data = [[BLACK for _ in range(SPRITE_W)] for _ in range(SPRITE_H)]

# --- 3. 縁取りを白で描画 ---
for y in range(SPRITE_H):
    for x in range(SPRITE_W):
        # 元のピクセルが背景色(黒)でなければ処理
        if original_data[y][x] != BLACK:
            is_edge = False
            # 上下左右の隣接ピクセルを確認
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny, nx = y + dy, x + dx
                # 画像の範囲外か、隣が背景色なら、そこは縁
                if not (0 <= ny < SPRITE_H and 0 <= nx < SPRITE_W) or original_data[ny][nx] == BLACK:
                    is_edge = True
                    break
            if is_edge:
                new_data[y][x] = WHITE

# --- 4. 縁取りの内側を元の色で塗りつぶす ---
for y in range(SPRITE_H):
    for x in range(SPRITE_W):
        # 元のピクセルが背景色でなく、まだ新しいデータで色が塗られていない(縁ではない)場合
        if original_data[y][x] != BLACK and new_data[y][x] == BLACK:
            new_data[y][x] = original_data[y][x]

# --- 5. 目、口、鼻を濃い茶色で上書き描画 ---
# 座標は一般的なスプライトを想定したものです
# 目
new_data[5][4] = DARK_BROWN
new_data[5][10] = DARK_BROWN
# 鼻
new_data[8][7] = DARK_BROWN
new_data[8][8] = DARK_BROWN
# 口 (U字型)
new_data[10][6] = DARK_BROWN
new_data[11][7] = DARK_BROWN
new_data[11][8] = DARK_BROWN
new_data[10][9] = DARK_BROWN

# --- 6. 新しいピクセルデータを画像に書き戻す ---
for y in range(SPRITE_H):
    for x in range(SPRITE_W):
        img.pset(SPRITE_X + x, SPRITE_Y + y, new_data[y][x])

# --- 7. 変更を保存 ---
pyxel.save("assets.pyxres")

print("Successfully modified 'assets.pyxres'.")