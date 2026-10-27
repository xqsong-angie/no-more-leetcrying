#20261023 AC

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.total=0
        n=len(employees)
        vis=set()
        def rec(employees,n,id):
            for i in range(n):
                if employees[i].id==id:
                    self.total+=employees[i].importance
                    vis.add(employees[i].id)
                    for s_id in employees[i].subordinates:
                        if s_id not in vis:
                            rec(employees,n,s_id)
        for i in range(n):
            if employees[i].id==id:
                self.total+=employees[i].importance
                vis.add(employees[i].id)
                for s_id in employees[i].subordinates:
                    if s_id not in vis:
                        rec(employees,n,s_id)
                        

        return self.total


        