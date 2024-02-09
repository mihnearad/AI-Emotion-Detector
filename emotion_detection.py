import cv2
from deepface import DeepFace
import time

# Function to wrap text and round values based on maximum width
def wrap_and_round_text(text, max_width):
    words = text.split()
    lines = []
    current_line = words[0]

    for word in words[1:]:
        if cv2.getTextSize(current_line + " " + word, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0][0] <= max_width:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return lines

# Open a connection to the webcam
cap = cv2.VideoCapture(0)

# Variables for duration
start_time = time.time()
duration = 4  # seconds

while time.time() - start_time <= duration:
    # Capture frame by frame
    ret, frame = cap.read()

    # Perform face, age, gender, and emotion detection
    result = DeepFace.analyze(frame, actions=['age', 'gender', 'emotion'], enforce_detection=False)

    # Check if the result is a list and take the first element
    if isinstance(result, list):
        result = result[0]

    # Display the frame with age, gender, and emotion 
    max_width = 300  # Adjust this value based on screen width

    # Wrap and round text lines
    age_text = wrap_and_round_text(f"Age: {round(result['age'], 1)}", max_width)
    gender_text = wrap_and_round_text(f"Gender: {result['gender']}", max_width)
    
    if 'emotion' in result:
        # Round emotion values to one decimal place
        rounded_emotion = {key: round(value, 0) for key, value in result['emotion'].items()}
        emotion_text = wrap_and_round_text(f"Emotion: {rounded_emotion}", max_width)
    else:
        emotion_text = ["Emotion: N/A"]

    # Display wrapped and rounded text lines
    y_position = 30
    for line in age_text + gender_text + emotion_text:
        cv2.putText(frame, line, (10, y_position), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        y_position += 30  # Adjust the line spacing as needed

    cv2.imshow('Webcam Analysis', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Print the values
print("Last Values:")
print(f"Age: {round(result['age'], 1)}")
print(f"Gender: {result['gender']}")
if 'emotion' in result:
    print(f"Emotion: {rounded_emotion}")
else:
    print("Emotion: N/A")