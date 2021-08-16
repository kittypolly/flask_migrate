from main import AOA, db
#document는 이 주소를 참고하세요. https://flask-sqlalchemy.palletsprojects.com/en/2.x

db.create_all()


## CREATE ##

Seolhyun = AOA('Seolhyun', 1995)
Hyejeong = AOA('Hyejeong', 1994)

# db.session.add(Seolhyun)
# db.session.add(Hyejeong)
# 아래와 같이 한 줄로 바꿔서 쓸 수 있다.
db.session.add_all([Seolhyun, Hyejeong])
db.session.commit()


## READ ##
all_members = AOA.query.all()
print(f"{all_members} 처음으로 모든 멤버를 읽어왔습니다.")

# Getting user by primary key #
print(f"{AOA.query.get(2)} primary key로 찾은 뒤에 출력했습니다.")

# Find by filter #
# all()을 넣어주지 않으면 쿼리문이 출력된다.
# 리스트형태이므로 [0]처럼 인덱스를 지정해주지 않으면 리스트 형태로 출력된다.
filter_name = AOA.query.filter_by(name = 'Seolhyun')
print(f"{filter_name.all()[0]} filter_name으로 찾은 뒤에 출력했습니다.")

## UPDATE ##
update_member = AOA.query.filter_by(birth = 1994).all()[0]
update_member.birth = 1993
db.session.add(update_member)
db.session.commit()
all_members = AOA.query.all()
print(f"{all_members} 두 번째로 모든 멤버를 읽어왔습니다.")


## DELETE ##
delete_member = AOA.query.get(2)
db.session.delete(delete_member)
db.session.commit()

all_members = AOA.query.all()
print(f"{all_members} 세 번째로 모든 멤버를 읽어왔습니다.")