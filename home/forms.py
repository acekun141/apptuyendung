from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import InfomationEnterprise, Post
from django.core.exceptions import ObjectDoesNotExist
import re

class RegistrationForm(forms.Form):
    username = forms.EmailField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control'})
    )
    password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder':'Mật khẩu', 'class':'form-control'})
    )
    password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder':'Nhập lại mật khẩu', 'class':'form-control'})
    )
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if not( password1 == password2 ):
                raise forms.ValidationError('Mật khẩu không hợp lệ!')
            if len(password1) < 6:
                raise forms.ValidationError('Mật khẩu quá ngắn')
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username = username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Tài khoản đã tồn tại')
    def save(self):
        User.objects.create_user(
            username = self.cleaned_data['username'],
            password = self.cleaned_data['password1'],
            email = self.cleaned_data['username']
        )

class SigninForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control'})
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder':'Mật khẩu', 'class':'form-control'})
    )
    def clean(self):
        user = authenticate(username = self.cleaned_data['username'], password = self.cleaned_data['password'])
        if not user:
            raise forms.ValidationError('Mật khẩu hoặc tài khoản không đúng')


class InfoForm(forms.ModelForm):
    company = forms.CharField(
        widget = forms.TextInput(
            attrs={
            'placeholder':'Tên doanh nghiệp',
            'class':'form-control'}
        ),
        max_length=200
    )
    local = forms.CharField(
        max_length=200,
        widget = forms.TextInput(
            attrs={
            'placeholder':'Địa chỉ công ty',
            'class':'form-control'}
        )
    )
    email = forms.EmailField(
        max_length=200,
        widget = forms.TextInput(
            attrs={
            'placeholder':'Email',
            'class':'form-control'}
        )
    )
    contact = forms.CharField(
        max_length=200,
        widget = forms.TextInput(
            attrs={
            'placeholder':'Số điện thoại',
            'class':'form-control'}
        )
    )
    website = forms.CharField(
        max_length=200,
        widget = forms.TextInput(
            attrs={
            'placeholder':'http://website.com',
            'class':'form-control'
            }
        )
    )
    option = [
        ('Dưới 10 nhân viên','Dưới 10 nhân viên'),
        ('Từ 10-49 nhân viên','Từ 10-49 nhân viên'),
        ('Từ 50-99 nhân viên','Từ 50-99 nhân viên'),
        ('Từ 100-499 nhân viên','Từ 100-499 nhân viên'),
        ('Từ 500-1000 nhân viên','Từ 500-1000 nhân viên'),
        ('Trên 1000 nhân viên','Trên 1000 nhân viên'),
    ]
    select = forms.ChoiceField(
        widget = forms.Select(
            attrs={
                'class':'selectDrop',
                'id':'category'
            }
        ),
        choices = option

    )
    describe = forms.CharField(
        max_length=200,
        widget = forms.Textarea(
            attrs={
            'placeholder':'Mô tả công ty',
            'class':'form-control'
            }
        )
    )
    class Meta:
        model = InfomationEnterprise
        fields = '__all__'



