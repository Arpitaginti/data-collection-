#window close is most important otherwise window will not close
import PySimpleGUI as sg  #importing pysimple gui with its object

#importing mysql connector
import mysql.connector
a=mysql.connector.connect(host="localhost", user="root",password="a1234")
b=a.cursor()
b.execute("use practicle")
#b.execute("create table gui(id int,first char(20),last char(20),address char(20),dob date,number char(20),email varchar(400),gender varchar(20),state varchar(20))")

#describe the strucure of window help of layout
layout=[
    [sg.Text("select any button")],
    [sg.Button("Add")],
    [sg.Button("Search")],
    [sg.Button("display data")],
    [sg.Button("update")],
    [sg.Button("delete")],
    [sg.Button("exit")]
]
#giving window1 a title and layout into one variable
window1=sg.Window("main page",layout).finalize()
window1.Maximize()
while True:
    event,values=window1.read()
    if(event=="Add"):
        #for showing loading bar
        
        #layout for another window
        layout=[
        [sg.Text("ID"),sg.Input(key="-id-")],
        [sg.Text("First Name"),sg.Input(key="-first-")],
        [sg.Text("last Name"),sg.Input(key="-last-")],
        [sg.Text("Email"),sg.Input(key="-email-")],
        [sg.Text("DOB"),sg.Input(key="-dob-")],
        [sg.Text("Address"),sg.Input(key="-add-")],
        [sg.Text("mobile No."),sg.Input(key="-no-")],
        [sg.Text("Gender")],
        [sg.Radio('male', "RADIO1", key="-gender-")],
        [sg.Radio('female', "RADIO1",key="-gender-" )],
        [sg.Text("State")],
        [sg.Listbox(values=('Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana',
                            'Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra' ,'Manipur' ,
                            'Meghalaya',
                            'Mizoram' ,'Nagaland','Odisha' ,'Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana',
                            'Tripura','Uttar Pradesh','Uttarakhand','West Bengal'),size=(30,6),key="-state-")],
        
        [sg.Button("summit"),sg.Button("exit")]
        ]
        #descibing its title and other feature
        window=sg.Window("ADD STUDENT INFO",layout).finalize()
        window.Maximize()
        while True:
                #without read() we dont get any output which we want , if we dont use read() it will give address aur error
                    event,values=window.read()
                    #saving value on another variable
                    ids = values['-id-']
                    first = values['-first-']
                    last = values['-last-']
                    email=values['-email-']
                    dob = values['-dob-']
                    add = values['-add-'] 
                    num = values['-no-'] 
                    gender=values['-gender-']
                    if(gender==True):
                        k="male"
                    else:
                        k="female"
                    st=values[('-state-')]
                    state=st[0]
                    # now using database we save data
                    

                    ab=("insert into gui(id,first , last, address,dob,number,email,gender,state) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                    ba=(ids,first,last,add,dob,num,email,k,state)
                    b.execute(ab,ba)
                    a.commit()
                    if(event=="summit"):
                        break
                    else:
                        break
                        exit()
        window.close()
    elif(event=="Search"):
                layout=[
                [sg.Text("first name"),sg.Input(key="-name-")], 
                #[sg.Text("first name","last name","address","dob","mobile no.","email","gender","state")],    
                [sg.MLine(size=(100, 5), key='l'+sg.WRITE_ONLY_KEY)],
                [sg.Button("display data"),sg.Button("exit")]
                ]
                window=sg.Window("SEARCH STUDENT INFO",layout).finalize()
                window.Maximize()
                while True:
                    event,values=window.read()
                    first = values['-name-']#lata
                    b.execute("select * from gui ")
                    k=b.fetchall()
                    #print(k)
                    lk =  [list(i) for i in k]
                    #print(lk)
                    a.commit()
                    if(event=="display data"):
                    #i=[1003, 'masoom', 'mishra', 'bihar', datetime.date(2000, 10, 25), '9988776655', 'mishramasoom@gmail.com', 'male', 'Bihar']
                        for i in lk:
                            #j=1003
                            for j in i:#(j=lata)
                                if(j==first):#(lata==lata)
                                    ka=i#[101,lata,manral,haldwani,manrallata@gmail.com]
                                    for i in ka:
                                        #print(i)
                                        #for j in i:
                                        window['l'+sg.WRITE_ONLY_KEY].print(i,end='  ', text_color='red', background_color='yellow')
                                    window['l'+sg.WRITE_ONLY_KEY].print()
                        break
                        exit()
                    
                    else:
                        break
                        exit()
                window.close()
    elif(event=="display data"):         
        layout=[
                [sg.MLine(size=(100, 5), key='l'+sg.WRITE_ONLY_KEY)],
                [sg.Button("display data"),sg.Button("exit")
                ]
                ]
        window=sg.Window("DISPLAY ALL DATA OF STUDENT",layout).finalize()
        window.Maximize()
        while True:
            event,values=window.read()
            b.execute("select * from gui")
            kl=b.fetchall()
            a.commit()
            lk =  [list(i) for i in kl]
            if(event=="display data"):
                for i in lk:
                    for j in i:
                        print(j)
                        window['l'+sg.WRITE_ONLY_KEY].print(j,end='    ||     ', text_color='black')   
                    window['l'+sg.WRITE_ONLY_KEY].print()    
            elif(event=="exit"):
                break
                exit()  
        window.close()        
        
    elif(event=="exit"):
            break
            exit() 
    

    elif(event=="update"):
        
        #layout for another window
        layout=[
        [sg.Text("ENTER THE DATA TO UPDATE")],
        [sg.Text("ID"),sg.Input(key="-id-")],
        [sg.Text("First Name"),sg.Input(key="-first-")],
        [sg.Text("last Name"),sg.Input(key="-last-")],
        [sg.Text("Email"),sg.Input(key="-email-")],
        [sg.Text("DOB"),sg.Input(key="-dob-")],
        [sg.Text("Address"),sg.Input(key="-add-")],
        [sg.Text("mobile No."),sg.Input(key="-no-")],
        [sg.Text("Gender")],
        [sg.Radio('male', "RADIO1", key="-gender-")],
        [sg.Radio('female', "RADIO1",key="-gender-" )],
        [sg.Text("State")],
        [sg.Listbox(values=('Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa''Gujarat','Haryana',
                            'Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra' ,'Manipur' ,
                            'Meghalaya',
                            'Mizoram' ,'Nagaland','Odisha' ,'Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana',
                            'Tripura','Uttar Pradesh','Uttarakhand','West Bengal'),size=(30,6),key="-state-")],
        
        [sg.Button("summit"),sg.Button("exit")]
        ]
        #descibing its title and other feature
        window=sg.Window("UPDATE DATA OF STUDENT",layout).finalize()
        window.Maximize()
        while True:
                #without read() we dont get any output which we want , if we dont use read() it will give address aur error
                    event,values=window.read()
                    #saviny value on another variable
                    ids = values['-id-']
                    first = values['-first-']
                    last = values['-last-']
                    email=values['-email-']
                    dob = values['-dob-']
                    add = values['-add-'] 
                    num = values['-no-'] 
                    gender=values['-gender-']# 0,1
                    if(gender==True):
                        k="male"
                    else:
                        k="female"
                    st=values[('-state-')]
                    state=st[0]
                    #in which we have store the value now using database we save it
                    

                    
                    ab=("update gui set first=%s where gui.id= %s")
                    #ab=("update gui set first=shubhi where gui.id= 103")
                    #first=lata 
                    ba=(first,ids,)
                    b.execute(ab,ba,)
                    a.commit()
                    ab=("update gui set  last=%s where id= %s")
                    ba=(last,ids)
                    b.execute(ab,ba)
                    a.commit()
                    ab=("update gui set  address=%s where id= %s")
                    ba=(add,ids)
                    b.execute(ab,ba)
                    a.commit()
                    ab=("update gui set dob=%s  where id= %s")
                    ba=(dob,ids)
                    b.execute(ab,ba)
                    a.commit()
                    ab=("update gui set number=%s where id= %s")
                    ba=(num,ids)
                    b.execute(ab,ba)
                    a.commit()
                    ab=("update gui set  email=%s where id= %s")
                    ba=(email,ids)
                    b.execute(ab,ba)
                    a.commit()
                    ab=("update gui set  gender=%s  where id= %s")
                    ba=(k,ids)
                    b.execute(ab,ba)
                    a.commit()
                    ab=("update gui set state=%s where id= %s")
                    ba=(state,ids)
                    b.execute(ab,ba)
                    a.commit()
                    if(event=="summit"):
                        sg.Text("summited")
                        break
                    else:
                        break
        window.close()
    elif(event=="delete"):
                layout=[
                [sg.Text("id"),sg.Input(key="-ids-")], 
                [sg.Button("exit"),sg.Button("delete")]
                ]
                
                window=sg.Window("DELETE DATA",layout).finalize()
                window.Maximize()
                while True:
                    event,values=window.read()
                    ids = values['-ids-']
                        
                    iid=int(ids)
                    #print(int(iid))
                    b.execute("select * from gui ")
                    k=b.fetchall()
                    lk =  [list(i) for i in k]
                    a.commit()
                    if(event=="exit"):
                        break
                        exit()
                    else:
                        for i in lk:
                            if(i[0]==iid):
                                    ba=("delete from gui where gui.id = '%s'") 
                                    ab=(iid,)
                                    b.execute(ba,ab,)
                                    break
                                    exit()
                window.close()
window1.close()

        
    