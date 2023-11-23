from lib.University import *
from unittest.mock import Mock

def test_admit_students_unit_when_student_studies_right_subject(): 
    university = University()
    fake_student = Mock()
    fake_student.get_subject.return_value = "English"
    university.admit_student(fake_student)
    fake_student.accepted_in_uni.assert_called()
    assert university.students_list == [fake_student]

def test_update_student_subject_on_list(): 
    mock_student = Mock()
    subject = "French"
    mock_student.get_subject.return_value = "English"

    university = University()
    university.admit_student(mock_student)
    university.update_student_subject(mock_student, subject)
    mock_student.update_subject.assert_called()

