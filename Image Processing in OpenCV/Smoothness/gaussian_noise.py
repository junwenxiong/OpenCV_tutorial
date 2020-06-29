from skimage import util
import cv2

if __name__ == "__main__":
    img = cv2.imread('resource\\1.jpg')

    noise_gs_img = util.random_noise(img, 'gaussian')

    cv2.imshow('original image', img)
    cv2.imshow('gs noise', noise_gs_img)
    noise_gs_img = cv2.normalize(noise_gs_img, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    cv2.imwrite('resource\\1_gs_noise.jpg', noise_gs_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()