import datetime
import enum

from exceptions import ArgumentError


class Type(enum.Enum):
    START = "start"
    END = "end"


def dt_now() -> datetime.datetime:
    dt = datetime.datetime.now()
    return dt


def dt_now_str() -> str:
    dt_str = dt_now().strftime("%Y-%m-%d %H:%M:%S")
    return dt_str


def last_line(path: str) -> str:
    try:
        with open(path) as f:
            line = f.read().splitlines()[-1]
    except FileNotFoundError:
        line = ""
    return line


def start_end(log_path: str, type_of_dt: str) -> None:
    if type_of_dt not in {Type.START, Type.END}:
        raise ArgumentError("Invalid type of datetime.")

    now = dt_now_str()
    buffer = f"{type_of_dt},{now}\n"

    line = last_line(log_path)
    last_line_type = line.split(',')[0]

    if type_of_dt == Type.START:
        if last_line_type == Type.START:
           raise ArgumentError("Forbidden.")
    elif type_of_dt == Type.END:
        if last_line_type == Type.END:
            raise ArgumentError("Forbidden.")


    with open(log_path, "a") as f:
        f.write(buffer)


def start(log_path: str) -> None:
    start_end(log_path, Type.START)


def end(log_path: str) -> None:
    start_end(log_path, Type.END)


def main(log_path: str, starting: bool) -> None:
    if starting:
        start(log_path)
    elif not starting:
        end(log_path)
    else:
        raise ValueError("Invalid starting value.")
        exit(1)
