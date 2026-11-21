import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


@pytest.mark.parametrize(
    ("marks", "expected"),
    [
        (100, "S"),
        (90, "S"),
        (89, "A"),
        (80, "A"),
        (79, "B"),
        (70, "B"),
        (69, "C"),
        (60, "C"),
        (59, "D"),
        (50, "D"),
        (49, "E"),
        (40, "E"),
        (39, "F"),
        (0, "F"),
    ],
)
def test_letter_grade_boundaries(marks, expected):
    assert letter_grade(marks) == expected


@pytest.mark.parametrize("marks", [-1, 101])
def test_letter_grade_rejects_out_of_range(marks):
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(marks)


@pytest.mark.parametrize(
    ("internal", "external", "has_project", "expected"),
    [
        (0, 0, False, 0),
        (40, 60, False, 100),
        (20, 30, False, 50),
        (20, 30, True, 55),
        (40, 60, True, 100),
    ],
)
def test_final_marks(internal, external, has_project, expected):
    assert final_marks(internal, external, has_project) == expected


@pytest.mark.parametrize(
    ("internal", "external"),
    [(41, 60), (40, 61)],
)
def test_final_marks_rejects_out_of_range(internal, external):
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(internal, external, False)


@pytest.mark.parametrize(
    ("attendance", "fees_paid", "has_medical", "expected"),
    [
        (100, True, False, "eligible"),
        (75, True, False, "eligible"),
        (74, True, True, "eligible"),
        (65, True, True, "eligible"),
        (64, True, True, "detained"),
        (65, True, False, "detained"),
        (0, True, False, "detained"),
        (100, False, True, "blocked"),
        (0, False, False, "blocked"),
    ],
)
def test_exam_eligibility(attendance, fees_paid, has_medical, expected):
    assert exam_eligibility(attendance, fees_paid, has_medical) == expected