class PostForm(forms.Form):
    title = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':"form-control hasGuide",
                'id':"jobTitle",
                'placeholder':'VD: Nhân viên IT',
                'tips':"Viết ngắn gọn, chính xác vị trí + công việc cần tuyển. <span class='red font-italic'>Không sử dụng các từ như [HN], lương cao, tuyển gấp ...</span>",
                'example':"<p class='example-text'>- Nhân viên kinh doanh</p><p class='example-text'>- Chăm sóc khách hàng</p><p class='example-text'>- PHP Developer</p>"
            }
        ),
        max_length=100
    )
    speciality = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':"form-control hasGuide",
                'tips':"Có thể chọn tối đa 3 ngành nghề khác nhau",
                'example':"<p class='example-text'>Thiết kế đồ họa, Thời trang</p>"
            }
        ),
        max_length=200
    )
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
    workplace = forms.ChoiceField(
        widget = forms.Select(
            attrs={
                'id':"address",
                'class':"hasGuide",
                'tips':"Địa điểm làm việc là nơi ứng viên sẽ làm việc sau khi được nhận. Bạn có thể chọn nhiều hơn một địa điểm, có thể chọn quận/huyện.",
                'example':"<p class='example-text'>Hà Nội, TP. HCM, Cầu Giấy,...</p>"      
            }
        ),
        choices=list_workplance
    )
    amount = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control hasGuide',
                'placeholder':"0",
                'tips':"Số lượng cần tuyển, nếu tuyển không xác định thì để trống.",
                'example':"<p class='example-text'>10</p>"
            }
        ),
        max_length=100
    )
    rank = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control hasGuide',
            }
        ),
        max_length=100
    )
    list_worktime = [
        ('Toàn thời gian','Toàn thời gian'),
        ('Bán thời gian','Bán thời gian'),
        ('Thực tập','Thực tập'),
    ]
    worktime = forms.ChoiceField(
        widget = forms.Select(
            attrs={
                'class':"selectDrop",
            } 
        ),
        choices=list_worktime
    )
    list_sex = [
        ('Nam','Nam'),
        ('Nữ','Nữ'),
        ('Nam/Nữ','Nam/Nữ')
    ]
    sex = forms.ChoiceField(
        widget = forms.Select(
            attrs={
                'class':'selectDrop',
                'id':'category'
            }  
        ),
        choices=list_sex
    )
    salary = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control hasGuide',
            }
        ),
        max_length=100
    )
    exp = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control hasGuide',
            }
        ),
        max_length=200
    )
    deadline = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':"form-control dateTime hasGuide",
                'placeholder':"Năm-tháng-ngày",
                'tips':"Hạn chót để ứng viên nộp hồ sơ, nhập theo định dạng <span class='green'>năm-tháng-ngày</span>. Sau ngày này tin tuyển dụng sẽ không được hiển thị.",
                'example':"<p class='example-text'>2019-01-01</p>" 
            }
        ),
        max_length=100
    )
    name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':"form-control hasGuide",
                'placeholder':"Anh Nguyễn Văn A",
                'tips':"Tên người sẽ nhận hồ sơ ứng tuyển để người nộp hồ sơ tiện xưng hô.",
                'example':"<p class='example-text'>Anh Nguyễn Văn A</p>"
            }
        ),
        max_length=100
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'class':"form-control hasGuide",
                'placeholder':"e.g. email@company.com",
                'tips':"Email nhận hồ sơ là thông tin bắt buộc, các đơn ứng tuyển sẽ được gửi trực tiếp về email này sau khi được duyệt.",
                'example':"<p class='example-text'>nguyenvana@company.com</p>" 
            }
        )
    )
    contact = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':"form-control hasGuide",
                'placeholder':"VD: 0000-000-000",
                'tips':"Điện thoại liên hệ của người nhận hồ sơ. Bạn nên ghi chính xác để ứng viên có thể liên hệ khi cần thiết.",
                'example':"<p class='example-text'>0123 456 789</p>"
            }
        ),
        max_length=100
    )
    des_of_company = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':"form-control hasGuide",
                'placeholder':"Viết ngắn gọn khoảng 3 dòng giới thiệu về công ty hoặc dịch vụ của công ty giúp thu hút ứng viên ứng tuyển vào công việc này. Nếu bỏ trống sẽ tự động thay thế bằng thông tin mô tả chung của công ty.",
                'tips':"Mô tả ngắn gọn giới thiệu về công ty của bạn, hoặc sản phẩm của công ty liên quan trực tiếp tới tin tuyển dụng. Mô tả tốt sẽ thu hút sự quan tâm của ứng viên giúp tăng số lượng đơn ứng tuyển.",
                'example':"<p class='example-text'>Công ty A là một công ty về phần mềm, ...</p>"
            }
        ),
        max_length=255
    )
    describe = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'id':"editor",
                'class':'form-control'
            }
        ),
        max_length=1000
    )
    require = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'id':"editor1",
                'class':'form-control'
            }
        ),
        max_length=1000
    )
    benefit = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'id':"editor2",
                'class':'form-control'
            }
        )
    )
    skill = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':"form-control hasGuide",
            }
        ),
        max_length=100
    )

    def clean(self):
        lis = ['title', 'speciality', 'workplace', 'amount','rank','worktime','sex','exp','salary','deadline','name','email','contact','des_of_company','describe','require','benefit','skill']
        for i in lis:
            if not (i in self.cleaned_data):
                raise forms.ValidationError('Vui lòng điền đầy đủ thông tin')
