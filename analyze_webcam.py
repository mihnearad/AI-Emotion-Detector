import cv2
from deepface import DeepFace
import time

#function to get the webcam data

def analyze_webcam(duration=4):
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)

    # Variables for duration
    start_time = time.time()

    # Variables for results
    total_age = 0
    num_frames = 0
    max_gender = None
    max_emotion = None

    while time.time() - start_time <= duration:
        # Capture frame by frame
        ret, frame = cap.read()

        # Perform face, age, gender, and emotion detection
        result = DeepFace.analyze(frame, actions=['age', 'gender', 'emotion'], enforce_detection=False)

        # Check if the result is a list and take the first element
        if isinstance(result, list):
            result = result[0]

        # Accumulate age values
        total_age += result['age']
        num_frames += 1

        # Update max_gender if a higher confidence value is found
        if 'gender' in result:
            max_gender = max(result['gender'], key=result['gender'].get)
        else:
            max_gender = "N/A"

        # Find the emotion with the highest value
        if 'emotion' in result:
            max_emotion = max(result['emotion'], key=result['emotion'].get)
        else:
            max_emotion = "N/A"

        # Display the frame with age, gender, and emotion 
        max_width = 300  # Adjust this value based on screen width

        # Display wrapped and rounded text lines
        y_position = 30
        for line in [
            f"Average Age: {round(total_age / num_frames, 1)}",
            f"Highest Gender: {max_gender}",
            f"Highest Emotion: {max_emotion}"
        ]:
            cv2.putText(frame, line, (10, y_position), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            y_position += 30  # Adjust the line spacing as needed

        cv2.imshow('Webcam Analysis', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return total_age / num_frames, max_gender, max_emotion

# Example usage:
average_age, gender_result, emotion_result = analyze_webcam(duration=4)

# Print the results
print("Last Values:")
print(f"Average Age: {round(average_age, 1)}")
print(f"Highest Gender: {gender_result}")
print(f"Highest Emotion: {emotion_result}")
