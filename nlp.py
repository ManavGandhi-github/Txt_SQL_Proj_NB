def process_query(query):
    """
    This function takes a query as input, processes the query to determine the intent, and returns the intent.
    For now, it only checks if the query contains the words "average" and "mission time", and if so, returns the intent 'average_mission_time'.
    If the query does not contain these words, it returns 'unknown'.
    """
    # Convert the query to lowercase
    query = query.lower()

    # Check for keywords in the query and return the corresponding intent
    if 'average' in query and 'mission time' in query:
        return 'average_mission_time'
    else:
        return 'unknown'


if __name__ == '__main__':
    # Test the process_query function
    print(process_query('What is the average mission time?'))  # Should print 'average_mission_time'
    print(process_query('Some other query'))  # Should print 'unknown'
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

# This is our training data
# In a real-world scenario, you would want a much larger and more diverse training set
training_data = [
    ('What is the average mission time?', 'average_mission_time'),
    ('Tell me about the mission', 'mission_details'),
    ('Give me details about LGV', 'lgv_details'),
    # You can add more examples as needed
]

# We create a NaiveBayesClassifier with our training data
clf = NaiveBayesClassifier(training_data)

def process_query(query):
    """
    This function takes a query as input, processes the query to determine the intent, and returns the intent.
    It uses a Naive Bayes Classifier trained on example queries to determine the intent.
    """
    # We use the classifier to classify the query
    intent = clf.classify(query)
    return intent


if __name__ == '__main__':
    # Test the process_query function
    print(process_query('What is the average mission time?'))  # Should print 'average_mission_time'
    print(process_query('Tell me about the mission'))  # Should print 'mission_details'
    print(process_query('Give me details about LGV'))  # Should print 'lgv_details'
    print(process_query('Some other query'))  # Might print any of the intents, as this query was not in the training data
