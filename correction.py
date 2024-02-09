import cv2
import numpy as np

import json

# コンフィグファイルの読み込み
def load_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

# 設定の使用
config = load_config('config.json')
image_path = config['image_path']

# ==============================================================================

# 変数に代入する
# Camera matrix :
#  [[1.37122343e+03 0.00000000e+00 3.70495684e+02]
#  [0.00000000e+00 1.38246611e+03 6.35750714e+02]
#  [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
# dist :
#  [[ 0.00198131  0.03103268  0.00191343 -0.00208937 -0.04526965]]
# rvecs :
#  (array([[0.54175799],
#        [0.40481243],
#        [0.19647394]]),)
# tvecs :
#  (array([[ 10.41512675],
#        [-13.8451441 ],
#        [ 31.88547683]]),)

# カメラ行列
mtx = [
    [1.37122343e+03, 0.00000000e+00, 3.70495684e+02],
    [0.00000000e+00, 1.38246611e+03, 6.35750714e+02],
    [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]

# 歪み係数
dist = [[0.00198131,  0.03103268,  0.00191343, -0.00208937, -0.04526965]]


# ==============================================================================
mtx = np.array(mtx)
dist = np.array(dist)

# 補正前の画像を読み込む
# 実際の画像パスに置き換えてください
img = cv2.imread(image_path)

# cv2.undistort関数を使用して画像の歪みを補正する
dst = cv2.undistort(img, mtx, dist, None, mtx)

# 補正後の画像を表示する
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.imshow('Undistorted Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
