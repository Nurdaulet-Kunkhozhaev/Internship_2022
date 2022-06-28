IP_ADDR = "127.0.0.1"
PORT = 65432
BUF_SIZE = 1000

from socket import socket, AF_INET, SOCK_DGRAM
import cv2

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((IP_ADDR, PORT))

camera = cv2.VideoCapture(0)
cv2.namedWindow("test")

img_counter = 0

while True:
    print("Waiting for a new packet. .. ... ")

    data, addr = sock.recvfrom(BUF_SIZE)

    if data is None:
        print("Waiting for a client")
    else:
        ret, frame = camera.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        stopKey = cv2.waitKey(1)
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

        print(f"Packet contains info: {data.decode()}")

    print()

    if stopKey % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

camera.release()
cv2.destroyAllWindows()
