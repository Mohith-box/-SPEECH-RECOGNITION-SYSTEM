# -SPEECH-RECOGNITION-SYSTEM

COMPANY: CODTECH IT SOLUTIONS

NAME: Mohith B

INTERN ID: CT06WRL

DOMAIN: Artificial intelligence

DURATION: 6 WEEKS

MENTOR: NEELA SANTOSH


#OBJECTIVE

The goal of Task 2 was to build a Speech-to-Text tool using pre-trained models and libraries that can accurately transcribe audio files into written text. This task demonstrates the use of Automatic Speech Recognition (ASR) — a key component in AI-powered virtual assistants, transcription tools, and voice-controlled systems.

WHAT IS THE TOOL WE CREATED?

We developed a simple but effective Speech-to-Text Transcription Tool using the SpeechRecognition Python library. This tool processes a .wav audio file and returns a textual representation of the spoken content.

🔹 Functionality:
Takes a short audio file (.wav) as input.

Processes the audio using Google Web Speech API (via SpeechRecognition).

Outputs the spoken content as plain text.

🔹 Key Features:
Easy to use and lightweight.

Requires minimal configuration.

Works offline with local .wav files and online with cloud APIs.

Accurate for clean and short audio clips.

#PLATFORM & TECHNOLOGY STACK

Component	Details

Language	Python

Libraries	SpeechRecognition, pyaudio or wave (for audio input)

Model/API	Google Web Speech API (used internally by SpeechRecognition)

Execution	Command-line Python script

Runtime	CPU

Development	Any Python IDE / Terminal

#How the Tool Works (Behind the Scenes)

Audio Loading: The user supplies a .wav file containing clear spoken content.

Preprocessing: The SpeechRecognition library loads and decodes the audio into chunks.

Model Inference: The audio is sent to Google’s API (or processed locally), where speech is converted into text.

Output Display: The text is printed to the screen and optionally saved to a file

#Why This Is Valuable

Speech-to-Text technology is the foundation of voice-based AI interfaces — from smart speakers like Alexa to mobile voice assistants like Siri and Google Assistant. This task helps demonstrate how to build an intelligent interface between sound and written language.

