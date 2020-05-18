class GraphNode:
    def __init__(self, val):
        self.val = val
        self.prerequisites = set()
        self.prerequisite_for = set()
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = [
            GraphNode(n)
            for n in range(numCourses)
        ] # can be an array
        
        for course, prereq in prerequisites:
            nodes[course].prerequisites.add(prereq)
            nodes[prereq].prerequisite_for.add(course)
            
        stack = [
            node
            for node in nodes
            if not node.prerequisites
        ]
        
        while stack:
            node = stack.pop()
            if node.prerequisites:
                continue
            
            for course in node.prerequisite_for:
                course_node = nodes[course]
                course_node.prerequisites.remove(node.val)
                stack.append(course_node)
            
            node.prerequisite_for = set()
            
        remaining_courses = [
            node
            for node in nodes
            if node.prerequisites
        ]
        
        return len(remaining_courses) == 0
            
            
