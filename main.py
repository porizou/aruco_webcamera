# -*- coding: utf-8 -*
import cv2
import numpy as np
aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# 二次元コードの番号が0の時の動作モード
def Mode0():
    print(0)
# 二次元コードの番号が1の時の動作モード
def Mode1():
    print(1)
# 二次元コードの番号が2の時の動作モード
def Mode2():
    print(2)
# 二次元コードの番号が3の時の動作モード
def Mode3():
    print(3)

def main():
    cap = cv2.VideoCapture(0) #ビデオキャプチャの開始
    while True:

        ret, frame = cap.read() #ビデオキャプチャから画像を取得

        Height, Width = frame.shape[:2] #sizeを取得

        img = cv2.resize(frame,(int(Width),int(Height)))

        corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary) #マーカを検出

        aruco.drawDetectedMarkers(img, corners, ids, (0,255,0)) #検出したマーカに描画する

        cv2.imshow('drawDetectedMarkers', img) #マーカが描画された画像を表示


        #id配列をnumpy配列に変換
        ID = np.array(ids)
        # ARマーカーが検出されたら処理を実行する
        if ids is not None:
            #検出した番号による動作モードを実行
            if ID[0,0]==0:
                Mode0()
            if ID[0,0]==1:
            	Mode1()
            if ID[0,0]==2:
            	Mode2()
            if ID[0,0]==3:
            	Mode3()
            

        # Enterキーが押されたら終了する
        if cv2.waitKey(1) == 13:
    	    break

    cap.release() #ビデオキャプチャのメモリ解放
    cv2.destroyAllWindows() #すべてのウィンドウを閉じる

if __name__ == '__main__':
    main()
