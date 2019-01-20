import logging
import sys

from Game import Game
import Space


logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main():

    # Initialize game
    g = Game()

    # Play as long as more than 1 player remains in game
    while g.players_remaining > 1:

        # Update game round
        g.updateRound()

        # Define player of turn
        for turn_player in g.players:

            # Initialize dice
            g.passDice()

            # Continue until turn ends
            while True:

                # Skip turn if player is bankrupt
                if turn_player.bankrupt:
                    break

                # Roll the dice
                g.dice.roll()

                # If third double, then go to jail and end turn
                if g.dice.doubleCounter == 3:
                    print("3x double roll. It's a problem. Go to cold storage.")
                    turn_player.go_to_jail()
                    break

                # Continue if player is in jail
                if turn_player.jail_turns > 0:
                    stay_in_jail = turn_player.choose_jail_strategy(rolled_double=g.dice.double)
                    if stay_in_jail:
                        break

                # Move player
                turn_player.move(g.dice.sum)

                # Define current board space
                space = g.board[turn_player.pos]

                # Pay taxes
                if isinstance(space, Space.Tax):
                    turn_player.pay(Space.tax, g.bank)

                # Choose property strategy
                elif isinstance(space, Space.Property):
                    turn_player.visit_property(space)

                # If a player owns monopolies
                if turn_player.owns_monopoly:
                    turn_player.buy_building()

                # End turn
                break

        if g.round == 10:
            break

if __name__ == '__main__':
    main()
