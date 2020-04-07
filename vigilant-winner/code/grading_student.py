

"""
Description:
Student 1 received a 73, and the next multiple of 5 from 73 is 75. Since 75 - 73 < 3, the student's grade is rounded to 75.
student 2 received a 82, next multiple of 5 is 85. Since 85 - 82 =< 3, the student's grade is rounded to 82'
"""

# complexity: runtime O(n) | space O(1)
def grading_students(students_grades):
    for grade in students_grades:
        if grade < 38:
            yield grade
        else:
            i = 0
            while grade % 5 != 0:
                grade += 1
                i += 1
            if i < 3:
                yield grade
            else:
                yield grade - i


# unittest
import unittest

input = """
27
89
56
47
38
12
98
72
85
76
72
56
23
77
25
49
4
52
71
43
11
2
44
10
20
3
90
64
48
31
56
51
70
91
14
25
61
41
0
"""

expected_output = """
27
90
56
47
40
12
100
72
85
76
72
56
23
77
25
50
4
52
71
45
11
2
45
10
20
3
90
65
50
31
56
51
70
91
14
25
61
41
0
"""


class TestGradingStudent(unittest.TestCase):
    def setUp(self):
        self.input = map(int, input.split())
        self.expected_output = map(int, expected_output.split())

    def test_grading_student(self):
        actual_output = grading_students(self.input)
        self.assertEqual(list(self.expected_output), list(actual_output))


if __name__ == '__main__':
    unittest.main()
