class Kid(object):
    def __init__(self,name,gender,age,parent_name,tel,address,payment_info,teacher,memo):
        self.name=name
        self.gender=gender
        self.age=age
        self.parent_name=parent_name
        self.tel=tel
        self.address=address
        self.payment_info=payment_info
        self.teacher=teacher
        self.memo=memo
    def __str__(self):
        return f"KID's info: {self.name},{self.gender},{self.age},{self.parent_info}.{self.tel}," \
               f"{self.address},{self.payment_info},{self.teacher},{self.memo}"