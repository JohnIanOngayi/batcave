#!/usr/bin/python3

from sqlalchemy import create_engine, ForeignKey, String, Integer, Column, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

if __name__ == "__main__":

    Base = declarative_base()

    def generate_uuid():
        return str(uuid.uuid4())

    class Users(Base):
        __tablename__ = "users"
        userID = Column("userID", String, primary_key=True, default=generate_uuid)
        firstName = Column("firstName", String)
        lastName = Column("lastName", String)
        profileName = Column("profileName", String)
        email = Column("email", String, unique=True)

        def __init__(self, firstName, lastName, profileName, email) -> None:
            self.firstName = firstName
            self.lastName = lastName
            self.profileName = profileName
            self.email = email


    class Posts(Base):
        __tablename__ = "posts"
        postID = Column("postID", String, primary_key=True, default=generate_uuid)
        userID = Column("userID", String, ForeignKey("users.userID"))
        postContent = Column("postContent", String)

        def __init__(self, userID, postContent) -> None:
            self.userID = userID
            self.postContent = postContent


    class Likes(Base):
        __tablename__ = "likes"
        likeID = Column("likeID", String, primary_key=True, default=generate_uuid)
        postID = Column("postID", String, ForeignKey("posts.postID"))
        userID = Column("userID", String, ForeignKey("users.userID"))

        def __init__(self, postID, userID) -> None:
            self.postID = postID
            self.userID = userID

    def addUser(session, firstName, lastName, profileName, email):
        exist = session.query(Users).filter(Users.email == email).all()
        if (len(exist) > 0):
            print("Account with email address already exists")
        else:
            user = Users(firstName, lastName, profileName, email)
            session.add(user)
            session.commit()

    def addPost(session, userID, postContent):
        user = session.query(Users).filter(Users.userID == userID).first()
        if user is None:
            print("User no exist")
            return
        post = Posts(userID, postContent)
        session.add(post)
        session.commit()

    def addLike(session, postID, userID):
        post = session.query(Posts).filter(Posts.postID == postID).first()
        user = session.query(Users).filter(Users.userID == userID).first()
        if post is None or user is None:
            print("No find post")
            return
        like = Likes(postID, userID)
        print("User {0} liked Post {1}".format(userID, postID))
        session.add(like)
        session.commit()

    def no_of_Likes(session, postID):
        post = session.query(Posts).filter(Posts.postID == postID).first()
        if post is None:
            print("No find post")
            return
        allLikes = session.query(Likes).filter(Likes.postID == postID).all()
        print("{0} likes on Post {1}".format(len(allLikes), postID))

    db = "sqlite:///socialDB.db"
    engine = create_engine(db, connect_args={'timeout': 10})#echo=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # userID = "71c63c6c-55f7-4ece-8ac3-0881bcec5d29"
    # allPosts = session.query(Posts).filter(Posts.userID == userID).all()
    # print([post.postContent for post in allPosts])
    # players = session.query(Users).order_by(Users.lastName)
    # for player in players:
    #     print(player.firstName, player.lastName, player.profileName)
    # mappeds = [Base._decl_class_registry.values()]
    # for _cls in mappeds:
    #     allPosts = session.query(_cls).all()
    #     for post in allPosts:
    #         print(post, post.userID)
    all_p = session.query(Player).all()
    print(all_p)
