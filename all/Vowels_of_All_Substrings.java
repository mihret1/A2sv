class Solution {
    public long countVowels(String word) {
         long result=0;
         long len=word.length();
        for(int i=0;i<word.length();i++){
             if(word.charAt(i)=='i'||word.charAt(i)=='o'||word.charAt(i)=='a'||
                         word.charAt(i)=='e'||word.charAt(i)=='u')
             {        
             result+=(len-i)*(i+1);
              } }
          return result;
    }
}
