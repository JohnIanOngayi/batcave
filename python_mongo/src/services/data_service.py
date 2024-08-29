#!/usr/bin/env python3

from datetime import datetime, timedelta
from typing import List
import bson
from data import snakes
from data.bookings import Booking
from data.cages import Cage
from data.owners import Owner
from data.snakes import Snake
from infrastructure import state


def create_account(name: str, email: str) -> Owner:
    new_owner = Owner()
    new_owner.email = email
    new_owner.name = name

    new_owner.save()
    return new_owner


def find_account_by_email(email: str) -> Owner | None:
    owner = Owner.objects().filter(email=email).first()
    """
    When you have a single filter parameter
    the query can be condensed to as below:->
    """
    owner = Owner.objects(email=email).first()

    return owner


def register_cage(
    owner: Owner, name, allow_dangerous_snakes, has_toys, is_carpeted, sq_meters, price
) -> Cage:
    cage = Cage()
    cage.name = name
    cage.is_carpeted = is_carpeted
    cage.has_toys = has_toys
    cage.sq_meters = sq_meters
    cage.allow_dangerous_snakes = allow_dangerous_snakes
    cage.price = price

    cage.save()
    account = find_account_by_email(owner.email)
    account.cage_ids.append(cage.id)
    account.save()
    return cage


def find_cages_for_user(user: Owner) -> List[Cage | None]:
    query = Cage.objects(id__in=user.cage_ids)
    cages = list(query)

    return cages


def add_available_date(selected_cage: Cage, start_date, days):
    booking = Booking()
    booking.check_in_date = start_date
    booking.check_out_date = start_date + timedelta(days=days)

    cage = Cage.objects(id=selected_cage.id).first()
    cage.bookings.append(booking)
    cage.save()

    return cage


def add_snake(account, name, length, species, is_venomous) -> Snake:
    snake = Snake()
    snake.name = name
    snake.length = length
    snake.species = species
    snake.is_venomous = is_venomous
    snake.save()

    owner = find_account_by_email(account.email)
    owner.snake_ids.append(snake.id)
    owner.save()

    return snake


def get_snakes_for_user(user_id: bson.ObjectId) -> List[Snake]:
    owner = Owner.objects(id=user_id).first()
    snakes = Snake.objects(id__in=owner.snake_ids).all()

    return list(snakes)


def get_available_cages(
    checkin: datetime, checkout: datetime, snake: Snake
) -> List[Cage]:
    min_size = snake.length / 4
    query = (
        Cage.objects()
        .filter(sq_meters__gte=min_size)
        .filter(bookings__check_in_date__lte=checkin)
        .filter(bookings__check_out_date__gte=checkout)
    )

    if snake.is_venomous:
        query = query.filter(allow_dangerous_snakes=True)

    cages = query.order_by("price", "-sq_meters")

    final_cages = []
    for c in cages:
        for b in c.bookings:
            if (
                b.check_in_date <= checkin
                and b.check_out_date >= checkout
                and b.guest_snake_id is None
            ):
                final_cages.append(c)
    return final_cages


def book_cage(
    account: Owner, snake: Snake, cage: Cage, checkin: datetime, checkout: datetime
):
    booking: Booking | None = None
    for b in cage.bookings:
        if (
            b.check_in_date <= checkin
            and b.check_out_date >= checkout
            and b.guest_snake_id is None
        ):
            booking = b
            break
    if booking:
        booking.guest_snake_id = snake.id
        booking.guest_owner_id = account.id
        booking.booked_date = datetime.now()
        booking.check_in_date = checkin
        booking.check_out_date = checkout

        cage.save()


def get_bookings_for_user(email: str) -> List[Booking]:
    account = find_account_by_email(email)
    booked_cages = (
        Cage.objects()
        .filter(bookings__guest_owner_id=account.id)
        .only("bookings", "name")
    )

    def map_cage_to_booking(cage: Cage, booking: Booking) -> Booking:
        booking.cage = cage
        return booking

    bookings = [
        map_cage_to_booking(cage, booking)
        for cage in booked_cages
        for booking in cage.bookings
        if booking.guest_owner_id == account.id
    ]

    return bookings
