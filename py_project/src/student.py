class student :
    id_counter = 1
    def __init__(self, name):
        self.id = student.id_counter
        student.id_counter += 1
        self.name = name
        self.grad={}
        self.coures=[]
        
    def __str__(self):
            return f"student name : {self.name} , student id : {self.id} , courses : {self.coures} , grades : {self.grad} "
    def __repr__(self):
        return f"student name : {self.name} , student id : {self.id}, courses : {self.coures} , grades : {self.grad} "
    def add_grad(self,course_id,grade):
        """
        add grade for specific course
        pram1 : take course id
        pram1 : int

        pram2 : take grade
        type int
        returns: grad
        """
        self.grad[course_id]=grade
        
        
    def add_course (self,course):
        self.coures.append(course)
        
    def enroll_in_course (self,course):
        self.enroll_in_course.append(course)