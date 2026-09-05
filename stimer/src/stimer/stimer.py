import datetime
import os


def dt_now() -> datetime.datetime:
    return datetime.datetime.now()


def dt_now_str() -> str:
    return str(dt_now())


def start_end(type_of_dt: str) -> None:
    if type_of_dt not in {"START", "END"}:
        raise ArgumentError("Invalid type of datetime.")

    now = dt_now_str()
    buffer = f"{type_of_dt},{now}\n"

    with open("log.txt", "a") as f:
        f.write(buffer)


def start() -> None:
    print("Start.")
    start_end("START")
    print("Done start.")


def end() -> None:
    print("End.")
    start_end("END")
    print("Done end.")


def main(starting: bool) -> None:
    if starting:
        start()
    elif not starting:
        end()
    else:
        raise ValueError("Invalid starting value.")
        exit(1)
