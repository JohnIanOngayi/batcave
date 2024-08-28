#!/usr/bin/env python3
from colorama import Fore
from infrastructure.switchlang import switch
import infrastructure.state as state
import services.data_service as svc


def run():
    print(" ****************** Welcome host **************** ")
    print()

    show_commands()

    while True:
        action = get_action()

        with switch(action) as s:
            s.case("c", create_account)
            s.case("a", log_into_account)
            s.case("l", list_cages)
            s.case("r", register_cage)
            s.case("u", update_availability)
            s.case("v", view_bookings)
            s.case("m", lambda: "change_mode")
            s.case(["x", "bye", "exit", "exit()"], exit_app)
            s.case("?", show_commands)
            s.case("", lambda: None)
            s.default(unknown_command)

        if action:
            print()

        if s.result == "change_mode":
            return


def show_commands():
    print("What action would you like to take:")
    print("[C]reate an account")
    print("Login to your [a]ccount")
    print("[L]ist your cages")
    print("[R]egister a cage")
    print("[U]pdate cage availability")
    print("[V]iew your bookings")
    print("Change [M]ode (guest or host)")
    print("e[X]it app")
    print("[?] Help (this info)")
    print()


def create_account():
    print(" ****************** REGISTER **************** ")
    name = input("What is your name? ")
    email = input("What is your email? ").strip().lower()

    old_account = svc.find_account_by_email(email)
    if old_account is None:
        state.active_account = svc.create_account(name, email)
        success_msg(f"Created new a/c with id {state.active_account.id}")
    else:
        error_msg(f"Error: Account with email {email} already exists!")


def log_into_account():
    print(" ****************** LOGIN **************** ")

    email = input("What is your email? ").strip().lower()
    account = svc.find_account_by_email(email)

    if not account:
        error_msg(f"Sorry, no a/c with email {email}")
        return

    state.active_account = account
    success_msg("Successfully logged in🙂")


def register_cage():
    print(" ****************** REGISTER CAGE **************** ")

    if not state.active_account:
        error_msg("You must login first to register cage")
        return

    sq_meters = input("How many square meters in the cage? ")
    if not sq_meters:
        error_msg("Cancelled")
        return

    sq_meters = float(sq_meters)
    is_carpeted = input("Is it carpeted? [y, n] ").lower().startswith("y")
    has_toys = input("Has snake toys? [y, n] ").lower().startswith("y")
    allow_dangerous_snakes = (
        input("Can you host venomous snakes? [y, n] ").lower().startswith("y")
    )
    name = input("Give your cage a name: ")

    price = input("How much would you like to charge per day in dollars($)? ")
    if not price:
        error_msg("Cancelled")
        return

    price = float(price)

    new_cage = svc.register_cage(
        owner=state.active_account,
        name=name,
        allow_dangerous_snakes=allow_dangerous_snakes,
        has_toys=has_toys,
        is_carpeted=is_carpeted,
        sq_meters=sq_meters,
        price=price,
    )

    state.reload_account()
    success_msg(f"Registered new cage with id {new_cage.id}")


def list_cages(supress_header=False):
    if not supress_header:
        print(" ******************     Your cages     **************** ")

    if not state.active_account:
        error_msg("You must login first to list your registered cages")
        return

    cages = svc.find_cages_for_user(state.active_account)
    print(f"You have {len(cages)} cages")
    for idx, c in enumerate(cages):
        print(f"{idx+1}. {c.name} is {c.sq_meters} sq meters")
        for b in c.bookings:
            print(
                "     * Booking: {}, {} days, booked? {}".format(
                    b.check_in_date,
                    (b.checK_out_date - b.check_in_date).days,
                    "YES" if b.booked_date is not None else "no",
                )
            )


def update_availability():
    print(" ****************** Add available date **************** ")

    if not state.active_account:
        error_msg("You mst login first to view your cages")
        return

    list_cages(supress_header=True)

    cage_number = input("Select cage no.: ")
    if not cage_number.strip():
        error_msg("Cancelled")
        print()
        return

    cage_number = int(cage_number)

    cages = svc.find_cages_for_user(state.active_account)
    selected_cage = cages[cage_number - 1]

    start_date = parser.parse(input("Enter available date [yyyy-mm-dd]: "))
    days = int(input("How many days is this block of time? "))

    print(" -------- NOT IMPLEMENTED -------- ")


def view_bookings():
    print(" ****************** Your bookings **************** ")

    # TODO: Require an account
    # TODO: Get cages, and nested bookings as flat list
    # TODO: Print details for each

    print(" -------- NOT IMPLEMENTED -------- ")


def exit_app():
    print()
    print("bye")
    raise KeyboardInterrupt()


def get_action():
    text = "> "
    if state.active_account:
        text = f"{state.active_account.name}> "

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def unknown_command():
    print("Sorry we didn't understand that command.")


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)
