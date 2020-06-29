from skimage import util
import cv2

if __name__ == "__main__":
    img  = cv2.imread('resource\\1.jpg')
    # 产生椒盐噪声, 输出图像为float64格式
    noise_sp_img = util.random_noise(img, mode='s&p')
    print(noise_sp_img[0])

    cv2.imshow('img', img)
    cv2.imshow('sp noise', noise_sp_img)

    noise_sp_img = cv2.normalize(noise_sp_img, None, 0, 255, cv2.NORM_MINMAX,cv2.CV_8U)
    cv2.imwrite('resource\\1_sp_noise.jpg', noise_sp_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()