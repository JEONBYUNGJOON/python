# dictionary : 키(값의 이름)와 값의 쌍
ice={"바밤바":1000, "옥동자":1200, "월드콘":2000}
print(ice)
#Read
print(ice["바밤바"])
#월드콘의 가격
print(ice['월드콘'])
#create
ice['빵빠레']=1500
print(ice)
#update
ice['빵빠레']=1800
#delete
del ice['빵빠레']
print(ice)