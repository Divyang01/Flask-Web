#from sqlalchemy import create_engine
from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+pymysql://root:@localhost/zometo",echo = True)
db = scoped_session(sessionmaker(bind=engine))

def main():
		zometo_user = db.execute(" SELECT zometo_user_id, zometo_user_name,mobile, email from zometo_user").fetchall()
		print(zometo_user)
		return zometo_user
		#for user in zometo_user:
		#	print(f"{user.zometo_user_id} -- {user.zometo_user_name} -- {user.mobile} -- {user.email}")
if __name__ == '__main__':
	main()