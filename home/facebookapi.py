def facebook(company,local,title,speciality,workplace,amount,rank,worktime,sex,exp,salary,deadline,name,email,contact,des_of_company,describe,require,benefit,skill):
    import facebook

    msg = ""
    token = "EAAje2IAXV2oBAFPQZC6pcdT8ZBfpSl8L2SgqKRv7w3lyWSom00qWmIRrKrIQPbnFbbu8ZAtuPYURrAs3PaP55jYBqTAFqZBDeZCeTANaITLurjalkPTNClOJvNwG7KwpdEttBUorKN0xXX32bHGeJXiy9lJsEiZASvPZA3YEg1zx2niRQKQ51UmbazyLVT6wQm2NpmiDL439gZDZD"
    graph = facebook.GraphAPI(access_token=token)
    groups = graph.get_object("me/groups")
    list1 = [company,local,title,speciality,workplace,amount,rank,worktime,sex,exp,salary,deadline,name,email,contact,des_of_company,describe,require,benefit,skill]
    list2 = ['Công ty','Địa chỉ','Tiêu đề','Chuyên ngành','Nơi làm việc','Số lượng','Cấp bậc','Thời gian','Giới tính','Kinh nghiệm','Mức lương','Hạn chót nộp hồ sơ','Tên người đăng','Email','Số điện thoại','Mô tả về công ty','Mô tả công việc','Yêu cầu','Lợi ích của ứng viên','Kĩ năng']
    for i in range(len(list2)):
        msg = msg + list2[i] + ":" + list1[i] + "\n"
    hashtag = "#tuyendungpython #pythonvietnam"
    graph.put_object("504170536777582", "feed", message=hashtag+"\n"+msg)