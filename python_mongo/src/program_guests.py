#!/usr/bin/env python3
from dateutil.parser import parser
import datetime
from infrastructure.switchlang import switch
import program_hosts as hosts
import infrastructure.state as state
from services import data_service as svc


def run():
    print(" ****************** Welcome guest **************** ")
    print()

    show_commands()

    while True:
        action = hosts.get_action()

        with switch(action) as s:
            s.case("c", hosts.create_account)
            s.case("l", hosts.log_into_account)

            s.case("a", add_a_snake)
            s.case("y", view_your_snakes)
            s.case("b", book_a_cage)
            s.case("v", view_bookings)
            s.case("m", lambda: "change_mode")

            s.case("?", show_commands)
            s.case("", lambda: None)
            s.case(["x", "bye", "exit", "exit()"], hosts.exit_app)

            s.default(hosts.unknown_command)

        state.reload_account()

        if action:
            print()

        if s.result == "change_mode":
            return


def show_commands():
    print("What action would you like to take:")
    print("[C]reate an account")
    print("[L]ogin to your account")
    print("[B]ook a cage")
    print("[A]dd a snake")
    print("View [y]our snakes")
    print("[V]iew your bookings")
    print("[M]ain menu")
    print("e[X]it app")
    print("[?] Help (this info)")
    print()


def add_a_snake():
    print(" ****************** Add a snake **************** ")
    if not state.active_account:
        hosts.error_msg("You must be logged in first to add a snake")
        return

    name = input("What is your snake's name? ")
    if not name:
        hosts.error_msg("Cancelled")
        return

    length = float(input("How long is your snake (in meters)? "))
    species = input("Species? ")
    is_venomous = input("Is your snake venomous? [y, n] ").lower().startswith("y")

    snake = svc.add_snake(state.active_account, name, length, species, is_venomous)
    state.reload_account()
    hosts.success_msg(f"Successfully created {snake.name} with id {snake.id} 🐍")

    print(" -------- NOT IMPLEMENTED -------- ")


def view_your_snakes():
    print(" ****************** Your snakes **************** ")

    if not state.active_account:
        hosts.error_msg("You must login first to view your snakes")
        return

    snakes = svc.get_snakes_for_user(state.active_account.id)
    print(f"You have {len(snakes)} snakes")
    for s in snakes:
        print(
            "* {} is a {} that is {}m long and is {}venomous".format(
                s.name, s.species, s.length, "" if s.is_venomous else "not "
            )
        )


def book_a_cage():
    print(" ****************** Book a cage **************** ")
    if not state.active_account:
        hosts.error_msg("You must login first to book a cage")
        return

    snakes = svc.get_snakes_for_user(state.active_account.id)
    if not snakes:
        hosts.error_msg("You must first [a]dd a snake before you can book a cage")
        return
    print("Lets start by finding available cages")

    checkin = parser.parse(input("Check-in date [yyyy-mm-dd]: "))
    if not checkin:
        hosts.error_msg("Cancelled")
        return

    checkout = parser.parse(input("Check-out date [yyyy-mm-dd]: "))
    if checkin >= checkout:
        hosts.error_msg("Check-in must be before check-out")
        return
    print()
    for idx, s in enumerate(snakes):
        print(
            "{}. {} (length: {}m, venomous: {})".format(
                idx + 1, s.name, s.length, "yes" if s.is_venomous else "no"
            )
        )
    snake = snakes[int(input("Which snake do you want to book (number) ")) - 1]
    cages = svc.get_available_cages(checkin, checkout, snake)
    print(f"There are {len(cages)} available during that time")
    for idx, c in enumerate(cages):
        print(
            "{}. {} rated {} and {} sq meters  carpeted: {}, has toys: {}.".format(
                idx + 1,
                c.name,
                # c.average_rating,
                c.sq_meters,
                "yes" if c.is_carpeted else "no",
                "yes" if c.has_toys else "no",
            )
        )

    if not cages:
        hosts.error_msg("Sorry, no cages available for that date.")
        return

    cage = cages[int(input("Which cage do you want to book (number): ")) - 1]
    svc.book_cage(state.active_account, snake, cage, checkin, checkout)
    hosts.success_msg(
        f"Successfully booked {cage.name} for {snake.name} from {checkin} till {checkout}"
    )


def view_bookings():
    print(" ****************** Your bookings **************** ")
    if not state.active_account:
        hosts.error_msg("You must login first to view your bookings")
        return

    snakes = {s.id: s for s in svc.get_snakes_for_user(state.active_account.id)}
    bookings = svc.get_bookings_for_user(state.active_account)

    print(f"You have {len(bookings)}")
    for b in bookings:
        print(
            "* Snake: {} is booked at {} from {} for {} days".format(
                snakes.get(b.guest_snake_id).name,
                b.cage.name,
                datetime.date(
                    b.check_in_date.year, b.check_in_date.month, b.check_in_date.day
                ),
                (b.check_out_date - b.check_in_date).days,
            )
        )
