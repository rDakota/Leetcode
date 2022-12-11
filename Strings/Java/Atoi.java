
public class Atoi {
	
	public static int myAtoi(String s) {
	
		int index = 0;
		int total = 0;
		int sign = 1;
		
		//1. Empty string
		if (s.length() == 0) {
			return 0;
		}

		//2. Remove Spaces
		while(index < s.length() && s.charAt(index) == ' ') {
            index++;
		}
		
		if (index == s.length()) {
			return 0;
		}


		//3. Handle signs
		if(s.charAt(index) == '+' || s.charAt(index) == '-'){
			// Ternary operator
			// if index == +
			// sign gets 1, else gets -1
			sign = s.charAt(index) == '+' ? 1 : -1;
			index ++;
		}
    
		//4. Convert number and avoid overflow
		while(index < s.length()){
			int digit = s.charAt(index) - '0';
			if(digit < 0 || digit > 9) {
				break;
			}

			//  Check if total will be overflow after 10 times and add digit
			//  Integer.MAX_VALUE = 2147483647 and Integer.MIN_VALUE = -2147483648
			if(Integer.MAX_VALUE/10 < total || Integer.MAX_VALUE/10 == total && Integer.MAX_VALUE %10 < digit) {
				// if sign == 1
				// True return sign as max value, false returns sign as min value
				return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
			}

			total = 10 * total + digit;
			index ++;
		}
		return total * sign;
}

	public static void main(String[] args) {
		System.out.println(myAtoi("     -43"));
		System.out.println(myAtoi("4193 with words"));
		System.out.println(myAtoi("420 nobody goes off trail and nobody walks alone"));
		System.out.println(myAtoi(" a652b "));
		System.out.println(myAtoi(" 652b "));
	}

}
