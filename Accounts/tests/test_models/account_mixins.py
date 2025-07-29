from common.tests.models import UniversityTestBase
from Accounts.models import (
    StaffAccount,
    StudentAccount,
    TeacherAccount,
    AuthorityAccount
    )


class AccountTestMixin(UniversityTestBase):
    def create_student_account(self,account=None,batch=None):
        if account is None:
            self.user = self.create_user(email="teststudent@test.com")
            account = self.create_account(user=self.user)
        
        if batch is None:
            batch = self.create_batch()

        return StudentAccount.objects.create(
            account=account,
            batch = batch,
        )
    
    def create_teacher_account(self,account=None):
            
            return TeacherAccount.objects.create(
            account = account,
            department=self.department,
            Department_head=True
        )

