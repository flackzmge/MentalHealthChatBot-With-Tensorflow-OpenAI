# Mental Health FAQ Chatbot

This is a PyQt6 chatbot that provides answers to frequently asked questions about mental health. The chatbot uses a trained model to generate initial responses, which are then refined using the OpenAI API.

## How to Use

Clone or download the repository.
Install the required packages: PyQt6, tensorflow, and openai.
Run the chatbot by executing python `ChatBotGUI.py`.
Type your question in the text field and press the return key to receive a response.
To exit the chatbot, type "bye" or "goodbye" in the text field.
`Note`: The chatbot is currently incomplete and the responses may not be very accurate. Work is ongoing to improve the response quality.

### Important!
For this to work you will need to use your own Open AI key and swap it in for mine in the code

## Data

The data for the chatbot is stored in the Data/Mental_Health_FAQ.csv file in the following format:

```
Question_ID,Questions,Answers
1590140,
"What does it mean to have a mental illness?", 
"Mental illnesses are health conditions that disrupt a person’s thoughts, emotions, relationships, and daily functioning. They are associated with distress and diminished capacity to engage in the ordinary activities of daily life. Mental illnesses fall along a continuum of severity: some are fairly mild and only interfere with some aspects of life, such as certain phobias. On the other end of the spectrum lie serious mental illnesses, which result in major functional impairment and interference with daily life. These include such disorders as major depression, schizophrenia, and bipolar disorder, and may require that the person receives care in a hospital. It is important to know that mental illnesses are medical conditions that have nothing to do with a person’s character, intelligence, or willpower. Just as diabetes is a disorder of the pancreas, mental illness is a medical condition due to the brain’s biology. Similarly to how one would treat diabetes with medication and insulin, mental illness is treatable with a combination of medication and social support. These treatments are highly effective, with 70-90 percent of individuals receiving treatment experiencing a reduction in symptoms and an improved quality of life. With the proper treatment, it is very possible for a person with mental illness to be independent and successful."

2110618,
"Who does mental illness affect?", 
"It is estimated that mental illness affects 1 in 5 adults in America, and that 1 in 24 adults have a serious mental illness. Mental illness does not discriminate; it can affect anyone, regardless of gender, age, income, social status, ethnicity, religion, sexual orientation, or background. Although mental illness can affect anyone, certain conditions may be more common in different populations. For instance, eating disorders tend to occur more often in females, while disorders such as attention deficit/hyperactivity disorder is more prevalent in children. Additionally, all ages are susceptible, but the young and the old are especially vulnerable. Mental illnesses usually strike individuals in the prime of their lives, with 75 percent of mental health conditions developing by the age of 24. This makes identification and treatment of mental disorders particularly difficult, because the normal personality and behavioral changes of adolescence may mask symptoms of a mental health condition. Parents and caretakers should be aware of this fact, and take notice of changes in their child’s mood, personality, personal habits, and social withdrawal. When these occur in children under 18, they are referred to as serious emotional disturbances (SEDs)."
```

The data is preprocessed and tokenized using the TensorFlow Tokenizer class before being used to train the model.

## Model

The model used by the chatbot is a TensorFlow neural network that takes in a padded sequence of integers representing the user's question and outputs a probability distribution over the possible responses. The response with the highest probability is selected as the initial response.

## Refining Responses with OpenAI

The initial response is then passed to the OpenAI API, which generates a refined response using the Text-Davinci-003 engine. The refined response is returned to the chatbot and displayed to the user.

## Limitations

The chatbot is currently a work in progress and the responses may not be very accurate. Further work is needed to improve the response quality and increase the coverage of the FAQs.
