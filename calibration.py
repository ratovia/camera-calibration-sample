import numpy as np
import cv2
import glob
import json

# コンフィグファイルの読み込み
def load_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

# 設定の使用
config = load_config('config.json')
resolution = config['resolution']
width, height = resolution['width'], resolution['height']

# 校正するための準備として、チェスボードのコーナーを検出します。
chessboard_size = (7, 6)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((chessboard_size[0]*chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0],
                       0:chessboard_size[1]].T.reshape(-1, 2)

objpoints = []  # 3D point in real world space
imgpoints = []  # 2D points in image plane.

# 画像サイズを格納する変数に直接値を設定
image_size = (height, width)

images = glob.glob('calibration_images/*.jpg')

print(images)
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 画像サイズを取得
    if image_size is None:
        image_size = gray.shape[::-1]

    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(
            gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        print(imgpoints.count)

        cv2.drawChessboardCorners(img, chessboard_size, corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

# 画像サイズが確定していることを確認
if image_size is not None:
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
        objpoints, imgpoints, image_size, None, None)
    print("Camera matrix : \n", mtx)
    print("dist : \n", dist)
    print("rvecs : \n", rvecs)
    print("tvecs : \n", tvecs)
else:
    print("画像サイズが取得できませんでした。")
