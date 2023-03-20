public class ChangeMoney {
    public static void main(String [] args){
        int[] Coins = new int[] {  3, 5, 10, 20, 25, 50};
        int Amount = 2;

        int nChange1 = changeMoney_recursive(Amount, Coins);
        System.out.println("nChange: " +  nChange1);

        int nChange2 = changeMoney_dp(Amount, Coins);
        System.out.println("nChange: " +  nChange2);
    }

    public static int changeMoney_recursive(int Amount, int[] Coins){
        int n_change = Integer.MAX_VALUE;
        if (Amount == 0)
            return 0;
        for (int coin : Coins){
            if (coin <= Amount) {
                int n_change1 = changeMoney_recursive(Amount - coin, Coins);
                if (n_change1 != Integer.MAX_VALUE)
                    n_change = Math.min(n_change, 1 + changeMoney_recursive(Amount - coin, Coins));
            }
        }
        return n_change;
    }

    public static int changeMoney_dp(int Amount, int[] Coins){
        int[] dp = new int[Amount+1];
        dp[0] = 0;
        for (int curr_amount = 1; curr_amount <= Amount; curr_amount++){
            int n_change = Integer.MAX_VALUE;
            for (int coin: Coins){
                if (curr_amount >= coin && dp[curr_amount - coin] != Integer.MAX_VALUE)
                    n_change = Math.min(n_change, 1 + dp[curr_amount - coin]);
            }
            dp[curr_amount] = n_change;
        }
        return dp[Amount];
    }
}

