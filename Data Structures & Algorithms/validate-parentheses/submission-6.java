public class Solution {
    public boolean isValid(String s) {

        if(s.length() % 2 != 0){
            return false;
        }
        
        Stack<Character> check = new Stack<>();

        for(char c : s.toCharArray()){
            if(c == '(' || c == '[' || c == '{'){
                check.push(c);
            }
            else if (c == ')' && !check.isEmpty() && check.peek() == '('){
                check.pop();
            }
            else if (c == '}' && !check.isEmpty() && check.peek() == '{'){
                check.pop();
            }
            else if (c == ']' && !check.isEmpty() && check.peek() == '['){
                check.pop();
            }
            else{
                return false;
            }
        }

        return check.isEmpty();
    }
}