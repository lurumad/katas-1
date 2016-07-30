package com.katas;

import com.katas.hands.HandCalculator;
import com.katas.hands.HandType;
import com.katas.hands.TopUserHand;

import java.util.Arrays;
import java.util.List;

public class PokerGame {

    private final HandCalculator handCalculator;
    private final Player whitePlayer;
    private final Player blackPlayer;

    public PokerGame(HandCalculator handCalculator, Player whitePlayer, Player blackPlayer) {

        this.handCalculator = handCalculator;
        this.whitePlayer = whitePlayer;
        this.blackPlayer = blackPlayer;
    }

    public String showDown() {

        TopUserHand handTypeForWhitePlayer = this.handCalculator.calculateTopHand(whitePlayer.getPokerHand());
        TopUserHand handTypeForBlackPlayer = this.handCalculator.calculateTopHand(blackPlayer.getPokerHand());

        if (handTypeForWhitePlayer.getHandType().equals(handTypeForBlackPlayer.getHandType())) {
            if (handTypeForWhitePlayer.getMaxCardValue().getValue() > handTypeForBlackPlayer.getMaxCardValue().getValue()) {
                return this.createResultMessage(whitePlayer, handTypeForWhitePlayer);
            }
            return this.createResultMessage(blackPlayer, handTypeForBlackPlayer);
        }
        return null;
    }

    private String createResultMessage(Player player, TopUserHand topUserHand) {
        return whitePlayer.getPlayerName() + " wins. - with high card: " + topUserHand.getMaxCardValue().getDescription();
    }

}
