# -*- coding: utf-8 -*-
height = float(input('请输入小明身高(m):'));
weight = float(input('请输入小明体重(kg):'));
bmi = weight/height**2;
c1 = None;
while c1 != '2':
    if bmi<=18.5:
        print('过轻！');
    elif bmi<=25:
        print('正常');
    elif bmi<=28:
        print('过重');
    elif bmi<=32:
        print('肥胖');
    else:
        print('严重肥胖');
    c1 = input('请选择后续操作:\n\t\t1.修改数据\n\t\t2.退出\n')
    if c1 == '1':
        c2 = input('请选择要修改的数据:\n\t\t1.体重\n\t\t2.身高\n\t\t3.体重&身高\n');
        if c2 == '1':
            weight = float(input('请输入修改后的体重:'));
        elif c2 == '2':
            height = float(input('请输入修改后的身高:'));
        elif c2 == '3':
            weight = float(input('请输入修改后的体重:'));
            height = float(input('请输入修改后的身高:'));
        bmi = weight/height**2;
print('bye');
