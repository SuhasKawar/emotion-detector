from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detector is running"

@app.route("/emotionDetector")
def emotion_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
