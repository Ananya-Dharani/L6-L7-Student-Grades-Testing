import pytest
from hypothesis import given, strategies as st
from student_grades import average_marks, parse_srn, short_name


@given(st.lists(st.integers(min_value=-1000, max_value=1000), min_size=1, max_size=20))
def test_average_marks_property(marks):
    result = average_marks(",".join(str(mark) for mark in marks))
    assert isinstance(result, float)
    assert result == round(sum(marks) / len(marks), 2)


@given(st.text() | st.none())
def test_average_marks_no_crash(value):
    try:
        average_marks(value)
    except (TypeError, ValueError):
        pass


@given(
    st.builds(
        lambda campus, year, dept, serial: (
            f"{campus}UG{year:02d}{dept}{serial}"
        ),
        campus=st.just("PES1"),
        year=st.integers(min_value=0, max_value=99),
        dept=st.just("CS"),
        serial=st.integers(min_value=0, max_value=999).map(str),
    )
)
def test_parse_srn_valid_format(srn):
    campus, year, department = parse_srn(srn)
    assert campus == "PES1"
    assert 0 <= year <= 99
    assert department == "CS"


@given(st.text() | st.none())
def test_parse_srn_no_crash(value):
    try:
        parse_srn(value)
    except (TypeError, ValueError):
        pass


@given(
    st.tuples(
        st.from_regex(r"[A-Za-z][A-Za-z'-]*", fullmatch=True),
        st.from_regex(r"[A-Za-z][A-Za-z'-]*", fullmatch=True),
    )
)
def test_short_name_property(names):
    first, last = names
    assert short_name(f"{first} {last}") == f"{first[0].upper()}. {last.capitalize()}"


@given(st.text() | st.none())
def test_short_name_no_crash(value):
    try:
        short_name(value)
    except (TypeError, ValueError):
        pass


@pytest.mark.parametrize(
    ("marks_csv", "error"),
    [
        ("", ValueError),
        ("   ", ValueError),
        ("78,,92", ValueError),
        ("78,nope,92", ValueError),
    ],
)
def test_average_marks_rejects_malformed_csv(marks_csv, error):
    with pytest.raises(error):
        average_marks(marks_csv)


@pytest.mark.parametrize("srn", ["", "PES1", "PES1UGXXCS123"])
def test_parse_srn_rejects_invalid_input(srn):
    with pytest.raises(ValueError):
        parse_srn(srn)


@pytest.mark.parametrize("full_name", ["", "   ", "ravi"])
def test_short_name_rejects_missing_name(full_name):
    with pytest.raises(ValueError):
        short_name(full_name)
