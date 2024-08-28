#!/usr/bin/env python3

from typing import List
from data.cages import Cage
from data.owners import Owner


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
