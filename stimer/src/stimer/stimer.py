import datetime
import enum

from stimer.exceptions import ArgumentError

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class LogEntryType(enum.Enum):
    START = "start"
    END = "end"

    @classmethod
    def from_str(cls, s: str) -> "LogEntryType":
        try:
            return cls(s)
        except ValueError:
            raise ValueError(f"Invalid LogEntryType: '{s}'") from None


def dt_now() -> datetime.datetime:
    return datetime.datetime.now()


def dt_now_str() -> str:
    return dt_now().strftime(DATETIME_FORMAT)


def last_line(path: str) -> str:
    try:
        with open(path) as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        return ""
    return lines[-1] if lines else ""


def last_line_type(log_path: str) -> "LogEntryType | None":
    line = last_line(log_path)
    if not line:
        return None
    try:
        return LogEntryType.from_str(line.split(",")[0])
    except ValueError:
        return None


def start_end(log_path: str, kind: LogEntryType) -> None:
    last_type = last_line_type(log_path)
    if last_type is kind:
        raise ArgumentError(f"Forbidden: previous entry was also {kind.value}.")

    log_line = f"{kind.value},{dt_now_str()}\n"
    with open(log_path, "a") as f:
        f.write(log_line)


def start(log_path: str) -> None:
    start_end(log_path, LogEntryType.START)


def end(log_path: str) -> None:
    start_end(log_path, LogEntryType.END)


def main(log_path: str, starting: bool) -> None:
    if starting:
        start(log_path)
    else:
        end(log_path)
