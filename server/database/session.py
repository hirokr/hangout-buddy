from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from core.config import settings 
from typing import AsyncGenerator

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.SQLALCHEMY_ECHO,  # Optional: logs SQL queries (disable in production)
    pool_pre_ping=True,
    pool_recycle=3600,  
    future=True     # Use SQLAlchemy 2.0 style
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,  # Prevents automatic expiration after commit
    autoflush=True,         # Auto-flush before queries
    autocommit=False        # Explicit transaction control
)

# ✅ Proper dependency with correct type hints and error handling
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get async database session.
    Use with FastAPI Depends() or similar DI systems.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

# ✅ Alternative: Context manager for manual session handling
class DatabaseManager:
    """Context manager for database sessions outside of dependency injection"""
    
    def __init__(self):
        self.session: AsyncSession | None = None
    
    async def __aenter__(self) -> AsyncSession:
        self.session = AsyncSessionLocal()
        return self.session
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            if exc_type:
                await self.session.rollback()
            await self.session.close()

# ✅ Cleanup function for application shutdown
async def close_db():
    """Call this during application shutdown"""
    await engine.dispose()

# Example usage:
# 
# FastAPI dependency injection:
# @app.get("/users/")
# async def get_users(db: AsyncSession = Depends(get_db)):
#     result = await db.execute(select(User))
#     return result.scalars().all()
#
# Manual context manager:
# async def some_function():
#     async with DatabaseManager() as db:
#         result = await db.execute(select(User))
#         return result.scalars().all()