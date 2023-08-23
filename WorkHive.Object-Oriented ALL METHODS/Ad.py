class Ad():
    def __init__(self, username, category, description, price):
        self.username = username
        self.category = category
        self.description = description
        self.price = float(price)
        self.favoritos = 0
        self.feedbacks = []

    def add_feedback(self, feedback):
        self.feedbacks.append(feedback)
