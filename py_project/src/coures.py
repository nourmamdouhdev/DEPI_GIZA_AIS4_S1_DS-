class coures :
    _id_counter = 1
    def __init__(self, name):
        self.coures_id = coures._id_counter
        coures._id_counter += 1
        self.name = name
        self.ennroled_students=[]
        
    def __str__(self):
            return f"coures name : {self.name} , coures id : {self.coures_id} , students : {len(self.students)} "
        
    def enrrold_student (self,student):
        if student not in self.ennroled_students:
            self.ennroled_students.append(student)
            print("studet ennroled suscessfuly")
        else:
            print("student already ennroled")
            
    def remove_student (self,student):
        if student in self.ennroled_students:
            self.ennroled_students.remove(student)
            print("studet removed suscessfuly")
        else:
            print("student not found")