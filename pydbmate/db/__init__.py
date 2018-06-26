from sqlalchemy import create_engine

# from pydbmate.settings import DB_URI


engine = create_engine("sqlite:///db.sqlite3", echo=True)

# Base.metadata.create_all(engine)

# from sqlalchemy.orm import sessionmaker

# Session = sessionmaker(bind=engine)
# session = Session()

# first = Migration(name="Henrique Leal")

# session.add(session)

# session.commit()