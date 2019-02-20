def facebook(company,local,title,speciality,workplace,amount,rank,worktime,sex,exp,salary,deadline,name,email,contact,des_of_company,describe,require,benefit,skill):
    import facebook

    msg = ""
    token = "EAAje2IAXV2oBAD50NMSyPcuBBsbkaNSM87jTnlEAlEGntxk4IVf5HU2NUyxq7BljPDJqsOfJyTeRmeNZAhriOh8npA7u4fBO2mZAbL4fffRvxt3j22AvfK9ywMEGbuhggPpeXXf8xvyWFWu8E9boVveQIHIZChS7BrnT5tDIN7hohwZBxrNZCZBZBrsIu0lqG0pjRZBZBfUQALgZDZD"
    graph = facebook.GraphAPI(access_token=token)
    groups = graph.get_object("me/groups")
    list1 = [company,local,title,speciality,workplace,amount,rank,worktime,sex,exp,salary,deadline,name,email,contact,des_of_company,describe,require,benefit,skill]
    list2 = ['Công ty','Địa chỉ','Tiêu đề','Chuyên ngành','Nơi làm việc','Số lượng','Cấp bậc','Thời gian','Giới tính','Kinh nghiệm','Mức lương','Hạn chót nộp hồ sơ','Tên người đăng','Email','Số điện thoại','Mô tả về công ty','Mô tả công việc','Yêu cầu','Lợi ích của ứng viên','Kĩ năng']
    for i in range(len(list2)):
        msg = msg + list2[i] + ":" + list1[i] + "\n"
    hashtag = "#tuyendungpython #pythonvietnam"
    graph.put_object("504170536777582", "feed", message=hashtag+"\n"+msg)