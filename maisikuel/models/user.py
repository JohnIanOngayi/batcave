#!/usr/bin/python3

from sqlalchemy.orm import Relationship
from models.base import TimeStampedModel
from models.base import Model
from sqlalchemy import Column, ForeignKey, Integer, String


class User(TimeStampedModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(length=80), nullable=False)
    last_name = Column(String(length=80), nullable=False)
    email = Column(String(length=320), nullable=False, unique=True)
    preference = Relationship("Preference", back_populates="user", uselist=False, passive_deletes=True)
    addresses = Relationship("Address", back_populates="user", passive_deletes=True)
    roles = Relationship("Role", secondary="user_roles", back_populates="users", passive_deletes=True)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}, name: {self.first_name} {self.last_name}"


class Preference(TimeStampedModel):
    __tablename__ = "preferences"
    id = Column(Integer, primary_key=True, autoincrement=True)
    language = Column(String(length=80), nullable=False)
    currency = Column(String(length=3), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True, unique=True)
    user = Relationship("User", back_populates="preference")


class Address(TimeStampedModel):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    road_name = Column(String, nullable=False)
    postcode = Column(String, nullable=False)
    city = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    user = Relationship("User", back_populates="addresses")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}, name: {self.city}"


class Role(Model):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=80), nullable=False)
    slug = Column(String(length=80), nullable=False, unique=True)
    users = Relationship("User", secondary="user_roles", back_populates="roles", passive_deletes=True)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}, name: {self.name}"

class UserRole(TimeStampedModel):
    __tablename__ = "user_roles"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)
