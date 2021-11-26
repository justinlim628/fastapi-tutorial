from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings


# orm
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]   
)
        
# connecting to routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Welcome to my API"}



#################################### SQL ##################################
# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts = cursor.fetchall()

#     return {"data": posts}


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_post(post: Post):
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", 
#                    (post.title, post.content, post.published))
#     new_post = cursor.fetchone()
#     conn.commit()

#     return {"data": new_post}


# @app.get("/posts/{id}")
# def get_post(id: int, response: Response):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
#     post = cursor.fetchone()
    
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} was not found')

#     return {"post detail": post}


# @app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     # find index in the array that has the required ID
#     # my_post.pop(index)
    
#     cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
#     deleted_posts = cursor.fetchone()
#     conn.commit()
    
#     if deleted_posts == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exist')
    
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put('/posts/{id}')
# def update_post(id: int, post: Post):
#     cursor.execute("""UPDATE posts SET title = %s, content=%s, published = %s WHERE id = %s RETURNING *""", 
#                    (post.title, post.content, post.published, str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()
    
#     if updated_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exist')
    
#     return {'data': updated_post}