import cv2
import time

# initialize the webcam
cap = cv2.VideoCapture(0)

# get the start time
start_time = cv2.getTickCount()

# start capturing frames from the webcam
while True:
    # grab the current frame
    ret, frame = cap.read()

    # check if the frame is returned
    if not ret:
        break

    # calculate the number of frames per second
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - start_time)

    # display the current frame with the fps value
    cv2.putText(frame, "FPS: {:.2f}".format(fps), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    cv2.imshow("Frame", frame)

    # update the start time
    start_time = cv2.getTickCount()

    # break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break