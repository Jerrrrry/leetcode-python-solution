// Just rewriting post and solution, for better readability

// You operate a marketplace for buying & selling used textbooks For a given textbook eg“TheoryofCryptography”
// there are people who want to buy this textbook and people who want to sell

// OfferstoBUY: [$100, $100, $99, $99, $97, $90]

// OfferstoSELL:[$109, $110, $110, $114, $115$, 119]

// A match occurs when two people agree on a price Some new offers do not match These offers should be added to the active set of offers

// For example, Tim offers to SELL at $150 This will not match No one is willing to buy at that price so we save the offer

// OfferstoSELL:: [$109, $110, $110, $114, $115, $119, $150]

// When matching we want to give the customer the “best price”

// Example matches: If Jane offers to BUY at $120

// she will match and buy a book for $109 (the lowest offer)

//Assuming sell is false then the price I got is for buy
public class Solution{

    public PriorityQueue<Integer> buy;
    public PriorityQueue<<Integer> sell;

    Solution(){
     buy = new PriorityQueue<Collections.reverseOrder()>();
     sell = new PriorityQueue<>();
    } 
    public int FindMatch(int price, boolean sell){
        int matchMoney=-1;  //default return -1
        if(sell){
            sell.add(price);
        }else{
            buy.add(price);
        }
        //check match is present
        if(buy.size()>0 && sell.size()>0){
            if(buy.peek() < sell.peek()){
                matchMoney= sell.poll();
                buy.poll(); // since request for buy is satisfied. 
            }
        }
     return matchMoney;
    }
}