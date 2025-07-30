from Departments.tests.base import BaseDepartmentTest

class TestDepartmentModel(BaseDepartmentTest):

    def test_01_department_name(self):
        self.assertEqual(self.department.name,'Test Department')
    
    def test_02_short_name(self):
        self.assertEqual(self.department.short_name,'TD')
    
    def test_03_str_representation(self):
        expected = "Test Department (Test University)"
        self.assertEqual(str(self.department), expected)

    def test_04_unique_department_name(self):
        with self.assertRaises(Exception):
            self.Department.objects.create(
                name='Test Department',  # duplicate
                short_name='ABC',
                university=self.university
            )
