class Parser:
    # static method for parsing board from .txt files
    # path is the file path of the txt file
    @staticmethod
    def parse(path:str) -> 'list[list]':
        board = []
        with open(path) as f:
            lines = f.readlines()
        count = 1
        row = []
        for i in lines[0]:
            if (i != "."): row.append(int(i))
            else: row.append(i)
            if count == 9:
                count = 0
                board.append(row)
                row = []
            count += 1
        return board




        

