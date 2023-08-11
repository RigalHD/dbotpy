# from sqlalchemy import create_engine, Column, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

# class ButtonClick(Base):
#     __tablename__ = 'button_clicks'

#     message_id = Column(String, primary_key=True)
#     user_id = Column(String)

# engine = create_engine('sqlite:///button_clicks.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()