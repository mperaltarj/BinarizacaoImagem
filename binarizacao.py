import cv2

def convert_to_grayscale(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Erro ao carregar a imagem em {image_path}")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite(output_path, gray_image)
    print(f"Imagem salva em escala de cinza em {output_path}")

def convert_to_black_and_white(image_path, output_path, threshold=127):
    # Read the grayscale image
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if gray_image is None:
        print(f"Erro ao carregar a imagem em {image_path}")
        return

    # Apply binary thresholding
    _, bw_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)

    # Save the black and white image
    cv2.imwrite(output_path, bw_image)
    print(f"Imagem salva em preto e branco em {output_path}")

# Example usage
input_image = "imagem/pexels-fhdiakgn-1573919.jpg"
gray_image_path = "imagem/gray_image.jpg"
bw_image_path = "imagem/bw_image.jpg"

convert_to_grayscale(input_image, gray_image_path)
convert_to_black_and_white(gray_image_path, bw_image_path)
