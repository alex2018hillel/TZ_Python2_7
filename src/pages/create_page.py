class Create_mail:
    expected_name = "alex2019hillel@ukr.net"

    create_button = "//div[@id='content']/aside/button"
    fild_input = "//input[@name='toFieldInput']"
    fild_subject = "//input[@name='subject']"
    fild_description = "//body[@id='tinymce']/div/span"
    fild_descriptions = "//span[@class='customFontStyle']"
    submit_button = "//div[@class='controls']/button"
    fild_descr = "//div[@class='screens']//div[@class='sendmsg__area']//div[@class='editor']"
    new_create_button = "//a[@id='0']/span[4]"
    action_button = "//button[@class='action']"
    default_button = "//button[@class='default']"

    content_fild = "//td[@class='msglist__row-subject']/a"
    in_mail_box = "//a[@id='0']//span[@class='sidebar__list-link-name']"
    row_check = "//td[@class='msglist__row-check']//input"
    delete_button = "//div[@class='msglist__controls']/a[2]"
