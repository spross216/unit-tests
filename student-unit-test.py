import unittest
import Student
import testData

class TestAssignment(unittest.TestCase):
        
    def test_getPercentage(self):   # unit test for Assignment.getpercentage
        testAssignment = [0.8, 1, 0.86, 0.9366666666666666, 0.93, 0.93, 0.97, 0.93]
        
        assignments = []
        for assignmentDict in testData.ASSIGNMENTS:
            assignments.append(Student.Assignment(**assignmentDict))
        
        for i, assignment in enumerate(assignments):
            self.assertEqual(assignment.getPercentage(), testAssignment[i])


class TestStudent(unittest.TestCase):

    def test_eventsFunctions(self):   
        events = []
        for eventDict in testData.EVENTS:
            events.append(Student.Event(**eventDict))
            student = Student.Student(name='Matthew Pogue', ID='h735f787', events=events)
            student.addEvent
        self.assertEqual(len(events), 9) # unit test for Student.addEvent
        self.assertEqual(student.countEventOfType(eventType='meeting'), 2) # unit test for Student.countMeetings

    def test_grades(self):
        assignments = []
        for assignmentDict in testData.ASSIGNMENTS:
            assignments.append(Student.Assignment(**assignmentDict))
            student = Student.Student(name='Matthew Pogue', ID='h735f787', assignments=assignments)
            student.addAssignment
        self.assertEqual(student.getGrade(), 0.92416666666666666666666666666667) # unit test for Student.getGrade
        self.assertEqual(student.getLetterGrade(), 'A') # unit test for Student.getLetterGrade
   
            
if __name__ == "__main__":
    unittest.main()