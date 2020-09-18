class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        orgPos = [0, 0]
        curPos = [0, 0]
        mov = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        dirCount = 0
        vectors = []

        if 'L' not in instructions and 'R' not in instructions:
            return False

        if 'G' not in instructions:
            return True

        direction = [0, 1]
        for instruction in instructions:
            if instruction == 'G':
                curPos = [curPos[0] + direction[0], curPos[1] + direction[1]]
            elif instruction == 'L':
                dirCount += 1
                direction = mov[dirCount % 4]
            elif instruction == 'R':
                dirCount -= 1
                direction = mov[dirCount % 4]
        vector = [curPos[0] - orgPos[0], curPos[1] - orgPos[1]]

        if vector == [0, 0] or direction != [0, 1]:
            return True
        return False