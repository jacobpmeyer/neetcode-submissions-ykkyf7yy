class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # students = [1,1,1], sandwiches = [0,1,1]
        while sandwiches:
            loop = True
            for i in range(len(sandwiches)):
                if sandwiches[0] == students[0]:
                    students = students[1:]
                    sandwiches = sandwiches[1:]
                    loop = False
                else:
                    students = students[1:] + students[:1]
            if loop:
                break
        return len(sandwiches)