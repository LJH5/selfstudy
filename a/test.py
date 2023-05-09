import numpy as np
import cv2

# PGM 파일을 읽어와 numpy 배열로 변환
pgm_file = cv2.imread('map.pgm', cv2.IMREAD_GRAYSCALE)

# PGM 파일의 각 픽셀 값을 그리드 맵의 셀 값으로 변환
grid_map = np.zeros_like(pgm_file)
grid_map[pgm_file < 250] = 100

# 변환된 Grid map을 txt 파일로 저장
np.savetxt('map.txt', grid_map, fmt='%d')
