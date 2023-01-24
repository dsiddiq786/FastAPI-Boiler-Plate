from .. import schemas,models
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    
    return blogs

def create(db: Session, blog):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id = 1)
    
    db.add(new_blog)
    
    db.commit()
    
    db.refresh(new_blog)
    
    return new_blog

def get_by_id(db: Session, id):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
    
    return blog

def destroy_by_id(db: Session, id):
    blog_details = db.query(models.Blog).filter(models.Blog.id==id)
    
    if not blog_details.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    blog_details.delete(synchronize_session=False)
    
    db.commit()
    
    return {"msg":f"Blog with {id} is deleted"}

def update_by_id(db: Session, id, blog):
    blog_details = db.query(models.Blog).filter(models.Blog.id==id)
    
    if not blog_details.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    blog_details.update({"title":blog.title, "body":blog.body},synchronize_session=False)
    
    db.commit()
    
    return {"data updated successfully"}