import static org.junit.Assert.*;

import org.junit.Test;


public class GiaiPTB1Test {
	private GiaiPTB1 giaiPTB1 = new GiaiPTB1();
	/*@Test
	public void test() {
		fail("Not yet implemented");
	}*/
	
	@Test
	public void test1() {
		assertEquals("",-1, giaiPTB1.test(1, 1));
	}
	
	@Test
	public void test2() {
		assertEquals("",9, giaiPTB1.test(-10, 90));
	}

}
