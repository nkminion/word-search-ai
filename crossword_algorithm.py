def find_words(crossword: list[list[str]], words: list[str]) -> list:

    coordinates = list()

    def recursive_search(position: tuple[int], search_dir: tuple[int], word: str, index: int):

        if search_dir == (0,0):
            for i in range(max(0, position[0] - 1), min(len(crossword) - 1, position[0] + 1) + 1):
                for j in range(max(0, position[1] - 1), min(len(crossword[0]) - 1, position[1] + 1) + 1):
                    #print(range(max(0, position[1] - 1), min(len(crossword) - 1, position[1] + 1) + 1), i, j, index)
                    if (i,j) != (position[0], position[1]) and crossword[i][j] == word[index]:
                        return recursive_search((i, j), (i-position[0], j-position[1]), word, index + 1)
        
        else:
            for i in range(index, len(word)):
                position = (position[0] + search_dir[0], position[1] + search_dir[1])
                if position[0] not in range(0, len(crossword)) or position[1] not in range(0, len(crossword[0])):
                    return 0
                if crossword[position[0]][position[1]] != word[i]:
                    return 0
                
            coordinates.append(((position[0] - (len(word)-1)*search_dir[0], position[1] - (len(word)-1)*search_dir[1]), (position[0], position[1])))
            return 1
        
    result = 0

    for word in words:
        letters = list(word)
        for i in range(len(crossword)):
            if result:
                result = 0
                break
            for j in range(len(crossword[i])):
                if crossword[i][j] == letters[0]:
                    result = recursive_search((i, j), (0, 0), word, 1)
                    if result:
                        break

    return coordinates