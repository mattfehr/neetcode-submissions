class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # ==========================================
        # STEP 1: PARSE THE INPUT & BUILD THE GRAPH
        # ==========================================
        adj_list = {}
        in_degree = {}
        
        # Initialize every unique letter
        for word in words:
            for char in word:
                if char not in adj_list:
                    adj_list[char] = set() #set to avoid duplicate edges
                    in_degree[char] = 0

        # Find sorting relationships
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # Edge Case: Prefix contradiction (e.g., "apple" before "app")
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""  # Invalid order
                
            # Scan for the first mismatch
            min_len = min(len(word1), len(word2))
            for j in range(min_len):
                char1 = word1[j]
                char2 = word2[j]
                
                if char1 != char2: #if they dont match then that must mean word 2 char is after word 1 char
                    if char2 not in adj_list[char1]:
                        adj_list[char1].add(char2)
                        in_degree[char2] += 1
                    break  # Stop checking this pair of words

        # ==========================================
        # STEP 2: RUN KAHN'S ALGORITHM
        # ==========================================
        # Queue up all starting letters (in-degree == 0)
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        sorted_letters = []
        
        while queue:
            current_char = queue.popleft()
            sorted_letters.append(current_char)
            
            # Free up the neighbors dependent on this letter
            for neighbor in adj_list[current_char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # ==========================================
        # STEP 3: VALIDATE THE RESULT (CYCLE CHECK)
        # ==========================================
        # If the output doesn't contain all unique letters, a cycle exists
        if len(sorted_letters) == len(in_degree):
            return "".join(sorted_letters)
        else:
            return ""  # Contradiction found (e.g., A > B and B > A)