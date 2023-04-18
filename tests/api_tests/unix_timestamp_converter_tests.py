import pytest
from assertpy import assert_that  # pyright: ignore[reportUnknownVariableType]
from requests_toolbelt.sessions import BaseUrlSession


class UnixTimeStampConverterTests:
    @pytest.mark.parametrize(
        "datetime_string, expected_unix_time",
        [
            ("2023-04-16 20:31:03", 1681669863),
            ("2038-01-19 4:14:07", 2147483647),
            ("1970-01-01 1:0:00", 0),
        ],
    )
    def test_can_convert_from_datetime_string_to_unix_timestamp(
        self, datetime_string: str, expected_unix_time: int, session: BaseUrlSession
    ) -> None:
        response = session.get(f"unix-timestamp-converter/?cached&s={datetime_string}").text
        utc_timestamp = self.__change_unix_timestamp_timezone_to_utc(response)
        assert_that(utc_timestamp).is_equal_to(expected_unix_time)

    @pytest.mark.parametrize(
        "unix_time, expected_datetime_string",
        [
            (1681612263, "2023-04-16 02:31:03"),
            (2147476447, "2038-01-19 01:14:07"),
            (0, "1970-01-01 12:00:00"),
        ],
    )
    def test_can_convert_from_unix_timestamp_to_datetime_string(
        self, unix_time: int, expected_datetime_string: str, session: BaseUrlSession
    ) -> None:
        response = session.get(f"unix-timestamp-converter/?cached&s={unix_time}").text
        assert_that(response.strip('"')).is_equal_to(expected_datetime_string)

    @pytest.mark.parametrize(
        "datetime",
        [
            ("2023-16-04 2:3:0"),
            ("203801-19 4:14:07"),
            ("1970-01-01 1:000"),
            ("2023-04-16T23:56:26+00:00"),
            (""),
            ("@"),
        ],
    )
    def test_cannot_convert_datetime(self, datetime: str, session: BaseUrlSession) -> None:
        response = session.get(f"unix-timestamp-converter/?cached&s={datetime}").text
        assert_that(response).is_equal_to("false")

    def __change_unix_timestamp_timezone_to_utc(self, timestamp: str) -> int:
        import time
        from datetime import datetime, timezone

        datetime_to_convert = datetime.fromtimestamp(float(timestamp), timezone.utc)
        utc_timestamp = time.mktime(datetime_to_convert.timetuple())

        return int(utc_timestamp)
