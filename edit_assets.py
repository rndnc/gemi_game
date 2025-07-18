import pyxel

# --- 色の定義 ---
# レモン用
YELLOW = 10
LIGHT_YELLOW = 11
BROWN = 6
# 虫用
DARK_PURPLE = 2
BLACK = 0
WHITE = 7
RED = 8

# --- Pyxelの初期化 ---
pyxel.init(16, 16, display_scale=0) # 画面は不要

# --- アセットファイルのロード ---
try:
    pyxel.load("assets.pyxres")
except Exception:
    print("assets.pyxresが見つかりません。空の状態で続行します。")

# --- Image 1: レモンの描画 (8x8) ---
img1 = pyxel.image(1)
img1.cls(0) # 背景を黒でクリア
# レモンの本体 (黄色)
img1.circ(3, 3, 3, YELLOW)
img1.rect(3, 0, 3, 7, YELLOW)
# ハイライト (明るい黄色)
img1.pset(3, 1, LIGHT_YELLOW)
img1.pset(4, 2, LIGHT_YELLOW)
# ヘタ (茶色)
img1.pset(6, 1, BROWN)
img1.pset(7, 0, BROWN)

# --- Image 2: 虫の描画 (8x8) ---
img2 = pyxel.image(2)
img2.cls(0) # 背景を黒でクリア
# 体 (濃い紫)
img2.rect(1, 2, 6, 4, DARK_PURPLE)
# 足 (黒)
img2.rect(1, 6, 1, 1, BLACK)
img2.rect(3, 6, 1, 1, BLACK)
img2.rect(5, 6, 1, 1, BLACK)
# 目 (赤)
img2.pset(2, 3, RED)
img2.pset(5, 3, RED)

# --- 変更を保存 ---
pyxel.save("assets.pyxres")

print("assets.pyxresを更新しました: Image 1にレモン、Image 2に虫を描画しました。")
