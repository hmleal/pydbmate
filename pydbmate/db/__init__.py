from sqlalchemy import create_engine
from pydbmate import settings

# from pydbmate.settings import DB_URI


engine = create_engine(settings.DATABASE_URL, echo=True)

# Base.metadata.create_all(engine)

# from sqlalchemy.orm import sessionmaker

# Session = sessionmaker(bind=engine)
# session = Session()

# first = Migration(name="Henrique Leal")

# session.add(session)

# session.commit()
