class Course:
    def __init__(self, course_name, price):
        self.course_name = course_name
        self.price = price

    def show_course(self):
        print("Course:", self.course_name)
        print("Price:", self.price)


class ProgrammingCourse(Course):
    def __init__(self, course_name, price, language, duration):
        super().__init__(course_name, price)
        self.language = language
        self.duration = duration

    def show_programming_course(self):
        self.show_course()
        print("Language:", self.language)
        print("Duration:", self.duration)


p1 = ProgrammingCourse("Python", 5000, "Python", "3 Months")
p2 = ProgrammingCourse("Java", 6000, "Java", "4 Months")

p1.show_programming_course()
print()
p2.show_programming_course()


class Camera:
    def __init__(self, camera_mp):
        self.camera_mp = camera_mp

    def take_photo(self):
        print("Camera:", self.camera_mp, "MP")


class MusicPlayer:
    def __init__(self, brand):
        self.brand = brand

    def play_music(self):
        print("Music Brand:", self.brand)


class SmartPhone(Camera, MusicPlayer):
    def __init__(self, model_name, camera_mp, brand):
        Camera.__init__(self, camera_mp)
        MusicPlayer.__init__(self, brand)
        self.model_name = model_name

    def show_details(self):
        print("Model:", self.model_name)
        self.take_photo()
        self.play_music()


s1 = SmartPhone("iPhone 14", 48, "Apple")
s2 = SmartPhone("Samsung S22", 50, "Samsung")

s1.show_details()
print()
s2.show_details()