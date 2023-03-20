import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;

public class ChangeMoneyTest {
    @Test
    public void testChangeMoney_no_Change (){
        int[] Coins = new int[]{3, 5, 10, 20, 25, 50};
        int Amount = 2;

        int nChange = ChangeMoney.changeMoney_recursive(Amount, Coins);
        Assertions.assertEquals(Integer.MAX_VALUE, nChange);
    }

    @Test
    public void testChangeMoney_change_present(){
        int[] Coins = new int[]{1, 2, 3, 5, 10, 20, 25, 50};
        int Amount = 12;

        int nChange = ChangeMoney.changeMoney_recursive(Amount, Coins);
        Assertions.assertEquals(2, nChange);
    }
}
