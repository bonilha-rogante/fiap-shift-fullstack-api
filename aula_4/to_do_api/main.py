from sqlalchemy import String, create_engine, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(16))
    email: Mapped[str] = mapped_column(String(42), nullable=True)
    
engine = create_engine(
    "postgresql://docker-user:docker-password@localhost:5432/todos",
    echo=True,
)
    
Base.metadata.create_all(engine)

session = Session(engine)

user = User(name="lucas.silva")
session.add(user)
session.commit()

users = session.query(User).all()

for user in users:
    print(user.name)

# result = session.execute(text("SELECT VERSION();"))
# print(result.all())