
class HashTableFunctions
{
         
   //hash function weights
   // 9 integers, each in the range 0-5 to act as weights for the characters in the keys
   int [] weights = {4, 2, 0, 4, 2, 0, 2, 2, 4};

   public HashTableFunctions(int [] weights){
      this.weights = weights;
   }
   // int [] weights = {4, 2, 0, 4, 2, 0, 2, 2, 4};
   
   // ADD YOUR WEIGHTS INSTEAD OF 1s

   // returns True if the hash table contains string s
   // return False if the hash table does not contain string s
   boolean find ( String s, int h, int hashTableSize, String [] hashTableArray )
   {
      while(hashTableArray[h] != ""){
         if(hashTableArray[h]==s){
            return true;
         }
         else{
            h++;
            h = h%hashTableSize;
         }
         
      }
      return false;
   }
}
