from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = "mysql+asyncmy://root:root@127.0.0.1:3306/kinit"

# 创建sqlalchemy引擎，后续会在其他地方使用 engine
# connect_args 参数只用于 sqlite数据库中
# echo=True 将数据库操作打印出来
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)

# SessionLocal类的每一个实例都会是一个数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 稍后我们将继承这个类，来创建每个数据库模型或类（ORM 模型）
Base = declarative_base()