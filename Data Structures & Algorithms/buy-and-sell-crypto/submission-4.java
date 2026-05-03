class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;

        int l =0;
        int r = 1;

        while(r < prices.length){
            if(prices[l] < prices[r]){
                int profit = prices[r] - prices[l];
                maxP = Math.max(profit,maxP);
            }
            else{
                l=r;
                
            }
            r++;
        }
        return maxP;
    }
}
