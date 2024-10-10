from sqlmodel import SQLModel, create_engine

# Supabase credentials from your dashboard
POSTGRES_USER = "joeg2984"
POSTGRES_PASSWORD = "dysdi4-xebDud-zigsaq"
POSTGRES_HOST = "aws-0-us-east-1.pooler.supabase.com"
POSTGRES_DB = "postgres"
DATABASE_URL = f"postgresql://postgres.llrfqpkbojsczfpiivqz:dysdi4-xebDud-zigsaq@aws-0-us-east-1.pooler.supabase.com:6543/postgres"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
