class Solution:
    def interpret(self, command: str) -> str:
        a=""
        for i in range(len(command)):
            if(command[i]=="G"):
                a+="G"
            elif command[i:i+2]== "()":
                a+="o"
            elif command[i:i+4]== "(al)":
                a+="al"
        return(a)
        
            
            
        