import cv2
import time
import os

# カメラデバイスを開く
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("カメラを開けませんでした。")
    exit()

# 画像を保存するディレクトリを指定（存在しなければ作成）
save_dir = "calibration_images"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

try:
    count = 0
    while True:
        # カメラから1フレーム読み込む
        ret, frame = cap.read()
        if not ret:
            print("フレームの取得に失敗しました。")
            break

        # 現在の時間をファイル名に使用
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = os.path.join(save_dir, f"image_{timestamp}_{count}.jpg")
        # 画像をファイルに保存
        cv2.imwrite(filename, frame)
        print(f"{filename} に保存しました。")
        # 5秒待機
        time.sleep(5)
        count += 1

except KeyboardInterrupt:
    print("プログラムを終了します。")

finally:
    # カメラデバイスを解放
    cap.release()
    cv2.destroyAllWindows()
