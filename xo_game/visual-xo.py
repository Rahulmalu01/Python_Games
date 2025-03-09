import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
xop=[" "] * 9
player1=input("Enter the player1 name : ")
player2=input("Enter the player2 name : ")
def board():
    board = np.zeros((3, 3))
    plt.imshow(board, vmin=0, vmax=1)
    plt.grid(color = "white")
    plt.tick_params(length=0)
    plt.xticks([0.5, 1.5])
    plt.yticks([0.5, 1.5])
    for i in range(1,10):
        fig.canvas.mpl_connect('button_press_event', on_click)
        plt.show()
        if i==9:print("The match is draw");exit()
def check():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6] 
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if xop[a] == xop[b] == xop[c] and xop[a] != " ":
            winner = player1 if xop[a] == "X" else player2
            print(f"\n🎉 {winner} wins the game! 🎉")
            plt.close(fig)
            exit()
    if " " not in xop:
        print("\n🤝 The match is a draw! 🤝")
        plt.close(fig)
        exit()
    return
def on_click(event):
    x, y = int(round(event.xdata)), int(round(event.ydata))
    pos = 3 * y + x
    if xop[pos] == " ":
        player_symbol = "X" if xop.count("X") <= xop.count("O") else "O"
        xop[pos] = player_symbol
        if player_symbol == "X":
            ax.plot([x-0.4, x+0.4], [y-0.4, y+0.4], color='red', linewidth=3)
            ax.plot([x+0.4, x-0.4], [y-0.4, y+0.4], color='red', linewidth=3)
        else:
            ax.add_patch(plt.Circle((x, y), 0.35, color='blue', fill=False, linewidth=3))
        plt.draw()
        if check():
            return
board()
