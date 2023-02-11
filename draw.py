import cv2

# initialize the webcam
cap = cv2.VideoCapture(0)

# initialize the counter
counter = 10

# start capturing frames from the webcam
while True:
    # grab the current frame
    ret, frame = cap.read()

    # check if the frame is returned
    if not ret:
        break
    
    cv2.waitKey(1000)
    # increment the counter
    counter -= 1

    # display the current frame with the counter value
    cv2.putText(frame, str(counter), (550, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    cv2.imshow("Frame", frame)

    # break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the webcam and close the window
cap.release()
cv2.destroyAllWindows()