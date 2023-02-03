class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        SPACE = ' '
        
        max_words = 0
        
        list_of_words = []
        
        for string in sentences:
            
            # We will take each sentence and split it into words.
            word_counter = string.split(SPACE)
            
            # Then we place the words into a list.
            list_of_words += word_counter
            
            # Now we will check the length of the list against the current max_words.
            max_words = max(max_words, len(list_of_words))
            
            # After that, we clear the list for the next iteration.
            list_of_words.clear()
            
        return max_words 
        