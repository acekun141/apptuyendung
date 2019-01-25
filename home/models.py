from django.db import models

# Create your models here.

class InfomationEnterprise(models.Model):
    username = models.CharField(max_length=100) # Tên tài khoản
    company = models.CharField(max_length=200)  # Tên công ty
    local = models.CharField(max_length=200) # Địa chỉ 
    email = models.EmailField() # Email
    contact = models.CharField(max_length=100) # Số điện thoại
    website = models.CharField(max_length=500)
    option = [
        ('Dưới 10 nhân viên','Dưới 10 nhân viên'),
        ('Từ 10-49 nhân viên','Từ 10-49 nhân viên'),
        ('Từ 50-99 nhân viên','Từ 50-99 nhân viên'),
        ('Từ 100-499 nhân viên','Từ 100-499 nhân viên'),
        ('Từ 500-1000 nhân viên','Từ 500-1000 nhân viên'),
        ('Trên 1000 nhân viên','Trên 1000 nhân viên'),
    ]
    select = models.CharField(max_length=100,choices=option) # Số nhân viên trong công ty
    describe = models.TextField()

    def __str__(self):
        return self.username

class Post(models.Model):
    username = models.ForeignKey(InfomationEnterprise, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    speciality = models.CharField(max_length=200) # Chuyên ngành
    list_workplance = [
        ('Hà Nội', 'Hà Nội'),
        ('Hồ Chí Minh', 'Hồ Chí Minh'),
        ('Bình Dương', 'Bình Dương'),
        ('Bắc Ninh', 'Bắc Ninh'),
        ('Đồng Nai', 'Đồng Nai'),
        ('Hưng Yên', 'Hưng Yên'),
        ('Hải Dương', 'Hải Dương'),
        ('Đà Nẵng', 'Đà Nẵng'),
        ('Hải Phòng', 'Hải Phòng'),
    ]
    workplace = models.CharField(max_length=100,choices=list_workplance) # Nơi làm việc
    amount = models.CharField(max_length=100) # Số lượng tuyển dụng
    rank = models.CharField(max_length=100) # Cấp bậc tuyển dụng
    list_worktime = [
        ('Toàn thời gian','Toàn thời gian'),
        ('Bán thời gian','Bán thời gian'),
        ('Thực tập','Thực tập'),
    ]
    worktime = models.CharField(max_length=1, choices=list_worktime) # Thời gian tuyển dụng
    list_sex = [
        ('Nam','Nam'),
        ('Nữ','Nữ'),
        ('Nam/Nữ','Nam/Nữ')
    ]
    sex = models.CharField(max_length=100, choices=list_sex)
    exp = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100) # Hạn chót nộp hồ sơ
    name = models.CharField(max_length=100) # Tên người đăng tin
    email = models.EmailField() 
    contact = models.CharField(max_length=100)
    des_of_company = models.TextField(max_length=255) # Mô tả về công ty
    describe = models.TextField() # Mô tả về công việc
    require = models.TextField() # Yêu cầu
    benefit = models.TextField(default='') # Quyền lợi của ứng viên
    skill = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

