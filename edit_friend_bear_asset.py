import pyxel

# --- 色の定義 ---
GOLD = 10
WHITE = 7
ORIGINAL_BODY = 4
ORIGINAL_SNOUT = 5

# --- Pyxelの初期化 ---
pyxel.init(256, 256, display_scale=0) # Image Bankのサイズで初期化

# --- アセットファイルのロード ---
try:
    pyxel.load("assets.pyxres")
except Exception as e:
    print(f"Error loading assets.pyxres: {e}")
    exit()

# --- Image 0 を編集対象にする ---
img = pyxel.image(0)

# --- (0,0)の元のクマを(16,0)にコピー ---
# blt(コピー先のx, コピー先のy, コピー元のimg, コピー元のu, コピー元のv, 幅, 高さ)
img.blt(16, 0, 0, 0, 0, 16, 16)

# --- (16,0)にコピーしたクマを金色に変更 ---
for y in range(16):
    for x in range(16):
        # (16,0)からの相対座標でピクセルをチェック
        px_color = img.pget(16 + x, y)
        if px_color == ORIGINAL_BODY: # 元の体の色なら金色に
            img.pset(16 + x, y, GOLD)
        elif px_color == ORIGINAL_SNOUT: # 元の鼻周りの色なら白に
            img.pset(16 + x, y, WHITE)

# --- 変更を保存 ---
pyxel.save("assets.pyxres")

print("assets.pyxresを更新しました: Image 0 の(16,0)に金色の仲間のクマを描画しました。")
