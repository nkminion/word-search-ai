def find_words(crossword: list[list[str]], words: list[str]):

    coordinates = list()

    def recursive_search(position: tuple[int], search_dir: tuple[int], word: str, index: int):
        
        if search_dir == (0,0):
            for i in range(max(0, position[0] - 1), min(len(crossword[0]), position[0] + 1) + 1):
                for j in range(max(0, position[1] - 1), min(len(crossword), position[1] + 1) + 1):
                    if crossword[i][j] == word[index]:
                        recursive_search((i, j), (i-position[0], j-position[1]), word, index + 1)
        
        else:
            for i in range(index, len(word)):
                position = (position[0] + search_dir[0], position[1] + search_dir[1])
                if position[0] not in range(0, len(crossword)) or position[1] not in range(0, len(crossword[0])):
                    return
                if crossword[position[0]][position[1]] != word[i]:
                    return

            coordinates.append(((position[0] - i*search_dir[0], position[1] - i*search_dir[1]), (position[0], position[1])))   

    for word in words:
        letters = list(word)
        for i in range(len(crossword)):
            for j in range(len(crossword[i])):
                try:
                    if crossword[i][j] == letters[0]:
                        recursive_search((i, j), (0, 0), word, 1)
                except Exception:
                    print(i, j)

    print(coordinates)

crossword = [['G', 'A', 'R', 'D', 'E', 'N', 'Y', 'S', 'M', 'B', 'M', 'T', 'O', 'L', 'S'], ['N', 'I', 'A', 'R', 'M', 'E', 'L', 'E', 'S', 'E', 'E', 'R', 'W', 'O', 'U'], ['U', 'C', 'I', 'N', 'C', 'I', 'P', 'E', 'A', 'S', 'I', 'A', 'M', 'S', 'N'], ['L', 'M', 'L', 'I', 'N', 'O', 'I', 'T', 'A', 'C', 'A', 'V', 'R', 'P', 'S'], ['P', 'O', 'P', 'S', 'I', 'C', 'L', 'E', 'O', 'L', 'D', 'E', 'K', 'I', 'H'], ['U', 'I', 'P', 'E', 'C', 'A', 'M', 'P', 'I', 'O', 'O', 'L', 'F', 'C', 'I'], ['Y', 'T', 'N', 'S', 'R', 'E', 'T', 'L', 'M', 'D', 'N', 'T', 'R', 'E', 'N'], ['P', 'W', 'N', 'S', 'O', 'E', 'P', 'A', 'T', 'G', 'N', 'E', 'D', 'X', 'E'], ['A', 'U', 'G', 'R', 'I', 'A', 'D', 'Y', 'B', 'O', 'A', 'Y', 'A', 'T', 'E'], ['R', 'L', 'J', 'U', 'L', 'Y', 'G', 'R', 'S', 'A', 'S', 'O', 'U', 'P', 'A'], ['K', 'E', 'F', 'G', 'L', 'C', 'E', 'A', 'T', 'H', 'I', 'R', 'G', 'A', 'S'], ['B', 'A', 'L', 'Y', 'P', 'A', 'E', 'N', 'O', 'C', 'R', 'E', 'U', 'R', 'D'], ['S', 'H', 'O', 'R', 'T', 'S', 'O', 'O', 'H', 'A', 'E', 'H', 'S', 'H', 'R'], ['U', 'Y', 'P', 'E', 'M', 'N', 'O', 'S', 'A', 'E', 'S', 'S', 'T', 'D', 'E'], ['C', 'H', 'E', 'T', 'A', 'M', 'C', 'L', 'Y', 'B', 'G', 'M', 'R', 'E', 'S'], ['X', 'L', 'A', 'O', 'V', 'Z', 'R', 'C', 'O', 'J', 'B', 'R', 'I', 'N', 'S'], ['F', 'O', 'S', 'E', 'M', 'A', 'E', 'R', 'C', 'E', 'C', 'I', 'O', 'W', 'L'], ['B', 'L', 'O', 'S', 'S', 'U', 'M', 'M', 'E', 'R', 'W', 'B', 'M', 'O', 'S']]

find_words(crossword, ['GARD'])