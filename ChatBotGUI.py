import sys
import csv
import tensorflow as tf
import openai
import PyQt6
openai.api_key = "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"

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QVBoxLayout, QWidget

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and layout
        self.setWindowTitle("Mental Health FAQ Chatbot")
        self.layout = QVBoxLayout()

        # Create the text field and label
        self.text_field = QLineEdit(self)
        self.text_field.returnPressed.connect(self.ask_question)
        self.label = QLabel(self)

        # Add the text field and label to the layout
        self.layout.addWidget(self.text_field)
        self.layout.addWidget(self.label)

        # Set the central widget and show the window
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        self.show()

    def ask_question(self):
        # Welcome the user
        self.label.setText("Hello! How can I help you today?")

        # Get the user's question from the text field
        question = self.text_field.text().lower()  # convert the question to lowercase

        if question == "bye" or question == "goodbye":
            # If the user says "bye" or "goodbye", exit the program
            self.label.setText("Goodbye!")
            #sys.exit()
        else:
            # Encode the user's question
            question_encoded = tokenizer.texts_to_sequences([question])
            question_padded = tf.keras.preprocessing.sequence.pad_sequences(question_encoded, maxlen=max_input_length,
                                                                            padding='post')

            # Generate a response using the model
            response_probs = model.predict(question_padded)
            response_index = tf.argmax(response_probs, axis=-1)
            #response_text = tokenizer.sequences_to_texts([response_index])[0]
            response_text = tokenizer.sequences_to_texts([response_index.numpy().tolist()])[0]

            completions = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"{response_text}\n",
                max_tokens=1024,
                n=1,
                temperature=0.5,
            )

            # Get the refined response from the OpenAI API
            response = completions.choices[0].text


            # Set the label text to the refined response
            self.label.setText(response)


# Load the data from the CSV file
questions = []
answers = []
with open('Data/Mental_Health_FAQ.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        questions.append(row['Questions'])
        answers.append(row['Answers'])

# Preprocess the data for training
questions_preprocessed = [q for q in questions]
answers_preprocessed = [a for a in answers]

# Tokenize the input data
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(questions_preprocessed)

# Encode the input data as sequences of integers
questions_encoded = tokenizer.texts_to_sequences(questions_preprocessed)

# Pad the input sequences to the same length
max_input_length = max([len(q) for q in questions_encoded])
questions_padded = tf.keras.preprocessing.sequence.pad_sequences(questions_encoded, maxlen=max_input_length, padding='post')

# Tokenize the output data
answers_encoded = tokenizer.texts_to_sequences(answers_preprocessed)

# Pad the output sequences to the same length
max_output_length = max([len(a) for a in answers_encoded])
answers_padded = tf.keras.preprocessing.sequence.pad_sequences(answers_encoded, maxlen=max_output_length, padding='post')

# Create a model for training
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=64, input_length=max_input_length),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(max_output_length, activation='softmax')
])

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(questions_padded, answers_padded, epochs=10)

# Create an instance of the chatbot window
app = QApplication(sys.argv)
window = ChatbotWindow()
sys.exit(app.exec())

