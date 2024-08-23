class TicTacToe {
    constructor() {
        this.board = Array.from({ length: 3 }, () => Array(3).fill('-'));
        this.currentPlayer = 'X';
    }

    initializeBoard() {
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                this.board[i][j] = '-';
            }
        }
    }

    printBoard() {
        console.log("-------------");
        this.board.forEach(row => {
            console.log("| " + row.join(" | ") + " |");
        });
        console.log("-------------\n");
    }

    makeMove(row, col) {
        if (row >= 0 && row < 3 && col >= 0 && col < 3 && this.board[row][col] === '-') {
            this.board[row][col] = this.currentPlayer;
            return true;
        }
        return false;
    }

    checkWinner() {
        return this.checkRows() || this.checkColumns() || this.checkDiagonals();
    }

    checkRows() {
        for (let i = 0; i < 3; i++) {
            if (this.board[i][0] === this.currentPlayer && this.board[i][1] === this.currentPlayer && this.board[i][2] === this.currentPlayer) {
                return true;
            }
        }
        return false;
    }

    checkColumns() {
        for (let i = 0; i < 3; i++) {
            if (this.board[0][i] === this.currentPlayer && this.board[1][i] === this.currentPlayer && this.board[2][i] === this.currentPlayer) {
                return true;
            }
        }
        return false;
    }

    checkDiagonals() {
        return (
            (this.board[0][0] === this.currentPlayer && this.board[1][1] === this.currentPlayer && this.board[2][2] === this.currentPlayer) ||
            (this.board[0][2] === this.currentPlayer && this.board[1][1] === this.currentPlayer && this.board[2][0] === this.currentPlayer)
        );
    }

    isBoardFull() {
        return this.board.flat().every(cell => cell !== '-');
    }

    switchPlayer() {
        this.currentPlayer = this.currentPlayer === 'X' ? 'O' : 'X';
    }

    playGame() {
        console.log("\n----------------------");
        console.log("Welcome to Tic-Tac-Toe!");
        console.log("----------------------");
        const readline = require('readline');
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        const askMove = () => {
            this.printBoard();
            rl.question(`Player ${this.currentPlayer}, enter your move (row and column, separated by a space): `, answer => {
                const move = answer.trim().split(' ');
                if (move.length === 2 && move.every(v => !isNaN(v))) {
                    const [row, col] = move.map(Number);
                    if (this.makeMove(row, col)) {
                        if (this.checkWinner()) {
                            this.printBoard();
                            console.log(`Player ${this.currentPlayer} wins!`);
                            rl.close();
                        } else if (this.isBoardFull()) {
                            this.printBoard();
                            console.log("It's a draw!");
                            rl.close();
                        } else {
                            this.switchPlayer();
                            askMove();
                        }
                    } else {
                        console.log('This move is not valid');
                        askMove();
                    }
                } else {
                    console.log('Invalid input. Please enter row and column separated by a space.');
                    askMove();
                }
            });
        };

        askMove();
    }
}

const game = new TicTacToe();
game.playGame();
