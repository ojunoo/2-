import random

def board_result(board, player):  # 컴퓨터는 보드 입력이 아니니까 제외
    if player < 1 or player > 9:
        print("1부터 9까지 중에 입력하세요")  # 오류
        return False  # 잘못된 입력 반환
    
    row = (player - 1) // 3
    col = (player - 1) % 3

    if board[row][col] != " ":  # 공백(이미 선택한 자리)이 아니면 False
        print("잘못된 입력입니다")
        return False
    
    board[row][col] = "O"  # 플레이어의 자리

    return True


def print_board(board):  # 보드 출력
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, symbol):  # 승리 체크는 이제 symbol로
    # 가로(행) 확인
    for row in board:
        if all(cell == symbol for cell in row):
            return True  # 같은 기호가 3개 연속이면 승리

    # 세로(열) 확인
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    # 대각선 확인 (왼쪽 위 → 오른쪽 아래)
    if all(board[i][i] == symbol for i in range(3)):
        return True

    # 대각선 확인 (오른쪽 위 → 왼쪽 아래)
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False  # 승리 조건이 없으면 False 반환


def main():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],  # 보드 생성 3x3
        [" ", " ", " "]
    ]
    
    while any(" " in row for row in board):
        try:
            player = int(input("원하는 위치 (1~9)를 입력하세요: "))        
        except ValueError:  # 숫자가 아닌 입력 방지
            print("숫자를 입력하세요.")
            continue
        if board_result(board, player):
            print_board(board)

            # 플레이어가 이겼는지 체크
            if check_win(board, "O"):
                print("🎉 플레이어 승리!")
                break  # 게임 종료

            # 컴퓨터 턴
            while True:
                computer = random.randint(1, 9)
                row = (computer - 1) // 3
                col = (computer - 1) % 3
                if board[row][col] == " ":
                    board[row][col] = "X"  # 컴퓨터의 자리
                    break

            print_board(board)

            # 컴퓨터가 이겼는지 체크
            if check_win(board, "X"):
                print("🤖 컴퓨터 승리!")
                break  # 게임 종료

    print("게임 종료!")


main()
