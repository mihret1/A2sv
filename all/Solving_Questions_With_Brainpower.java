class Solution {
    public long mostPoints(int[][] questions) {
        long ans=0;
        HashMap<Integer,Long> map=new HashMap<>();
        for(int i=questions.length-1;i>=0;i--){
            if((i+questions[i][1]+1)>=questions.length){
                ans=Math.max(ans,(long)questions[i][0]);
                map.put(i,ans);
            }
            else {
                ans=Math.max(ans,(long)questions[i][0]+map.get(i+questions[i][1]+1));
                map.put(i,ans);
            }
        }
     return ans;   
    }
}
