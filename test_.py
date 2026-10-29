import pytest 
from schedule import SCHEDULE, get_subjects, hours_in_day, is_correct_types


@pytest.fixture
def schedule():
    return SCHEDULE

class TestHoursInDay:
    def test_hours_monday(self, schedule):
        assert hours_in_day(schedule, "понедельник") == 5.5

    def test_hours_tuesday(self, schedule):
        assert hours_in_day(schedule, "вторник") == 4

    def test_hours_sunday(self, schedule):
        assert hours_in_day(schedule, "воскресенье") == 1

class TestIsCorrectTypes:

    @pytest.mark.parametrize("day", [
        "понедельник", "вторник", "среда", "четверг", "пятница"
    ])
    def test_weekday_types(self, schedule, day):
        assert is_correct_types(schedule, day) is True

    def test_sunday_types(self, schedule):
        assert is_correct_types(schedule, "воскресенье") is True

    @pytest.mark.skip(reason="Суббота не подxодит под спецификацию ")
    def test_saturday_types_skip(self):
        pass
class TestSubjects:

    def test_subjects_monday_order(self, schedule):
        assert get_subjects(schedule, "понедельник") == [
            "Математика",
            "Программирование",
            "История"
        ]

    def test_subjects_tuesday(self, schedule):
        assert get_subjects(schedule, "вторник") == [
            "Физика"
        ]

    def test_subjects_sunday(self, schedule):
        assert get_subjects(schedule, "воскресенье") == [
            "Конференция",
        ]