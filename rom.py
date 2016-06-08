public class RomanNumeral
{
  public static void main (String[]args)
  {
	 System.out.println("Enter a Roman Numeral");
	 String numeral = ReadLib.readString(); 
	
	
	 String newNumeral = numeral.replace("XL", "XXXX"); 
	 String newNumeral2 = newNumeral.replace("XC", "LXXXX"); 
	 String newNumeral3 = newNumeral2.replace("CD", "CCCC"); 
	 String newNumeral4 = newNumeral3.replace("CM", "DCCCC"); 
	 String newNumeral5 = newNumeral4.replace("IV", "IIII"); 
	 String newNumeral6 = newNumeral5.replace("IX", "VIIII"); 
   
	 char romanNumeral = 0;
	 int length = newNumeral6.length(); 
	 int arabicNumber = 0; 
	
	 for (int n = 0; n< length; n++)
	 {
	  romanNumeral = newNumeral6.charAt(n);
	 
	  if ( romanNumeral == 'M')
		{
	   arabicNumber+=1000; 
		}
	   if ( romanNumeral == 'D')
		{
	   arabicNumber+=500; 
	 
		}
	   if ( romanNumeral == 'C')
		{
	   arabicNumber+=100; 
		}
	   if ( romanNumeral == 'L')
		{
	   arabicNumber+=50; 
		}
	   if ( romanNumeral == 'X')
		{
	   arabicNumber+=10; 
		}
	   if ( romanNumeral == 'V')
		{
	   arabicNumber+=5; 
		}
	   if ( romanNumeral == 'I')
		{
	   arabicNumber+=1; 
		}
	 }
	 System.out.println(arabicNumber);
  }
} 
