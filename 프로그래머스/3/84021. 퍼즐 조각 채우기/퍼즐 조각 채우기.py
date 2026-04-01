from collections import deque

def solution(game_board, table):
    n = len(game_board)
    # extract 0 from game_board, 1 from table
    # allign the pieces (0,0)
    # rotate func
    # 게임보드 빈칸마다 퍼즐 조각 90도씩 돌리면서 맞춰보기
    def extract_pieces(board, target):
        pieces = []
        visited = [[False] * n for _ in range(n)]
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        
        for r in range(n):
            for c in range(n):
                if board[r][c] == target and not visited[r][c]:
                    piece = []
                    q = deque([(r, c)])
                    visited[r][c] = True
                    while q:
                        curr_r, curr_c = q.popleft()
                        piece.append((curr_r, curr_c))
                        for i in range(4):
                            nr, nc = curr_r + dr[i], curr_c + dc[i]
                            if 0<= nr < n and 0<=nc<n and not visited[nr][nc] and board[nr][nc] == target:
                                q.append((nr, nc))
                                visited[nr][nc] = True
                    pieces.append(normalize(piece))
        return pieces
                    
    def normalize(piece):
        min_r = min(p[0] for p in piece)
        min_c = min(p[1] for p in piece)
        return sorted([(p[0]-min_r, p[1]-min_c) for p in piece])
    
    def rotate(piece):
        return normalize([(p[1], -p[0]) for p in piece])
    
    blank_spaces = extract_pieces(game_board, 0)
    puzzle_pieces = extract_pieces(table, 1)
    answer = 0
    used_puzzle = [False] * len(puzzle_pieces)
    
    for blank in blank_spaces:
        matched = False
        for i, puzzle in enumerate(puzzle_pieces):
            if len(blank) == len(puzzle) and not used_puzzle[i]:
                curr_puzzle = puzzle
                for _ in range(4):
                    if blank == curr_puzzle:
                        answer += len(blank)
                        matched = True
                        used_puzzle[i] = True
                        break
                    curr_puzzle = rotate(curr_puzzle)
                if matched: break
                
    return answer
        