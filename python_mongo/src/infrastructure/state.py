#!/usr/bin/env python3
from data.owners import Owner
from services import data_service as svc

active_account: Owner | None = None


def reload_account():
    global active_account
    if not active_account:
        return

    active_account = svc.find_account_by_email(active_account.email)
