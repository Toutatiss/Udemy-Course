class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        pass
    
user_1 = User("001", "felix")
user_2 = User("002", "felony")

user_1.follow(user_2)