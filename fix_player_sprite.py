import pyxel

# --- 色の定義 ---
BLACK = 0
DARK_BROWN = 6
# 元のファイルでは背景がマゼンタ(13)で、目などが黒(0)と想定
ORIGINAL_BACKGROUND = 13
ORIGINAL_FEATURES = 0

# --- Pyxelの初期化 ---
pyxel.init(256, 256, display_scale=0)

# --- アセットファイルのロード ---
try:
    pyxel.load("assets.pyxres")
except Exception as e:
    print(f"Error loading assets.pyxres: {e}")
    exit()

# --- Image 0 を編集対象にする ---
img = pyxel.image(0)

# --- (0,0)の通常クマのピクセルを修正 ---
# 16x16の範囲をループ
for y in range(16):
    for x in range(16):
        px_color = img.pget(x, y)
        # 背景色だったら黒(透明色)に置き換える
        if px_color == ORIGINAL_BACKGROUND:
            img.pset(x, y, BLACK)
        # 黒(目や口)だったら濃い茶色に置き換える
        elif px_color == ORIGINAL_FEATURES:
            img.pset(x, y, DARK_BROWN)

# --- 変更を保存 ---
pyxel.save("assets.pyxres")

print("assets.pyxresを更新しました: 通常のクマの背景を黒(透明色)に、目と口を濃い茶色に変更しました。")
